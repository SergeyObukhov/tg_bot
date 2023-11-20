from config_data.config import load_config

# можно передать путь к .env, если файл находится не в директории проекта
config = load_config()

bot_token = config.tg_bot.token           # Сохраняем токен в переменную bot_token
superadmin = config.tg_bot.admin_ids[0]   # Сохраняем ID админа в переменную superadmin

# Выводим значения полей экземпляра класса Config на печать, 
# чтобы убедиться, что все данные, получаемые из переменных окружения, доступны
print('BOT_TOKEN:', config.tg_bot.token)
print('ADMIN_IDS:', config.tg_bot.admin_ids)
print()
print('DATABASE:', config.db.database)
print('DB_HOST:', config.db.db_host)
print('DB_USER:', config.db.db_user)
print('DB_PASSWORD:', config.db.db_password)
print()
print('config type:', type(config))