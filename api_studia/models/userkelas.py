from .modules import Base, Integer, String, Column, DateTime, json, ForeignKey, relationship, UUID, datetime
from sqlalchemy.ext.associationproxy import association_proxy


class UserKelas(Base):
    __tablename__ = "userkelas"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True)
    kelas_id = Column(UUID(as_uuid=True), ForeignKey("kelas.id"), primary_key=True)
