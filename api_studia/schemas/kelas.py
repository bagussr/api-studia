from api_studia.modules import BaseModel
from api_studia.models import tugas, blog
from datetime import datetime
from uuid import UUID

import string
import random


def randomword(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


class KelasBase(BaseModel):
    name: str
    section: str


class KelasCreate(KelasBase):
    created_by: str
    pass


class Kelas(KelasBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
