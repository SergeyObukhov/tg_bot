from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str            # Токен для доступа к телеграм-боту 


@dataclass
class ApiAccess:
    token: str            # Токен для доступа по API 


@dataclass
class Service:
    token: str            # Токен для подключения к источнику данных
    url: str              # URL источника данных
    account_url: str      # URL для проверки баланса


@dataclass
class Config:
    tg_bot: TgBot
    api_access: ApiAccess
    service: Service


def load_config(path: str | None = None) -> Config:
    '''
    Функция для чтения переменных из окружения .env
    и записи их в объект конфигурации
    '''
    env = Env()
    env.read_env(path)
    config = Config(
        tg_bot=TgBot(token=env('TELEGRAM_TOKEN')),
        api_access=ApiAccess(token=env('API_ACCESS_TOKEN')),
        service=Service(
            token=env('SERVICE_TOKEN'),
            url=env('SERVICE_URL'),
            account_url=env('SERVICE_ACCOUNT_URL') 
        )
    )    
    return config