from api_studia.modules import Session
from api_studia.models.konten import Konten
from api_studia.schemas.konten import KontenSchema, UpdatedKontenSchema


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


def get_all_konten_kelas(db: Session, kelas_id: int):
    return db.query(Konten).filter(Konten.kelas_id == kelas_id).all()


def get_konten_kelas(db: Session, kelas_id: str, konten_id: str, skip: int = 0):
    return db.query(Konten).offset(skip).filter(Konten.kelas_id == kelas_id and Konten.id == konten_id).first()

async def update_konten(db: Session, konten: UpdatedKontenSchema, konten_id: int):
    db_konten = db.query(Konten).filter(Konten.id == konten_id).first()
    if db_konten:
        if konten.name:
            db_konten.name = konten.name
        if konten.text:
            db_konten.text = konten.text
        if konten.synopsis:
            db_konten.synopsis = konten.synopsis
        db.merge(db_konten)
        db.commit()
        db.refresh(db_konten)
        return db_konten
    return False
