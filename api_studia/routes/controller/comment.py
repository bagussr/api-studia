from api_studia.modules import Session
from api_studia.models.comment import Comment
from api_studia.models.konten import Konten
from api_studia.schemas.comment import CommentCreate, CommentBase


def get_all_comment_konten(db: Session, kelas_id: str, konten_id: str, skip: int = 0):
    return (
        db.query(Comment).filter_by(Comment.konten_id == konten_id and Konten.kelas_id == kelas_id).offset(skip).all()
    )


async def create_comment_konten(db: Session, comment: CommentCreate, konten_id: str):
    db_comment = Comment(**comment.dict(), konten_id=konten_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


async def update_comment(db: Session, comment_id: int, konten_id: str, comment: CommentBase):
    db_comment = db.query(Comment).filter_by(id=comment_id, konten_id=konten_id).first()
    if comment.text:
        db_comment.text = comment.text
    db.merge(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def delete_comment(db: Session, comment_id: int, konten_id: str, user_id: str):
    db_comment = db.query(Comment).filter_by(id=comment_id, konten_id=konten_id, user_id=user_id).first()
    db.delete(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment
