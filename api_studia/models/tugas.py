from .modules import Base, String, Column, json, ForeignKey, relationship, DateTime, Text, datetime, UUID
import random, string


def randomword(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


class Tugas(Base):
    __tablename__ = "tugas"

    id = Column(String(15), primary_key=True, index=True, default=randomword(15))
    kelas_id = Column(UUID(as_uuid=True), ForeignKey("kelas.id"))
    name = Column(String(100))
    description = Column(Text)
    deadline = Column(DateTime)
    created_at = Column(DateTime, default=datetime.datetime.now)
    update_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    kelas = relationship("Kelas", back_populates="tugas")

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
