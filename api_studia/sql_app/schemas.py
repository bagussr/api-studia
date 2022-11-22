from pydantic import BaseModel
from datetime import datetime


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
