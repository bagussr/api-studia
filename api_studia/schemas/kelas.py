from api_studia.modules import BaseModel
from api_studia.models import tugas, blog
from datetime import datetime
from uuid import UUID


class KelasBase(BaseModel):
    owner_id: str
    name: str
    section: str
    code: str


class KelasCreate(KelasBase):
    pass


class Kelas(KelasBase):
    id: UUID
    # tugas_list: list[tugas.Tugas]
    # konten_list: list[blog.Konten]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
