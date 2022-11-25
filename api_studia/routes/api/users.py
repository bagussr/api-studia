from api_studia.modules import (
    APIRouter,
    Depends,
    HTTPException,
    status,
    Session,
    UploadFile,
    File,
    os,
    pathlib,
)
from api_studia.schemas.users import CreateUserSchema
from api_studia.schemas.media import CreateMediaSchema
from api_studia.models.users import Users
from api_studia.routes.controller.media import create_media
from api_studia.service.db_service import get_db

import aiofiles

x = pathlib.Path("public/asset/image").absolute()

user_route = APIRouter(prefix="/users", tags=["users"])


@user_route.post("/")
async def create_user(user: CreateUserSchema, file: UploadFile = File(), db: Session = Depends(get_db)):
    async with aiofiles.open(os.path.join(x, file.filename), "wb") as f:
        content = await file.read()
        await f.write(content)
    media = await create_media(
        db,
        CreateMediaSchema(
            name=file.filename, url=f"/asset/image/{file.filename}", base_url=os.path.join(x, ""), size=len(content)
        ),
    )
    user = Users(**user.dict(), photo_id=media.id)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@user_route.get("/")
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(Users).all()
    return users
