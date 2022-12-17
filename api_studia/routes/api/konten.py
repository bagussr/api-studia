from api_studia.modules import (
    Session,
    APIRouter,
    Depends,
    HTTPException,
    UploadFile,
    File,
    os,
    pathlib,
    io,
    deta,
    AuthJWT,
)
from api_studia.service.db_service import get_db
from api_studia.routes.controller.konten import (
    get_all_konten,
    create_konten,
    delete_konten,
    get_all_konten_kelas,
    get_konten_kelas,
    update_konten,
    get_konten_by_user,
)
from api_studia.routes.controller.media import create_media
from api_studia.routes.controller.kelas import get_kelas
from api_studia.schemas.konten import CreateKontenSchema, UpdatedKontenSchema
from api_studia.schemas.media import CreateMediaSchema
from api_studia.service.auth import get_authorize, admin_authorize
from api_studia.service.utils import resize_image

x = pathlib.Path("public/asset/image").absolute()

konten_route = APIRouter(prefix="/konten", tags=["konten"], dependencies=[Depends(get_authorize)])


@konten_route.get("/")
def get_all_konten_route(db: Session = Depends(get_db)):
    konten = get_all_konten(db)
    return {"message": "success", "data": konten}


@konten_route.get("/{kelas_id}")
def read_all_konten_kelas(kelas_id: str, db: Session = Depends(get_db)):
    db_kelas = get_kelas(db, kelas_id=kelas_id)
    if db_kelas is None:
        raise HTTPException(status_code=404, detail="Kelas Not Found")
    all_konten_kelas = get_all_konten_kelas(db, kelas_id=kelas_id)
    return {"message": "success", "data": all_konten_kelas}


@konten_route.post("/")
async def create_new_konten_route(
    kontens: CreateKontenSchema,
    file: UploadFile = File(),
    Authorize: AuthJWT = Depends(),
    db: Session = Depends(get_db),
):
    drive = deta.Drive("konten")
    image = resize_image(file.file)
    drive.put(file.filename, image.getvalue())
    media = await create_media(
        db,
        CreateMediaSchema(
            name=file.filename,
            url=f"/media/konten/{file.filename.split('.')[0]}",
            base_url="media/konten",
            size=len(image.getvalue()),
            type=file.content_type,
        ),
    )
    konten = await create_konten(db, kontens, media.id, Authorize.get_jwt_subject())
    return {"message": "success", "data": konten}


@konten_route.delete("/{konten_id}")
def delete_konten_route(konten_id: int, db: Session = Depends(get_db)):
    konten = delete_konten(db, konten_id)
    if konten:
        return {"message": "success"}
    raise HTTPException(status_code=404, detail="Konten not found")


@konten_route.put("/{konten_id}")
async def update_konten_route(konten_id: int, kontens: UpdatedKontenSchema, db: Session = Depends(get_db)):
    konten = update_konten(db, konten_id, kontens)
    if konten:
        return {"message": "success", "data": konten}
    raise HTTPException(status_code=404, detail="Konten not found")


@konten_route.get(
    "/{konten_id}/k/{kelas_id}",
)
def read_konten_kelas(kelas_id: str, konten_id: str, skip: int = 0, db: Session = Depends(get_db)):
    konten_kelas = get_konten_kelas(db, skip=skip, kelas_id=kelas_id, konten_id=konten_id)
    if konten_kelas is None:
        raise HTTPException(status_code=404, detail="Konten Not Found")
    return {"message": "success", "data": konten_kelas}


@konten_route.get(
    "/u/{user_id}",
)
def read_konten_user(user_id: str, db: Session = Depends(get_db)):
    konten_user = get_konten_by_user(db, user_id=user_id)
    if konten_user is None:
        raise HTTPException(status_code=404, detail="Konten Not Found")
    return {"message": "success", "data": konten_user}
