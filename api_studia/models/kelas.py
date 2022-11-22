from .modules import Base, Integer, String, Column, DateTime, json, ForeignKey, relationship, UUID, datetime
from .userkelas import UserKelas
import uuid
import random, string


def randomword(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


class Kelas(Base):
    __tablename__ = "kelas"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    section = Column(String(100), nullable=False)
    code = Column(String(10), default=randomword(10), unique=True)
    created_by = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    update_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    tugas = relationship("Tugas", back_populates="kelas")
    owner_id = relationship("Users", back_populates="kelas", secondary=UserKelas.__table__)

    def __repr__(self):
        return json.dumps(
            {
                "id": self.id,
                "name": self.name,
                "section": self.section,
                "code": self.code,
            }
        )
