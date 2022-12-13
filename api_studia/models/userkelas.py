from .modules import Base, Column, ForeignKey, UUID

class UserKelas(Base):
    __tablename__ = "userkelas"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True)
    kelas_id = Column(UUID(as_uuid=True), ForeignKey("kelas.id"), primary_key=True)
