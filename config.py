import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')


class ProdConfig(Config):
    DEBUG = False


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}

