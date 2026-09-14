from fastapi import APIRouter
from .userController import UserController

user_router = APIRouter()

@user_router.get("/{user_id}")
def get_user(user_id: str):
    user = UserController().get_user(user_id)
    return {"message": "User retrieved successfully", 'data': user}
