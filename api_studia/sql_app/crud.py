from sqlalchemy.orm import Session

from api_studia.sql_app import models, schemas


def get_all_tugas_kelas(db: Session, kelas_id: str, skip: int = 0):
    return db.query(models.Tugas).offset(skip).filter_by(models.Tugas.kelas_id == kelas_id).all()


def get_tugas_kelas(db: Session, kelas_id: str, konten_id: str, skip: int = 0):
    return (
        db.query(models.Tugas)
        .offset(skip)
        .filter(models.Tugas.kelas_id == kelas_id and models.Tugas.id == konten_id)
        .first()
    )


def create_tugas_kelas(db: Session, tugas: schemas.TugasCreate, kelas_id: str):
    db_tugas = models.Tugas(**tugas.dict(), kelas_id=kelas_id)
    db.add(db_tugas)
    db.commit()
    db.refresh(db_tugas)
    return db_tugas


def get_all_konten_kelas(db: Session, kelas_id: str, skip: int = 0):
    return db.query(models.Konten).offset(skip).filter_by(models.Konten.kelas_id == kelas_id).all()


def get_konten_kelas(db: Session, kelas_id: str, konten_id: str, skip: int = 0):
    return (
        db.query(models.Konten)
        .offset(skip)
        .filter(models.Konten.kelas_id == kelas_id and models.Konten.id == konten_id)
        .first()
    )


def create_konten_kelas(db: Session, konten: schemas.KontenCreate, kelas_id: str):
    db_konten = models.Konten(**konten.dict(), kelas_id=kelas_id)
    db.add(db_konten)
    db.commit()
    db.refresh(db_konten)
    return db_konten


def get_all_comment_konten(db: Session, kelas_id: str, konten_id: str, skip: int = 0):
    return (
        db.query(models.Comment)
        .offset(skip)
        .filter_by(models.Comment.konten_id == konten_id and models.Konten.kelas_id == kelas_id)
        .all()
    )


def create_comment_konten(db: Session, comment: schemas.CommentCreate, konten_id: str):
    db_comment = models.Comment(**comment.dict(), konten_id=konten_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def get_all_media_konten(db: Session, kelas_id: str, konten_id: str, skip: int = 0):
    return (
        db.query(models.MediaPhoto)
        .offset(skip)
        .filter_by(models.MediaPhoto.konten_id == konten_id and models.Konten.kelas_id == kelas_id)
        .all()
    )


def get_media_konten(db: Session, kelas_id: str, konten_id: str, media_id: int, skip: int = 0):
    return (
        db.query(models.MediaPhoto)
        .offset(skip)
        .filter(
            models.MediaPhoto.konten_id == konten_id
            and models.Konten.kelas_id == kelas_id
            and models.MediaPhoto.id == media_id
        )
        .first()
    )


def create_media_konten(db: Session, konten: schemas.KontenCreate, konten_id: str):
    db_media = models.Tugas(**konten.dict(), konten_id=konten_id)
    db.add(db_media)
    db.commit()
    db.refresh(db_media)
    return db_media
