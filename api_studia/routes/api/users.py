from api_studia.modules import (
    APIRouter,
    Depends,
    HTTPException,
    status,
    Session,
    BaseModel,
    UploadFile,
    File,
    os,
    pathlib,
)
from api_studia.models.users import Users
from api_studia.models.media import Media
from api_studia.service.db_service import get_db

import json
import aiofiles

x = pathlib.Path("public/asset/image").absolute()

user_route = APIRouter(prefix="/users", tags=["users"])


class UserSchema(BaseModel):
    username: str
    email: str
    password: str
    name: str
    address: str
    gender: int


class CreateUserSchema(UserSchema):
    isTeacher: bool = False
    isStudent: bool = False

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value

    class config:
        orm_mode = True


@user_route.post("/")
async def create_user(user: CreateUserSchema, file: UploadFile = File(), db: Session = Depends(get_db)):
    async with aiofiles.open(os.path.join(x, file.filename), "wb") as f:
        content = await file.read()
        await f.write(content)
    media = Media(
        name=file.filename, url=os.path.join(x, file.filename), base_url=os.path.join(x, ""), size=len(content)
    )
    db.add(media)
    db.commit()
    user = Users(**user.dict(), photo_id=media.id)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@user_route.get("/")
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(Users).all()
    return users
