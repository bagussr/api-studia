from api_studia.service.db_service import Base
from .modules import Column, Integer, String, ForeignKey, relationship, datetime, DateTime, json, UUID, Text


class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    deskripsi = Column(String, nullable=False)
    detail = Column(Text, nullable=False)
    kelas_id = Column(UUID, ForeignKey("kelas.id"))
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    rel_kelas_lessons = relationship("Kelas", back_populates="lessons")
    rel_tugas_lesson = relationship("Tugas", back_populates="lesson_rel")

    def __repr__(self) -> str:
        return json.dumps(
            {
                "id": self.id,
                "name": self.name,
                "kelas_id": self.kelas_id,
                "created_at": str(self.created_at),
                "updated_at": str(self.updated_at),
            }
        )
