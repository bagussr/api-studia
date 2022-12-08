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
    AuthJWT,
    io,
)
from api_studia.schemas.users import CreateUserSchema, LoginSchema, UserSchema
from api_studia.schemas.media import CreateMediaSchema
from api_studia.models.users import Users
from api_studia.routes.controller.users import create_user, get_user_username, get_user_id, delete_user, update_user
from api_studia.routes.controller.media import create_media
from api_studia.service.db_service import get_db
from api_studia.service.auth import get_authorize, teacher_authorize, admin_authorize

import aiofiles

from fastapi.security import HTTPBearer


x = pathlib.Path("public/asset/image").absolute()

user_route = APIRouter(prefix="/users", tags=["users"])


@user_route.get("/", dependencies=[Depends(get_authorize), Depends(admin_authorize)])
def get_all_users(db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    users = db.query(Users).all()
    return users


@user_route.get("/current", dependencies=[Depends(get_authorize)])
def get_current_user(Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()
    db_user = get_user_id(db, current_user)
    return {"message": "success", "data": db_user}


@user_route.post("/register")
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
    db_user = await create_user(db, user, media.id)
    return {"message": "User Created", "data": db_user}


@user_route.post("/login")
def login_route(user: LoginSchema, db: Session = Depends(get_db), auth: AuthJWT = Depends()):
    db_user = get_user_username(db, user.username)
    if user.password == db_user.password:
        auth_token = auth.create_access_token(
            subject=str(db_user.id),
            expires_time=24 * 60 * 60,
            user_claims={
                "is_admin": db_user.isAdmin,
                "is_teacher": db_user.isTeacher,
                "is_student": db_user.isStudent,
            },
        )
        return {"message": "Login Success", "access_token": auth_token}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Username or Password")


@user_route.delete("/delete/{id}", dependencies=[Depends(get_authorize)])
def delele_user_route(id: str, db: Session = Depends(get_db)):
    db_user = delete_user(db, id)
    return {"message": "User Deleted", "data": db_user}


@user_route.put("/update/{id}", dependencies=[Depends(get_authorize)])
def update_user_route(id: str, db: Session = Depends(get_db)):
    db_user = update_user(db, id)
    return {"message": "User Updated", "data": db_user}
