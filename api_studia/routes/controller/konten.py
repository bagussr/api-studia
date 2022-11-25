from api_studia.modules import Session
from api_studia.models.konten import Konten
from api_studia.schemas.konten import KontenSchema


def get_all_konten(db: Session):
    return db.query(Konten).all()


async def create_konten(db: Session, konten: KontenSchema, media_id: int):
    db_konten = Konten(**konten.dict(), photo_id=media_id)
    db.add(db_konten)
    db.commit()
    db.refresh(db_konten)
    return db_konten


def delete_konten(db: Session, konten_id: int):
    db_konten = db.query(Konten).filter(Konten.id == konten_id).first()
    if db_konten:
        db.delete(db_konten)
        db.commit()
        return db_konten
    return False
