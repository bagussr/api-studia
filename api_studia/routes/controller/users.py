from api_studia.modules import Session
from api_studia.models.users import Users
from api_studia.schemas.users import CreateUserSchema, UserSchema


async def create_user_new(db: Session, user: CreateUserSchema, media_id: int):
    db_user = Users(**user.dict(), photo_id=media_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_username(db: Session, username: str):
    return db.query(Users).filter_by(username=username).first()


def get_user_id(db: Session, id: str):
    return db.query(Users).filter_by(id=id).first()


def delete_user(db: Session, id: str):
    db_data = db.query(Users).filter_by(id=id).first()
    return db_data


async def update_user(db: Session, id: str, user: UserSchema):
    db_user = db.query(Users).filter_by(id=id).first()
    if user.name:
        db_user.name = user.name
    if user.address:
        db_user.address = user.address
    if user.gender:
        db_user.gender = user.gender
    db.merge(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


async def edit_photo(db: Session, id: str, photo: int):
    db_user = db.query(Users).filter_by(id=id).first()
    db_user.photo_id = photo
    db.merge(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
