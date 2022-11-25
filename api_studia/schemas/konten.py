from api_studia.modules import BaseModel
import json


class KontenSchema(BaseModel):
    name: str
    text: str
    synopsis: str

    class Config:
        orm_mode = True


class CreateKontenSchema(KontenSchema):
    kelas: str
    user_id: str
    pass

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value
