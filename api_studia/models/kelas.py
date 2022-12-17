from .modules import Base, Integer, String, Column, DateTime, json, ForeignKey, relationship, UUID, datetime
from .userkelas import UserKelas
import uuid


class Kelas(Base):
    __tablename__ = "kelas"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    image_id = Column(Integer, ForeignKey("media.id"))
    name = Column(String(100), nullable=False)
    section = Column(String(100), nullable=False)
    code = Column(String(10), unique=True)
    created_by = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.datetime.now)
    update_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    owner_id = relationship("Users", back_populates="kelas", secondary=UserKelas.__table__)
    rel_media_kelas = relationship("Media", back_populates="rel_kelas_media")
    lessons = relationship("Lesson", back_populates="rel_kelas_lessons")

    def __repr__(self):
        return json.dumps(
            {
                "id": self.id,
                "name": self.name,
                "section": self.section,
                "code": self.code,
                "created_by": self.created_by,
                "created_at": self.created_at,
                "update_at": self.update_at,
            }
        )
