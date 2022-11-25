from api_studia.modules import Session
from api_studia.models.kelas import Kelas
from api_studia.models.userkelas import UserKelas
from api_studia.schemas.kelas import KelasCreate, KelasBase


def get_kelas(db: Session, kelas_id: str):
    return db.query(Kelas).filter(Kelas.id == kelas_id).first()


def get_all_kelas(db: Session, skip: int = 0):
    return db.query(Kelas).offset(skip).all()


async def create_kelas(db: Session, kelas: KelasCreate):
    db_kelas = Kelas(created_by=kelas.created_by, name=kelas.name, section=kelas.section)
    db.add(db_kelas)
    db.commit()
    db.refresh(db_kelas)
    return db_kelas


def delete_kelas(db: Session, kelas_id: str):
    db_kelas = get_kelas(db, kelas_id=kelas_id)
    if db_kelas is None:
        return False
    db.delete(db_kelas)
    db.commit()
    return db_kelas


async def update_kelas(db: Session, kelas_id: str, kelas: KelasBase):
    db_kelas = get_kelas(db, kelas_id=kelas_id)
    if db_kelas is None:
        return False
    db_kelas.name = kelas.name
    db_kelas.section = kelas.section
    db.commit()
    return db_kelas


async def join_kelas(db: Session, user_id: str, code: str):
    db_kelas = db.query(Kelas).filter(Kelas.code == code).first()
    if db_kelas is None:
        return False
    db_join = UserKelas(user_id=user_id, kelas_id=db_kelas.id)
    db.add(db_join)
    db.commit()
    db.refresh(db_join)
    return db_join


def joined_kelas(db: Session, user_id: str):
    return db.query(Kelas).join(UserKelas).filter(UserKelas.user_id == user_id).all()
