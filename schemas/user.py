from enum import Enum

from pydantic import BaseModel, Field, EmailStr


class Gender(Enum):
    MALE: str = 'Male'
    FEMALE: str = 'Female'


class UserBase(BaseModel):
    email: EmailStr
    username: str = Field(..., min_length=4)


class User(UserBase):
    first_name: str = Field(..., min_length=3, max_length=50)
    last_name: str = Field(..., min_length=3, max_length=50)
    gender: Gender = Gender.FEMALE


class LoginUser(UserBase):
    password: str = Field(..., min_length=8, max_length=50)


class RegisterUser(User, UserBase):
    password: str = Field(..., min_length=8, max_length=50)
