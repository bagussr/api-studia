from .modules import Base, Integer, String, Column, Boolean, json, ForeignKey, relationship, UUID, DateTime, datetime
from .userkelas import UserKelas
import uuid


class Users(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    photo_id = Column(Integer, ForeignKey("media.id"))
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    address = Column(String(250))
    gender = Column(Boolean, default=False)
    isAdmin = Column(Boolean, default=False)
    isStudent = Column(Boolean, default=False)
    isTeacher = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    media = relationship("Media", back_populates="users")
    kelas = relationship("Kelas", back_populates="owner_id", secondary=UserKelas.__table__)
    rel_konten_userkonten = relationship("Konten", back_populates="rel_user")
    rel_comment_user = relationship("Comment", back_populates="user_rel")

    def __repr__(self):
        return json.dumps(
            {
                "id": self.id,
                "photo_id": self.photo_id,
                "username": self.username,
                "email": self.email,
                "password": self.password,
                "name": self.name,
                "address": self.address,
                "gender": self.gender,
                "isAdmin": self.isAdmin,
                "isStudent": self.isStudent,
                "isTeacher": self.isTeacher,
            }
        )
