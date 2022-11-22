from .modules import Base, Integer, String, Column, DateTime, json, ForeignKey, relationship, UUID, datetime
import uuid
import random, string


def randomword(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


class Kelas(Base):
    __tablename__ = "kelas"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    name = Column(String(100), nullable=False)
    section = Column(String(100), nullable=False)
    code = Column(String(10), default=randomword(10), unique=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    update_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    tugas = relationship("Tugas", back_populates="kelas")
    userkelas = relationship("UserKelas", back_populates="kelas")
    owner_id = relationship("Users", back_populates="kelas")
    rel_konten_kelas = relationship("Konten", back_populates="rel_kelas_konten")

    def __repr__(self):
        return json.dumps(
            {
                "id": self.id,
                "name": self.name,
                "section": self.section,
                "code": self.code,
            }
        )


class Userkelas(Base):
    __tablename__ = "userkelas"

    id = Column(Integer, primary_key=True, index=True)
    users_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    kelas_id = Column(UUID(as_uuid=True), ForeignKey("kelas.id"))
    joint_at = Column(DateTime, default=datetime.datetime.utcnow)

    kelas = relationship("Kelas", back_populates="userkelas")
    user = relationship("Users", back_populates="userkelas")

    def __repr__(self):
        return json.dumps(
            {"id": self.id, "users_id": self.users_id, "kelas_id": self.kelas_id, "joint_at": self.joint_at}
        )
