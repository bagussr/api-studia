from api_studia.modules import BaseModel
from api_studia.models import konten, tugas
from datetime import datetime
from uuid import UUID


class JoinKelas(BaseModel):
    user_id: str
    code: str


class KelasBase(BaseModel):
    name: str
    section: str


class KelasCreate(KelasBase):
    pass


class Kelas(KelasBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
