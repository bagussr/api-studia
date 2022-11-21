from typing import List

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from api_studia.sql_app import crud, schemas
from api_studia.service.db_service import get_db
from api_studia.routes.controller.kelas import router as kelas_route


@kelas_route.post("/", response_model=schemas.Kelas)
def create_kelas(kelas: schemas.KelasCreate, db: Session = Depends(get_db)):
    return crud.create_kelas(db=db, kelas=kelas)


@kelas_route.get("/", response_model=List[schemas.Kelas])
def read_all_kelas(skip: int = 0, db: Session = Depends(get_db)):
    all_kelas = crud.get_all_kelas(db, skip=skip)
    return all_kelas


@kelas_route.get("/{kelas_id}", response_model=schemas.Kelas)
def read_kelas(kelas_id: str, db: Session = Depends(get_db)):
    db_kelas = crud.get_kelas(db, kelas_id=kelas_id)
    if db_kelas is None:
        raise HTTPException(status_code=404, detail="Kelas Not Found")
    return db_kelas


@kelas_route.post("/{kelas_id}/tugas", response_model=schemas.Tugas)
def create_tugas_kelas(kelas_id: str, tugas: schemas.TugasCreate, db: Session = Depends(get_db)):
    return crud.create_tugas_kelas(db=db, tugas=tugas, kelas_id=kelas_id)


@kelas_route.get("/{kelas_id}/tugas", response_model=List[schemas.Tugas])
def read_all_tugas_kelas(kelas_id: str, skip: int = 0, db: Session = Depends(get_db)):
    db_kelas = crud.get_kelas(db, kelas_id=kelas_id)
    if db_kelas is None:
        raise HTTPException(status_code=404, detail="Kelas Not Found")
    all_tugas_kelas = crud.get_all_tugas_kelas(
        db, skip=skip, kelas_id=kelas_id)
    return all_tugas_kelas


@kelas_route.get("/{kelas_id}/tugas/{tugas_id}", response_model=schemas.Tugas)
def read_tugas_kelas(kelas_id: str, tugas_id: str, skip: int = 0, db: Session = Depends(get_db)):
    tugas_kelas = crud.get_tugas_kelas(
        db, skip=skip, kelas_id=kelas_id, tugas_id=tugas_id)
    if tugas_kelas is None:
        raise HTTPException(status_code=404, detail="Tugas Not Found")
    return tugas_kelas


@kelas_route.post("/{kelas_id}/konten", response_model=schemas.Konten)
def create_konten_kelas(kelas_id: str, konten: schemas.TugasCreate, db: Session = Depends(get_db)):
    return crud.create_konten_kelas(db=db, konten=konten, kelas_id=kelas_id)


@kelas_route.get("/{kelas_id}/konten", response_model=List[schemas.Konten])
def read_all_konten_kelas(kelas_id: str, skip: int = 0, db: Session = Depends(get_db)):
    db_kelas = crud.get_kelas(db, kelas_id=kelas_id)
    if db_kelas is None:
        raise HTTPException(status_code=404, detail="Kelas Not Found")
    all_konten_kelas = crud.get_all_konten_kelas(
        db, skip=skip, kelas_id=kelas_id)
    return all_konten_kelas


@kelas_route.get("/{kelas_id}/konten/{konten_id}", response_model=schemas.Konten)
def read_konten_kelas(kelas_id: str, konten_id: str, skip: int = 0, db: Session = Depends(get_db)):
    konten_kelas = crud.get_konten_kelas(
        db, skip=skip, kelas_id=kelas_id, konten_id=konten_id)
    if konten_kelas is None:
        raise HTTPException(status_code=404, detail="Konten Not Found")
    return konten_kelas


@kelas_route.post("/{kelas_id}/konten/{konten_id}", response_model=schemas.Comment)
def create_comment_konten(konten_id: str, kelas_id: str, comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    db_konten = crud.get_konten_kelas(
        db, kelas_id=kelas_id, konten_id=konten_id)
    if db_konten is None:
        raise HTTPException(status_code=404, detail="Konten Not Found")
    return crud.create_comment_konten(db=db, comment=comment, konten_id=konten_id)


@kelas_route.get("/{kelas_id}/konten/{konten_id}", response_model=List[schemas.Comment])
def read_all_comment_konten(konten_id: str, kelas_id: str, skip: int = 0, db: Session = Depends(get_db)):
    db_konten = crud.get_konten_kelas(
        db, kelas_id=kelas_id, konten_id=konten_id)
    if db_konten is None:
        raise HTTPException(status_code=404, detail="Konten Not Found")
    read_all_comment_konten = crud.get_all_comment_konten(
        db, skip=skip, kelas_id=kelas_id)
    return read_all_comment_konten


@kelas_route.post("/{kelas_id}/konten/{konten_id}/media", response_model=schemas.MediaPhoto)
def create_media_konten(konten_id: str, konten: schemas.MediaPhotoCreate, db: Session = Depends(get_db)):
    return crud.create_media_konten(db=db, konten=konten, konten_id=konten_id)


@kelas_route.get("/{kelas_id}/konten/{konten_id}/media", response_model=List[schemas.Konten])
def read_all_media_konten(konten_id: str, kelas_id: str, skip: int = 0, db: Session = Depends(get_db)):
    db_konten = crud.get_konten_kelas(
        db, kelas_id=kelas_id, konten_id=konten_id)
    if db_konten is None:
        raise HTTPException(status_code=404, detail="Konten Not Found")
    all_media_konten = crud.get_all_media_konten(
        db, skip=skip, kelas_id=kelas_id, konten_id=konten_id)
    return all_media_konten


@kelas_route.get("/{kelas_id}/konten/{konten_id}/media/{media_id}", response_model=schemas.Konten)
def read_media_konten(kelas_id: str, konten_id: str, media_id: int, skip: int = 0, db: Session = Depends(get_db)):
    konten_kelas = crud.get_media_konten(
        db, skip=skip, kelas_id=kelas_id, konten_id=konten_id, media_id=media_id)
    if konten_kelas is None:
        raise HTTPException(status_code=404, detail="Konten Not Found")
    return konten_kelas
