from config_data.config import load_config

# можно передать путь к .env, если файл находится не в директории проекта
config = load_config()

bot_token = config.tg_bot.token           # Сохраняем токен в переменную bot_token

# Выводим значения полей экземпляра класса Config на печать, 
# чтобы убедиться, что все данные, получаемые из переменных окружения, доступны
print('BOT_TOKEN:', config.tg_bot.token)
print()
print('config type:', type(config))