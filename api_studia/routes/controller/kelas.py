from api_studia.modules import Session
from api_studia.models.kelas import Kelas
from api_studia.schemas.kelas import KelasCreate


def get_kelas(db: Session, kelas_id: str):
    return db.query(Kelas).filter(Kelas.id == kelas_id).first()


def get_all_kelas(db: Session, skip: int = 0):
    return db.query(Kelas).offset(skip).all()


def create_kelas(db: Session, kelas: KelasCreate):
    db_kelas = Kelas(id=kelas.id, name=kelas.name, section=kelas.section, code=kelas.code)
    db.add(kelas)
    db.commit()
    db.refresh(db_kelas)
    return db_kelas
