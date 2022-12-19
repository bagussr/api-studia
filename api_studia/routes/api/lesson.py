from api_studia.modules import APIRouter, Depends, HTTPException, status, Session
from api_studia.schemas.lesson import CreateLesson
from api_studia.routes.controller.lesson import create_lesson, get_lesson_kelas, update_lesson, delete_lesson
from api_studia.routes.controller.kelas import get_kelas
from api_studia.service.db_service import get_db
from api_studia.service.auth import get_authorize

lesson_route = APIRouter(prefix="/lesson", tags=["lesson"], dependencies=[Depends(get_authorize)])


@lesson_route.post("/create")
async def create_lesson_route(lesson: CreateLesson, db: Session = Depends(get_db)):
    db_lesson = await create_lesson(db, lesson)
    return {"success": "Success", "data": db_lesson}


@lesson_route.get("/k/{kelas_id}")
def get_lesson_kelas_route(kelas_id: str, db: Session = Depends(get_db)):
    kelas = get_kelas(db, kelas_id=kelas_id)
    if kelas:
        lessons = get_lesson_kelas(db, kelas_id=kelas_id)
        return {"success": "Success", "data": lessons}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Kelas not found")


@lesson_route.put("/update/{lesson_id}")
async def update_lesson_route(lesson_id: str, lesson: CreateLesson, db: Session = Depends(get_db)):
    db_lesson = await update_lesson(db, id=lesson_id, lesson=lesson)
    if db_lesson:
        return {"success": "Success", "data": db_lesson}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lesson not found")


@lesson_route.delete("/delete/{lesson_id}")
def delete_lesson_route(lesson_id: str, db: Session = Depends(get_db)):
    db_lesson = delete_lesson(db, id=lesson_id)
    if db_lesson:
        return {"success": "Success", "data": db_lesson}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lesson not found")
