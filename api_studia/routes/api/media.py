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
    HTTPException,
    status,
    AuthJWT,
    Response,
)
from api_studia.routes.controller.users import edit_photo
from api_studia.routes.controller.media import create_media, update_size
from api_studia.schemas.media import CreateMediaSchema
from api_studia.service.db_service import get_db
from api_studia.service.auth import get_authorize

from api_studia.service.utils import resize_image

media_route = APIRouter(prefix="/media", tags=["media"])


# @media_route.post("/photos/seeds")
# async def seed_media(db: Session = Depends(get_db)):
#     drive = deta.Drive("photos")
#     list_folder = os.listdir(os.path.join(PUBLIC_DIR, "asset/image/profile"))
#     for x in list_folder:
#         for file in os.listdir(os.path.join(PUBLIC_DIR, "asset/image/profile", x)):
#             with open(os.path.join(PUBLIC_DIR, f"asset/image/profile/{x}", file.split(".")[0] + ".png"), "rb") as f:
#                 drive.put(file, io.BytesIO(f.read()))
#                 content = CreateMediaSchema(
#                     name=file.split(".")[0] + ".png",
#                     url="/media/photos/" + file.split(".")[0],
#                     base_url="/media/photos",
#                     size=len(io.BytesIO(f.read()).read()),
#                     type=file.split(".")[1],
#                 )

#             await create_media(db, content)

#     return {"success": "Succes"}


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
        image = resize_image(file.file)
        drive.put(f"{filename}.png", image.getvalue())
        content = CreateMediaSchema(
            name=filename,
            url=f"https://studia.deta.dev//media/photos/{filename}",
            base_url=f"https://studia.deta.dev//media/photos/",
            size=len(image.getvalue()),
            type=file.content_type,
        )
        media = await create_media(db, content)
        await edit_photo(db, Authorize.get_jwt_subject(), media.id)
        return {"message": "success"}
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail={"error": str(e)})


# @media_route.post("/backgrounds/seeds")
# async def background_seeds(db: Session = Depends(get_db)):
#     try:
#         drive = deta.Drive("backgrounds")
#         for file in os.listdir(os.path.join(PUBLIC_DIR, "asset/image/background")):
#             with open(os.path.join(PUBLIC_DIR, f"asset/image/background", file), "rb") as f:
#                 image = resize_image(f)
#                 drive.put(file, image.getvalue())
#                 content = CreateMediaSchema(
#                     name=file.split(".")[0] + ".png",
#                     url="/media/backgrounds/" + file.split(".")[0],
#                     base_url="/media/backgrounds",
#                     size=len(image.getvalue()),
#                     type=file.split(".")[1],
#                 )
#             await update_size(
#                 db,
#                 content.size,
#                 file.split(".")[0] + ".png"
#             )
#     except Exception as e:
#         raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail={"error": str(e)}) from e
#     return {"message": "success"}


@media_route.get("/backgrounds")
def get_all():
    drive = deta.Drive("backgrounds")
    return {"message": "success", "list": drive.list()["names"]}


@media_route.post("/backgrounds")
async def add_background(background: UploadFile = File(...), filename: str = Form(...), db: Session = Depends(get_db)):
    # try:
    drive = deta.Drive("backgrounds")
    image = resize_image(background.file)
    drive.put(f"{filename}.jpg", image.getvalue())
    content = CreateMediaSchema(
        name=filename,
        url=f"https://studia.deta.dev//media/backgrounds/{filename}",
        base_url=f"https://studia.deta.dev//media/backgrounds/",
        size=len(image.getvalue()),
        type=background.content_type,
    )
    await create_media(db, content)
    return {"message": "success"}
    # except:
    # raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail={"error": "Internal Server Error"})


@media_route.get("/backgrounds/{filename}")
def get_photo(filename: str):
    drive = deta.Drive("backgrounds")
    file = drive.get(f"{filename}.jpg")
    if file:
        return StreamingResponse(file.iter_lines(), media_type="image/jpeg")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"error": "Not Found"})


@media_route.get("photos/download/{filename}")
def download(filename: str):
    drive = deta.Drive("tugas")
    file = drive.get(f"{filename}.pdf")
    return Response(
        file.read(),
        media_type="application/octet-stream",
        headers={"Content-Disposition": f"attachment;filename={filename}.png"},
    )
