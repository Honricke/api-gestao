from sqlmodel import Session
from ..db.session import engine
from .userModel import User

class UserController:
    def get_user(self, user_id: str):
        with Session(engine) as session:
            return session.get(User, user_id)
