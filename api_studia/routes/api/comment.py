from api_studia.modules import APIRouter, Depends, HTTPException, Session
from api_studia.service.db_service import get_db
from api_studia.schemas.comment import CommentCreate, CommentBase
from api_studia.routes.controller.comment import (
    get_all_comment_konten,
    create_comment_konten,
    update_comment,
    delete_comment,
)
from api_studia.routes.controller.konten import get_konten_kelas
from api_studia.service.auth import get_authorize

comment_route = APIRouter(prefix="/comment", tags=["comment"], dependencies=[Depends(get_authorize)])


@comment_route.post("/{konten_id}/k/{kelas_id}")
async def create_comment_konten(konten_id: str, kelas_id: str, comment: CommentCreate, db: Session = Depends(get_db)):
    db_konten = get_konten_kelas(db, kelas_id=kelas_id, konten_id=konten_id)
    if db_konten is None:
        raise HTTPException(status_code=404, detail="Konten Not Found")
    return await create_comment_konten(db=db, comment=comment, konten_id=konten_id)


@comment_route.get("/{konten_id}/k/{kelas_id}")
def read_all_comment_konten(konten_id: str, kelas_id: str, skip: int = 0, db: Session = Depends(get_db)):
    db_konten = get_konten_kelas(db, kelas_id=kelas_id, konten_id=konten_id)
    if db_konten is None:
        raise HTTPException(status_code=404, detail="Konten Not Found")
    read_all_comment_konten = get_all_comment_konten(db, skip=skip, kelas_id=kelas_id)
    return read_all_comment_konten


@comment_route.put("/{comment_id}/k/{konten_id}")
async def comment_edit(comment_id: int, konten_id: str, comment: CommentBase, db: Session = Depends(get_db)):
    db_comment = await update_comment(db, comment_id=comment_id, konten_id=konten_id, comment=comment)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment Not Found")
    return db_comment


@comment_route.delete("/{comment_id}/k/{konten_id}/u/{user_id}")
def comment_delete(comment_id: int, konten_id: str, user_id: str, db: Session = Depends(get_db)):
    db_comment = delete_comment(db, comment_id=comment_id, konten_id=konten_id, user_id=user_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment Not Found")
    return db_comment
