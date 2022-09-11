from pydantic import BaseModel, Field, EmailStr
from typing import List


class Game(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class User(BaseModel):
    id: int
    name: str
    age: int = Field(..., lt=100, gt=0,)
    email: EmailStr

    class Config:
        orm_mode = True


class GameOut(Game):
    users: List[User] = []


class UserOut(User):
    games: List[Game] = []
