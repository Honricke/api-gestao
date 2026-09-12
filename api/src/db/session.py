from sqlmodel import create_engine, Session
from ..configs.settings import settings


postgres_url = f"postgresql://{settings.db.USER}:{settings.db.PASS.get_secret_value()}@{settings.db.HOST}:{settings.db.PORT}/{settings.db.NAME}"
engine = create_engine(postgres_url)

def get_session():
    with Session(engine) as session:
        yield session