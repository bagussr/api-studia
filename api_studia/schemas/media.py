from api_studia.modules import BaseModel


class MediaSchema(BaseModel):
    name: str
    url: str
    base_url: str
    size: str
    type: str

    class Config:
        orm_mode = True


class CreateMediaSchema(MediaSchema):
    pass
