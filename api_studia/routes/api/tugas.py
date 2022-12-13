from api_studia.modules import APIRouter, Session, Depends, HTTPException, UploadFile, File, deta, io
from api_studia.service.db_service import get_db
from api_studia.schemas.tugas import Tugas, TugasCreate
from api_studia.routes.controller.tugas import (
    create_tugas_kelas,
    get_all_tugas_kelas,
    get_tugas_kelas,
    delete_tugas,
    update_tugas,
)
from api_studia.routes.controller.kelas import get_kelas
from api_studia.service.auth import get_authorize, teacher_authorize

tugas_route = APIRouter(prefix="/tugas", tags=["tugas"])


@tugas_route.post("/{kelas_id}", dependencies=[Depends(get_authorize), Depends(teacher_authorize)])
async def create_tugas_kelas_route(kelas_id: str, tugas: TugasCreate, db: Session = Depends(get_db)):
    await create_tugas_kelas(db=db, tugas=tugas, kelas_id=kelas_id)
    return {"message": "Tugas berhasil dibuat"}


@tugas_route.get("/{kelas_id}", dependencies=[Depends(get_authorize)])
def read_all_tugas_kelas(kelas_id: str, skip: int = 0, db: Session = Depends(get_db)):
    db_kelas = get_kelas(db, kelas_id=kelas_id)
    if db_kelas is None:
        raise HTTPException(status_code=404, detail="Kelas Not Found")
    all_tugas_kelas = get_all_tugas_kelas(db, skip=skip, kelas_id=kelas_id)
    return {"tugas": all_tugas_kelas}


@tugas_route.get("/{tugas_id}/k/{kelas_id}", dependencies=[Depends(get_authorize)])
def read_tugas_kelas(kelas_id: str, tugas_id: str, skip: int = 0, db: Session = Depends(get_db)):
    tugas_kelas = get_tugas_kelas(db, skip=skip, kelas_id=kelas_id, tugas_id=tugas_id)
    if tugas_kelas is None:
        raise HTTPException(status_code=404, detail="Tugas Not Found")
    return tugas_kelas


@tugas_route.post("/upload/", dependencies=[Depends(get_authorize)])
def upload_tugas(file: UploadFile = File()):
    print(file.filename)
    return {"message": "Upload Tugas berhasil"}


@tugas_route.delete("/{tugas_id}/k/{kelas_id}", dependencies=[Depends(get_authorize), Depends(teacher_authorize)])
def delete_tugas_kelas(kelas_id: str, tugas_id: str, db: Session = Depends(get_db)):
    db_tugas = delete_tugas(db, tugas_id=tugas_id, kelas_id=kelas_id)
    if db_tugas is False:
        raise HTTPException(status_code=404, detail="Tugas Not Found")
    return {"message": "Tugas berhasil dihapus"}


@tugas_route.put("/{tugas_id}/k/{kelas_id}", dependencies=[Depends(get_authorize), Depends(teacher_authorize)])
def update_tugas_kelas(kelas_id: str, tugas_id: str, tugas: TugasCreate, db: Session = Depends(get_db)):
    db_tugas = update_tugas(db, tugas_id=tugas_id, kelas_id=kelas_id, tugas=tugas)
    if db_tugas is False:
        raise HTTPException(status_code=404, detail="Tugas Not Found")
    return {"message": "Tugas berhasil diupdate"}
