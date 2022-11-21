from sqlalchemy.orm import Session

from api_studia.sql_app import models, schemas


def get_kelas(db: Session, kelas_id: str):
    return db.query(models.Kelas).filter(models.Kelas.id == kelas_id).first()


def get_all_kelas(db: Session, skip: int = 0):
    return db.query(models.Kelas).offset(skip).all()


def create_kelas(db: Session, kelas: schemas.KelasCreate):
    db_kelas = models.Kelas(id=kelas.id,
                            name=kelas.name, section=kelas.section, code=kelas.code)
    db.add(kelas)
    db.commit()
    db.refresh(db_kelas)
    return db_kelas


def get_tugas_kelas(db: Session, kelas_id: str, skip: int = 0):
    return db.query(models.Tugas).offset(skip).filter_by(models.Tugas.kelas_id == kelas_id).all()


def create_tugas_kelas(db: Session, tugas: schemas.TugasCreate, kelas_id: str):
    db_tugas = models.Tugas(**tugas.dict(), kelas_id=kelas_id)
    db.add(db_tugas)
    db.commit()
    db.refresh(db_tugas)
    return db_tugas
