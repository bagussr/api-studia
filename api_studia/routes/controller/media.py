from api_studia.modules import Session
from api_studia.models.media import Media
from api_studia.schemas.media import CreateMediaSchema


async def create_media(db: Session, medias: CreateMediaSchema):
    media = Media(**medias.dict())
    db.add(media)
    db.commit()
    return media
