# Arquivo destinado para agrupamento de todas as configurações do projeto, como configurações de banco de dados, jwt ...
# todas essas configurações vem de outros arquivos, como o database.py e agrupadas aqui.

from pydantic_settings import BaseSettings, SettingsConfigDict
from .database import DBSettings

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env.local', extra='ignore', env_nested_delimiter='__')

    db: DBSettings

settings = Settings()