from api_studia.modules import APIRouter, List, Session, Depends, HTTPException
from api_studia.service.db_service import get_db
from api_studia.schemas.tugas import Tugas, TugasCreate
from api_studia.routes.controller.tugas import create_tugas_kelas, get_all_tugas_kelas, get_tugas_kelas
from api_studia.routes.controller.kelas import get_kelas

tugas_route = APIRouter(prefix="/tugas", tags=["tugas"])


@tugas_route.post("/{kelas_id}")
def create_tugas_kelas_route(kelas_id: str, tugas: TugasCreate, db: Session = Depends(get_db)):
    create_tugas_kelas(db=db, tugas=tugas, kelas_id=kelas_id)
    return {"message": "Tugas berhasil dibuat"}


@tugas_route.get("/{kelas_id}")
def read_all_tugas_kelas(kelas_id: str, skip: int = 0, db: Session = Depends(get_db)):
    db_kelas = get_kelas(db, kelas_id=kelas_id)
    if db_kelas is None:
        raise HTTPException(status_code=404, detail="Kelas Not Found")
    all_tugas_kelas = get_all_tugas_kelas(db, skip=skip, kelas_id=kelas_id)
    return {"tugas": all_tugas_kelas}


@tugas_route.get("/{tugas_id}/{kelas_id}", response_model=Tugas)
def read_tugas_kelas(kelas_id: str, tugas_id: str, skip: int = 0, db: Session = Depends(get_db)):
    tugas_kelas = get_tugas_kelas(db, skip=skip, kelas_id=kelas_id, tugas_id=tugas_id)
    if tugas_kelas is None:
        raise HTTPException(status_code=404, detail="Tugas Not Found")
    return tugas_kelas
