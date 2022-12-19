from api_studia.modules import BaseModel
from api_studia.models import konten, tugas
from datetime import datetime
from uuid import UUID
import random
import string
from pydantic import Field


def randomword(length=10):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


class JoinKelas(BaseModel):
    user_id: str
    code: str


class KelasBase(BaseModel):
    name: str
    section: str


class KelasCreate(KelasBase):
    code: str = Field(default_factory=randomword)
    pass


class Kelas(KelasBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
