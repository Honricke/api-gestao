from sqlmodel import SQLModel, Field
import uuid

class UserBase(SQLModel):
    name: str = Field(default=None)
    email: str = Field(default=None, unique=True)

class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid7, primary_key=True)
    password_hash: str

class UserPublic(UserBase):
    id: str

class UserCreate(UserBase):
    password: str