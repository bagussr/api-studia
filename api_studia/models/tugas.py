from .modules import Base, String, Column, json, ForeignKey, relationship, DateTime, Text, datetime, UUID, Integer


class Tugas(Base):
    __tablename__ = "tugas"

    id = Column(String(15), primary_key=True, index=True)
    lesson_id = Column(Integer, ForeignKey("lessons.id"))
    name = Column(String(100))
    description = Column(Text)
    deadline = Column(DateTime)
    created_at = Column(DateTime, default=datetime.datetime.now)
    update_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    lesson_rel = relationship("Lesson", back_populates="rel_tugas_lesson")

    def __repr__(self):
        return json.dumps(
            {
                "id": self.id,
                "kelas_id": self.kelas_id,
                "name": self.name,
                "description": self.description,
                "deadline": self.deadline,
            }
        )
