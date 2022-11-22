from api_studia.modules import BaseModel
from datetime import datetime
from uuid import UUID


class TugasBase(BaseModel):
    name: str
    description: str
    deadline: datetime


class TugasCreate(TugasBase):
    pass


class Tugas(TugasBase):
    id: str
    kelas_id: UUID
    craeted_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
