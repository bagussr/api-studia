from api_studia.modules import Session
from api_studia.models.tugas import Tugas
from api_studia.schemas.tugas import TugasCreate, TugasUpdate


def get_all_tugas_kelas(db: Session, kelas_id: str, skip: int = 0):
    return db.query(Tugas).filter(Tugas.kelas_id == kelas_id).offset(skip).all()


def get_tugas_kelas(db: Session, kelas_id: str, konten_id: str, skip: int = 0):
    return db.query(Tugas).offset(skip).filter(Tugas.kelas_id == kelas_id and Tugas.id == konten_id).first()


async def create_tugas_kelas(db: Session, tugas: TugasCreate, kelas_id: str):
    db_tugas = Tugas(**tugas.dict(), kelas_id=kelas_id)
    db.add(db_tugas)
    db.commit()
    db.refresh(db_tugas)
    return db_tugas


def delete_tugas(db: Session, tugas_id: str, kelas_id: str):
    db_tugas = Tugas.query.filter(Tugas.id == tugas_id and Tugas.kelas_id == kelas_id).first()
    if db_tugas is None:
        return False
    db.delete(db_tugas)
    db.commit()
    return db_tugas


async def update_tugas(db: Session, tugas_id: str, kelas_id: str, tugas: TugasUpdate):
    db_tugas = Tugas.query.filter(Tugas.id == tugas_id and Tugas.kelas_id == kelas_id).first()
    if db_tugas is None:
        return False
    if tugas.name is not None:
        db_tugas.name = tugas.name
    if tugas.description is not None:
        db_tugas.description = tugas.description
    if tugas.deadline is not None:
        db_tugas.deadline = tugas.deadline
    db.merge(db_tugas)
    db.commit()
    db.refresh(db_tugas)
    return db_tugas
