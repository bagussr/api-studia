from api_studia.modules import Session
from api_studia.models.tugas import Tugas
from api_studia.schemas.tugas import TugasCreate


def get_all_tugas_kelas(db: Session, kelas_id: str, skip: int = 0):
    return db.query(Tugas).filter(Tugas.kelas_id == kelas_id).offset(skip).all()


def get_tugas_kelas(db: Session, kelas_id: str, konten_id: str, skip: int = 0):
    return db.query(Tugas).offset(skip).filter(Tugas.kelas_id == kelas_id and Tugas.id == konten_id).first()


def create_tugas_kelas(db: Session, tugas: TugasCreate, kelas_id: str):
    db_tugas = Tugas(**tugas.dict(), kelas_id=kelas_id)
    db.add(db_tugas)
    db.commit()
    db.refresh(db_tugas)
    return db_tugas
