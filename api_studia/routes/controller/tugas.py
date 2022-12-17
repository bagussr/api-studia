from api_studia.modules import Session
from api_studia.models.tugas import Tugas
from api_studia.schemas.tugas import TugasCreate, TugasUpdate


def get_tugas_lesson(db: Session, lesson_id: int):
    return db.query(Tugas).filter(Tugas.lesson_id == lesson_id).all()


def get_tugas_kelas(db: Session, lesson_id: int, konten_id: str, skip: int = 0):
    return db.query(Tugas).offset(skip).filter(Tugas.lesson_id == lesson_id and Tugas.id == konten_id).first()


async def create_tugas_kelas(db: Session, tugas: TugasCreate, lesson_id: str):
    db_tugas = Tugas(**tugas.dict(), lesson_id=lesson_id)
    db.add(db_tugas)
    db.commit()
    db.refresh(db_tugas)
    return db_tugas


def delete_tugas(db: Session, tugas_id: str):
    db_tugas = Tugas.query.filter(Tugas.id == tugas_id).first()
    if db_tugas is None:
        return False
    db.delete(db_tugas)
    db.commit()
    return db_tugas


async def update_tugas(db: Session, tugas_id: str, tugas: TugasUpdate):
    db_tugas = Tugas.query.filter(Tugas.id == tugas_id).first()
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
