from api_studia.modules import BaseModel


class LessonSchema(BaseModel):
    name: str
    kelas_id: str
    deskripsi: str
    detail: str

    class Config:
        orm_mode = True


class CreateLesson(LessonSchema):
    pass


class ReadLesson(LessonSchema):
    id: str
    created_at: str
    updated_at: str
