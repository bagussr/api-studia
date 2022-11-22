from api_studia.modules import BaseModel
from api_studia.models import tugas, blog


class KelasBase(BaseModel):
    id: str
    name: str
    section: str
    code: str


class KelasCreate(KelasBase):
    pass


class Kelas(KelasBase):
    tugas_list: list[tugas.Tugas]
    konten_list: list[blog.Konten]

    class Config:
        orm_mode = True
