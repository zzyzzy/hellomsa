from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    userid: str
    name: str
    email: str


class UserLogin(BaseModel):
    userid: str
    passwd: str


class UserCreate(UserBase):
    passwd: str


class User(UserBase):
    mno: int
    # regdate: datetime
    regdate: str

    class Config:
        from_attributes=True


class Token(BaseModel):
    access_token: str
    token_type: str
