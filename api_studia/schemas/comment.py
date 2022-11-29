from api_studia.modules import BaseModel


class CommentBase(BaseModel):
    text: str


class CommentCreate(CommentBase):
    konten_id: int
    pass
