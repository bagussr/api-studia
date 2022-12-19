from api_studia.modules import BaseModel, Optional
import json


class KontenSchema(BaseModel):
    name: str
    text: str
    synopsis: str

    class Config:
        orm_mode = True


class CreateKontenSchema(KontenSchema):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value


class UpdatedKontenSchema(BaseModel):
    name: Optional[str]
    text: Optional[str]
    synopsys: Optional[str]
