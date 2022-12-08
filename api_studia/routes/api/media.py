from api_studia.modules import APIRouter, Form, File, UploadFile, StreamingResponse, deta, io, Session, Depends
from api_studia.routes.controller.media import create_media
from api_studia.schemas.media import CreateMediaSchema
from api_studia.service.db_service import get_db


media_route = APIRouter(prefix="/media", tags=["media"])


@media_route.get("/photos/{filename}")
def get_photo(filename: str):
    drive = deta.Drive("photos")
    file = drive.get(f"{filename}.png")
    return StreamingResponse(file.iter_lines(), media_type="image/png")


@media_route.post("/photos")
async def add_photo(file: UploadFile = File(...), filename: str = Form(...), db: Session = Depends(get_db)):
    drive = deta.Drive("photos")
    drive.put(f"{filename}.png", io.BytesIO(file.file.read()))
    content = CreateMediaSchema(
        name=filename,
        url=f"/media/photos/{filename}",
        base_url=f"/media/photos/",
        size=len(await file.read()),
    )
    create_media(db, content)
    return {"message": "success"}


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
