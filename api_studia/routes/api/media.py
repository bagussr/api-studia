from api_studia.modules import (
    APIRouter,
    Form,
    File,
    UploadFile,
    StreamingResponse,
    deta,
    io,
    Session,
    Depends,
    os,
    PUBLIC_DIR,
    BackgroundTasks,
    FileResponse,
    HTTPException,
    status,
    AuthJWT,
)
from api_studia.routes.controller.users import edit_photo
from api_studia.routes.controller.media import create_media
from api_studia.schemas.media import CreateMediaSchema
from api_studia.service.db_service import get_db
from api_studia.service.auth import get_authorize

from api_studia.service.utils import detete_local_file


media_route = APIRouter(prefix="/media", tags=["media"])


@media_route.post("/photos/seeds")
async def seed_media(db: Session = Depends(get_db)):
    # drive = deta.Drive("photos")
    list_folder = os.listdir(os.path.join(PUBLIC_DIR, "asset/image/profile"))
    for x in list_folder:
        for file in os.listdir(os.path.join(PUBLIC_DIR, "asset/image/profile", x)):
            with open(os.path.join(PUBLIC_DIR, f"asset/image/profile/{x}", file.split(".")[0] + ".png"), "rb") as f:
                # drive.put(file, io.BytesIO(f.read()))
                content = CreateMediaSchema(
                    name=file.split(".")[0] + ".png",
                    url="/media/photo/" + file.split(".")[0],
                    base_url="/media/photo",
                    size=len(io.BytesIO(f.read()).read()),
                )
            await create_media(db, content)

    return {"success": "Succes"}


@media_route.get("/photos")
def get_all():
    drive = deta.Drive("photos")
    return {"message": "success", "list": drive.list()["names"]}


@media_route.get("/photos/{filename}")
def get_photo(filename: str):
    drive = deta.Drive("photos")
    file = drive.get(f"{filename}.png")
    return StreamingResponse(file.iter_lines(), media_type="image/png")


@media_route.post("/photos", dependencies=[Depends(get_authorize)])
async def add_photo_profile(
    file: UploadFile = File(...),
    filename: str = Form(...),
    db: Session = Depends(get_db),
    Authorize: AuthJWT = Depends(),
):

    try:
        drive = deta.Drive("photos")
        drive.put(f"{filename}.png", io.BytesIO(file.file.read()))
        content = CreateMediaSchema(
            name=filename,
            url=f"/media/photos/{filename}",
            base_url=f"/media/photos/",
            size=len(io.BytesIO(file.file.read()).read()),
        )
        media = await create_media(db, content)
        await edit_photo(db, Authorize.get_jwt_subject(), media.id)
        return {"message": "success"}
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail={"error": str(e)})


@media_route.post("/backgrounds/seeds")
async def background_seeds(db: Session = Depends(get_db)):
    try:
        # drive = deta.Drive("backgrounds")
        for file in os.listdir(os.path.join(PUBLIC_DIR, "asset/image/background")):
            with open(os.path.join(PUBLIC_DIR, f"asset/image/background", file), "rb") as f:
                # drive.put(file, io.BytesIO(f.read()))
                content = CreateMediaSchema(
                    name=file.split(".")[0] + ".png",
                    url="/media/backgrounds/" + file.split(".")[0],
                    base_url="/media/backgrounds",
                    size=len(io.BytesIO(f.read()).read()),
                )
            await create_media(db, content)
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail={"error": str(e)}) from e
    return {"message": "success"}


@media_route.get("/backgrounds")
def get_all():
    drive = deta.Drive("backgrounds")
    return {"message": "success", "list": drive.list()["names"]}


@media_route.post("/backgrounds")
async def add_background(background: UploadFile = File(...), filename: str = Form(...), db: Session = Depends(get_db)):
    drive = deta.Drive("backgrounds")
    drive.put(f"{filename}.png", io.BytesIO(background.file.read()))
    content = CreateMediaSchema(
        name=filename,
        url=f"/media/backgrounds/{filename}",
        base_url=f"/media/backgrounds/",
        size=len(await background.read()),
    )
    create_media(db, content)
    return {"message": "success"}


@media_route.get("/backgrounds/{filename}")
def get_photo(filename: str):
    drive = deta.Drive("backgrounds")
    file = drive.get(f"{filename}.jpg")
    if file:
        return StreamingResponse(file.iter_lines(), media_type="image/jpeg")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"error": "Not Found"})


@media_route.get("/download/{filename}")
def download(bgtask: BackgroundTasks, filename: str):
    drive = deta.Drive("photos")
    file = drive.get(f"{filename}.png")
    with open(os.path.join(PUBLIC_DIR, f"{filename}.png"), "wb") as f:
        f.write(file.read())
    return FileResponse(
        os.path.join(PUBLIC_DIR, f"{filename}.png"),
        media_type="application/octet-stream",
        filename="test.png",
        background=bgtask.add_task(detete_local_file, filename),
    )
