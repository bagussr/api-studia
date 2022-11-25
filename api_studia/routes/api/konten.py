from api_studia.modules import Session, APIRouter, Depends, HTTPException, UploadFile, File, os, pathlib
from api_studia.service.db_service import get_db
from api_studia.routes.controller.konten import get_all_konten, create_konten, delete_konten
from api_studia.routes.controller.media import create_media
from api_studia.schemas.konten import CreateKontenSchema
from api_studia.schemas.media import CreateMediaSchema

import aiofiles

x = pathlib.Path("public/asset/image").absolute()

konten_route = APIRouter(prefix="/konten", tags=["konten"])


@konten_route.get("/")
def get_all_konten_route(db: Session = Depends(get_db)):
    konten = get_all_konten(db)
    return {"message": "success", "data": konten}


@konten_route.post("/")
async def create_new_konten_route(
    kontens: CreateKontenSchema, file: UploadFile = File(), db: Session = Depends(get_db)
):
    async with aiofiles.open(os.path.join(x, file.filename), "wb") as f:
        content = await file.read()
        await f.write(content)
    media = await create_media(
        db,
        CreateMediaSchema(
            name=file.filename,
            url=f"/asset/image/{file.filename}",
            base_url=os.path.join(x, ""),
            size=len(content),
        ),
    )
    konten = await create_konten(db, kontens, media.id)
    return {"message": "success", "data": konten}


@konten_route.delete("/{konten_id}")
def delete_konten_route(konten_id: int, db: Session = Depends(get_db)):
    konten = delete_konten(db, konten_id)
    if konten:
        return {"message": "success"}
    raise HTTPException(status_code=404, detail="Konten not found")
