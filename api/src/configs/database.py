import os
from sqlmodel import create_engine, Session
from pydantic import BaseModel, SecretStr

class DBSettings(BaseModel):
    HOST: str
    PASS: SecretStr
    NAME: str
    USER: str
    PORT: str


