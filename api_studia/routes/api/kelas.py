from api_studia.modules import Session, APIRouter, Depends, HTTPException, status, List
from api_studia.service.db_service import get_db
from api_studia.routes.controller.kelas import get_kelas, get_all_kelas, create_kelas
from api_studia.schemas.kelas import KelasCreate, Kelas

kelas_route = APIRouter(prefix="/kelas", tags=["kelas"])


@kelas_route.post("/")
async def create_kelas_route(kelas: KelasCreate, db: Session = Depends(get_db)):
    data = await create_kelas(db, kelas)
    return {"message": "success"}


@kelas_route.get("/")
def read_all_kelas(skip: int = 0, db: Session = Depends(get_db)):
    all_kelas = get_all_kelas(db, skip=skip)
    return {"data": all_kelas}


@kelas_route.get("/{kelas_id}")
def read_kelas(kelas_id: str, db: Session = Depends(get_db)):
    db_kelas = get_kelas(db, kelas_id=kelas_id)
    if db_kelas is None:
        raise HTTPException(status_code=404, detail="Kelas Not Found")
    return {"data": db_kelas}


# @kelas_route.post("/{kelas_id}/konten", response_model=schemas.Konten)
# def create_konten_kelas(kelas_id: str, konten: schemas.TugasCreate, db: Session = Depends(get_db)):
#     return crud.create_konten_kelas(db=db, konten=konten, kelas_id=kelas_id)


# @kelas_route.get("/{kelas_id}/konten", response_model=List[schemas.Konten])
# def read_all_konten_kelas(kelas_id: str, skip: int = 0, db: Session = Depends(get_db)):
#     db_kelas = crud.get_kelas(db, kelas_id=kelas_id)
#     if db_kelas is None:
#         raise HTTPException(status_code=404, detail="Kelas Not Found")
#     all_konten_kelas = crud.get_all_konten_kelas(db, skip=skip, kelas_id=kelas_id)
#     return all_konten_kelas


# @kelas_route.get("/{kelas_id}/konten/{konten_id}", response_model=schemas.Konten)
# def read_konten_kelas(kelas_id: str, konten_id: str, skip: int = 0, db: Session = Depends(get_db)):
#     konten_kelas = crud.get_konten_kelas(db, skip=skip, kelas_id=kelas_id, konten_id=konten_id)
#     if konten_kelas is None:
#         raise HTTPException(status_code=404, detail="Konten Not Found")
#     return konten_kelas


# @kelas_route.post("/{kelas_id}/konten/{konten_id}", response_model=schemas.Comment)
# def create_comment_konten(konten_id: str, kelas_id: str, comment: schemas.CommentCreate, db: Session = Depends(get_db)):
#     db_konten = crud.get_konten_kelas(db, kelas_id=kelas_id, konten_id=konten_id)
#     if db_konten is None:
#         raise HTTPException(status_code=404, detail="Konten Not Found")
#     return crud.create_comment_konten(db=db, comment=comment, konten_id=konten_id)


# @kelas_route.get("/{kelas_id}/konten/{konten_id}", response_model=List[schemas.Comment])
# def read_all_comment_konten(konten_id: str, kelas_id: str, skip: int = 0, db: Session = Depends(get_db)):
#     db_konten = crud.get_konten_kelas(db, kelas_id=kelas_id, konten_id=konten_id)
#     if db_konten is None:
#         raise HTTPException(status_code=404, detail="Konten Not Found")
#     read_all_comment_konten = crud.get_all_comment_konten(db, skip=skip, kelas_id=kelas_id)
#     return read_all_comment_konten


# @kelas_route.post("/{kelas_id}/konten/{konten_id}/media", response_model=schemas.MediaPhoto)
# def create_media_konten(konten_id: str, konten: schemas.MediaPhotoCreate, db: Session = Depends(get_db)):
#     return crud.create_media_konten(db=db, konten=konten, konten_id=konten_id)


# @kelas_route.get("/{kelas_id}/konten/{konten_id}/media", response_model=List[schemas.Konten])
# def read_all_media_konten(konten_id: str, kelas_id: str, skip: int = 0, db: Session = Depends(get_db)):
#     db_konten = crud.get_konten_kelas(db, kelas_id=kelas_id, konten_id=konten_id)
#     if db_konten is None:
#         raise HTTPException(status_code=404, detail="Konten Not Found")
#     all_media_konten = crud.get_all_media_konten(db, skip=skip, kelas_id=kelas_id, konten_id=konten_id)
#     return all_media_konten


# @kelas_route.get("/{kelas_id}/konten/{konten_id}/media/{media_id}", response_model=schemas.Konten)
# def read_media_konten(kelas_id: str, konten_id: str, media_id: int, skip: int = 0, db: Session = Depends(get_db)):
#     konten_kelas = crud.get_media_konten(db, skip=skip, kelas_id=kelas_id, konten_id=konten_id, media_id=media_id)
#     if konten_kelas is None:
#         raise HTTPException(status_code=404, detail="Konten Not Found")
#     return konten_kelas
