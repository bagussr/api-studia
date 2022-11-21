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
    all_tugas_kelas = crud.get_tugas_kelas(db, skip=skip, kelas_id=kelas_id)
    return all_tugas_kelas
