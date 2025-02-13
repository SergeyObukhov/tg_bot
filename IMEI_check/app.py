from flask import Flask, request, jsonify
import requests
import telebot
from datetime import datetime
from config import Config, load_config

app = Flask(__name__)

# Загружаем конфиг в переменную config
config: Config = load_config()

# Белый список пользователей
WHITELIST = {123456789}  # Замените на реальные Telegram ID

# Токен API imeicheck.net
SERVICE_TOKEN = config.service.token
SERVICE_URL = config.service.url

# Токен эндпоинта API для внешних запросов
ENDPOINT_TOKEN = config.api_access.token

# Инициализация Telegram-бота
bot = telebot.TeleBot(config.tg_bot.token)

# Функция для проверки IMEI через API imeicheck.net
def check_imei(imei):
    headers = {
        'Authorization': f'Bearer {SERVICE_TOKEN}',
        'Content-Type': 'application/json'
    }
    response = requests.post(SERVICE_URL, json={'imei': imei}, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None

# Функция для форматирования ответа для пользователей телеграм
def format_response(data):
    # обработка ошибки подключения к сервису, и ситуации 'status': 'unsuccessful'
    if not data or 'properties' not in data or not isinstance(data['properties'], dict):
        return "Информация об устройстве не найдена."

    properties = data['properties']
    formatted_text = (
        f"📱 *Информация об устройстве:*\n\n"
        f"• *Модель устройства:* {properties.get('apple/modelName', 'Неизвестно')}\n"
        f"• *Название модели:* {properties.get('modelDesc', 'Неизвестно')}\n"
        f"• *IMEI:* {properties.get('imei', 'Неизвестно')}\n"
        f"• *IMEI 2:* {properties.get('imei2', 'Неизвестно')}\n"
        f"• *Серийный номер:* {properties.get('serial', 'Неизвестно')}\n"
        f"• *MEID:* {properties.get('meid', 'Неизвестно')}\n"
        f"• *Дата покупки:* {datetime.fromtimestamp(properties.get('estPurchaseDate', 0)).strftime('%Y-%m-%d') if properties.get('estPurchaseDate') else 'Неизвестно'}\n"
        f"• *Гарантия:* {'Есть' if properties.get('warrantyStatus') == 'In Warranty' else 'Нет'}\n"
        f"• *Было в ремонте:* {'Да' if properties.get('replaced') else 'Нет'}\n"
        f"• *Режим пропажи:* {'Активен' if properties.get('lostMode') else 'Не активен'}\n"
        f"• *Статус блокировки (США):* {properties.get('usaBlockStatus', 'Неизвестно')}\n"
        f"• *Сеть:* {properties.get('network', 'Неизвестно')}\n"
        f"• *Сим-лок:* {'Да' if properties.get('simLock') else 'Нет'}\n"
        f"• *Режим FMI (Find My iPhone):* {'Включен' if properties.get('fmiOn') else 'Выключен'}\n"
    )
    return formatted_text

# Обработчик сообщений в Telegram
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    if user_id not in WHITELIST:
        bot.reply_to(message, 'Доступ запрещен.')
        return

    imei = message.text
    if not imei.isdigit() or len(imei) != 15:
        bot.reply_to(message, 'Некорректный IMEI. IMEI должен состоять из 15 цифр.')
        return

    result = check_imei(imei)
    if result:
        formatted_result = format_response(result)
        bot.reply_to(message, formatted_result, parse_mode='Markdown')
    else:
        bot.reply_to(message, 'Ошибка при проверке IMEI. Попробуйте позже.')

# Эндпоинт API для проверки IMEI
@app.route('/api/check-imei', methods=['POST'])
def api_check_imei():
    data = request.json
    imei = data.get('imei')
    token = data.get('token')

    if not imei or not token:
        return jsonify({'error': 'Необходимо указать IMEI и токен.'}), 400

    if token != ENDPOINT_TOKEN:
        return jsonify({'error': 'Неверный токен.'}), 403

    result = check_imei(imei)
    if result:
        return jsonify(result)
    return jsonify({'error': 'Ошибка при проверке IMEI.'}), 500

# Запуск Flask-приложения и Telegram-бота
if __name__ == '__main__':
    from threading import Thread

    # Запуск Flask-приложения в отдельном потоке
    Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 5000}).start()

    # Запуск Telegram-бота
    bot.polling(none_stop=True)