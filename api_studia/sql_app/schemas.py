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


class MediaPhotoBase(BaseModel):
    id: int
    konten_id: str
    name: str
    url: str
    base_url: str
    size: str


class MediaPhotoCreate(MediaPhotoBase):
    pass


class MediaPhoto(MediaPhotoBase):

    class Config:
        orm_mode = True


class CommentBase(BaseModel):
    id: int
    konten_id: str
    user_id: int
    release_date: str
    text: str


class CommentCreate(CommentBase):
    pass


class Comment(CommentBase):

    class Config:
        orm_mode = True


class KontenBase(BaseModel):
    id: str
    kelas_id: str
    photo_id: str
    name: str
    release_date: str
    synopsis: str


class KontenCreate(KontenBase):
    pass


class Konten(KontenBase):
    comment_list: list[Comment] = []

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
    konten_list: list[Konten] = []

    class Config:
        orm_mode = True