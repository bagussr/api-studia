from api_studia.modules import APIRouter, Depends, HTTPException, status, Session, BaseModel
from api_studia.models.users import Users
from api_studia.service.db_service import get_db

user_route = APIRouter(prefix="/users", tags=["users"])


class UserSchema(BaseModel):
    username: str
    email: str
    password: str
    name: str
    address: str
    gender: int
    isTeacher: bool


@user_route.post("/")
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    user = Users(**user.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
