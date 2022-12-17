from api_studia.modules import Session, APIRouter, Depends, HTTPException, AuthJWT, Optional
from api_studia.service.db_service import get_db
from api_studia.routes.controller.kelas import (
    get_kelas,
    get_all_kelas,
    create_kelas,
    update_kelas,
    join_kelas,
    joined_kelas,
    get_kelas_owner,
    leave_kelas,
    delete_casecade,
)
from api_studia.routes.controller.media import get_media_by_name, get_media_by_id
from api_studia.routes.controller.users import get_user_id
from api_studia.schemas.kelas import KelasCreate, KelasBase, JoinKelas
from api_studia.service.auth import get_authorize, teacher_authorize, admin_authorize

import random

kelas_route = APIRouter(prefix="/kelas", tags=["kelas"])


@kelas_route.post("/", dependencies=[Depends(get_authorize), Depends(teacher_authorize)])
async def create_kelas_route(kelas: KelasCreate, db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    image = f"bg-{random.randrange(1, 7)}.jpg"
    media = get_media_by_name(db, image)
    if media is None:
        raise HTTPException(status_code=404, detail="Media Not Found")
    current_user = Authorize.get_jwt_subject()
    data = await create_kelas(db, kelas, current_user, media.id)
    await join_kelas(db, current_user, data.code)
    return {
        "message": "success",
    }


# except Exception as e:
# raise HTTPException(status_code=500, detail=str(e))


@kelas_route.get("/", dependencies=[Depends(get_authorize), Depends(admin_authorize)])
def read_all_kelas(skip: int = 0, db: Session = Depends(get_db)):
    all_kelas = get_all_kelas(db, skip=skip)
    if all_kelas:
        return {"data": all_kelas}
    raise HTTPException(status_code=404, detail="Kelas Not Found")


@kelas_route.get("/current_owner", dependencies=[Depends(get_authorize), Depends(teacher_authorize)])
def joined(db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    current = Authorize.get_jwt_subject()
    db_kelas = get_kelas_owner(db, current)
    if db_kelas:
        return {"msg": db_kelas}
    raise HTTPException(status_code=404, detail="Kelas Not Found")


@kelas_route.get("/{kelas_id}", dependencies=[Depends(get_authorize)])
def read_kelas(kelas_id: str, db: Session = Depends(get_db)):
    db_kelas = get_kelas(db, kelas_id=kelas_id)
    if db_kelas is None:
        raise HTTPException(status_code=404, detail="Kelas Not Found")
    return {"data": db_kelas}


@kelas_route.delete("/{kelas_id}", dependencies=[Depends(get_authorize), Depends(teacher_authorize)])
def delete_kelas_route(kelas_id: str, db: Session = Depends(get_db)):
    if delete_casecade(db, kelas_id):
        return {"message": "success"}
    raise HTTPException(status_code=404, detail="Kelas Not Found")


@kelas_route.put("/{kelas_id}", dependencies=[Depends(get_authorize), Depends(teacher_authorize)])
async def edit_kelas_route(kelas_id: str, kelas: KelasBase, db: Session = Depends(get_db)):
    kelas_db = await update_kelas(db, kelas_id=kelas_id, kelas=kelas)
    if kelas_db:
        return {"message": "success", "data": kelas_db}
    raise HTTPException(status_code=404, detail="Kelas Not Found")


@kelas_route.post("/join", dependencies=[Depends(get_authorize)])
async def join_kelas_route(payload: JoinKelas, db: Session = Depends(get_db)):
    kelas_db = await join_kelas(db, code=payload.code, user_id=payload.user_id)
    if kelas_db:
        return {"message": "success"}
    raise HTTPException(status_code=404, detail="Kelas Not Found")


@kelas_route.get("/joined/current", dependencies=[Depends(get_authorize)])
def joinend_kelas_route(populate: Optional[str] = None, db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    user_id = Authorize.get_jwt_subject()
    kelas_db = joined_kelas(db, user_id=user_id)
    if kelas_db:
        for kelas in kelas_db:
            if populate == "*":
                kelas.owner = get_user_id(db, kelas.created_by)
                kelas.image = get_media_by_id(db, kelas.image_id)
            elif populate == "owner":
                kelas.owner = get_user_id(db, kelas.owner)
            elif populate == "image":
                kelas.image = get_media_by_id(db, kelas.image_id)
        return {"message": "success", "data": kelas_db}
    raise HTTPException(status_code=404, detail="User Not Joined Any Class")


@kelas_route.delete("/leave/{kelas_id}", dependencies=[Depends(get_authorize)])
def leave_kelas_rout(kelas_id: str, db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    kelas = leave_kelas(db, kelas_id=kelas_id, user_id=Authorize.get_jwt_subject())
    return {"message": "success", "data": kelas}
