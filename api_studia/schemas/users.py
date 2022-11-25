from api_studia.modules import BaseModel
import json

class UserSchema(BaseModel):
    username: str
    email: str
    password: str
    name: str
    address: str
    gender: int


class CreateUserSchema(UserSchema):
    isTeacher: bool = False
    isStudent: bool = False

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value

    class config:
        orm_mode = True