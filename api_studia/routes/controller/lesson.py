from api_studia.modules import Session
from api_studia.schemas.lesson import CreateLesson
from api_studia.models.lesson import Lesson


async def create_lesson(db: Session, lesson: CreateLesson):
    db_lesson = Lesson(**lesson.dict())
    db.add(db_lesson)
    db.commit()
    return db_lesson


def get_lesson(db: Session, id: int):
    return db.query(Lesson).filter(Lesson.id == id).first()


def get_lesson_kelas(db: Session, kelas_id: str):
    db_lesson = db.query(Lesson).filter(Lesson.kelas_id == kelas_id).all()
    return db_lesson


async def update_lesson(db: Session, lesson: CreateLesson, id: int):
    db_lesson = db.query(Lesson).filter(Lesson.id == id).first()
    if lesson.name:
        db_lesson.name = lesson.name
    if lesson.deskripsi:
        db_lesson.deskripsi = lesson.deskripsi
    db.merge(db_lesson)
    db.commit()
    return db_lesson


def delete_lesson(db: Session, id: int):
    db_lesson = db.query(Lesson).filter(Lesson.id == id).first()
    if db_lesson:
        db.delete(db_lesson)
        db.commit()
        return db_lesson
    return False
