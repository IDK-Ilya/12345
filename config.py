from dotenv import load_dotenv
import os
from pydantic_settings import BaseSettings, SettingsConfigDict

# class Settings(BaseSettings):
#     CMC_API_KEY: str
#
#     model_config = SettingsConfigDict(env_file=".env")
#
# settings = Settings()

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")