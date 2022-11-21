from pydantic import BaseModel
from datetime import datetime


class TugasBase(BaseModel):
    id: str
    name: str
    description: str
    deadline: datetime


class TugasCreate(TugasBase):
    pass


class Tugas(TugasBase):
    kelas_id: int

    class Config:
        orm_mode = True


class KelasBase(BaseModel):
    id: str
    name: str
    section: str
    code: str


class KelasCreate(KelasBase):
    pass


class Kelas(KelasBase):
    tugas_list: list[Tugas] = []

    class Config:
        orm_mode = True
