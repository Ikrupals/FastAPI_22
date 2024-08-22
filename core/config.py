from starlette.config import Config


config = Config(".env")

API_PREFIX: str = "/api"
VERSION: str = config("API_VERSION")
APP_NAME: str = config("APP_NAME")
DEBUG: bool = config("DEBUG", cast=bool, default=False)

POSTGRES_USER: str = config("POSTGRES_USER")
POSTGRES_PASSWORD: str = config("POSTGRES_PASSWORD")
POSTGRES_HOST: str = config("POSTGRES_HOST")
POSTGRES_PORT: str = config("POSTGRES_PORT", cast=int)
POSTGRES_DB: str = config("POSTGRES_DB")

# from starlette.config import Config

# config = Config(".env")

# API_PREFIX = "/api"
# VERSION = config("API_VERSION")
# APP_NAME = config("APP_NAME")
# DEBUG = config("DEBUG", cast=bool, default=False)

# POSTGRES_USER = config("POSTGRES_USER")
# POSTGRES_PASSWORD = config("POSTGRES_PASSWORD")
# POSTGRES_HOST = config("POSTGRES_HOST")
# POSTGRES_PORT = config("POSTGRES_PORT", cast=int)
# POSTGRES_DB = config("POSTGRES_DB")
