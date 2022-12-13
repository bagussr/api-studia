from api_studia.modules import BaseModel
from datetime import datetime
from pydantic import Field
import random
import string


def randomword(length=10):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


class TugasBase(BaseModel):
    name: str
    description: str
    deadline: datetime = datetime.now()


class TugasCreate(TugasBase):
    id: str = Field(default_factory=randomword)
    pass


class TugasUpdate(TugasBase):
    pass


class Tugas(TugasBase):
    id: str
    kelas_id: str
    craeted_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
