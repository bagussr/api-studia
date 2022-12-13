from api_studia.modules import BaseModel
import json


class UserSchema(BaseModel):
    name: str
    address: str
    gender: bool


class CreateUserSchema(UserSchema):
    username: str
    email: str
    password: str
    isTeacher: bool = False
    isStudent: bool = False

    class config:
        orm_mode = True


class LoginSchema(BaseModel):
    username: str
    password: str

    class config:
        orm_mode = True
