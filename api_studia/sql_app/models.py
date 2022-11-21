from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from api_studia.sql_app.database import Base


class User(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    photo_id = Column(Integer)
    username = Column(String(50))
    email = Column(String(250), unique=True)
    password = Column(String(250))
    name = Column(String(250))
    isAdmin = Column(Boolean)
    gender = Column(Integer)
    address = Column(String(250))
    isAdmin = Column(Boolean)
    isStudent = Column(Boolean)
    isTeacher = Column(Boolean)


class Tugas(Base):
    __tablename__ = "tugas"

    id = Column(String(15), primary_key=True, index=True)
    kelas_id = Column(String(10), ForeignKey("kelas.id"))
    name = Column(String(100))
    description = Column(Text)
    deadline = Column(String)

    rel_kelas = relationship("Kelas", back_populates="rel_tugas")


class Kelas(Base):
    __tablename__ = "kelas"

    id = Column(String(10), primary_key=True, index=True)
    name = Column(String(100))
    section = Column(String(100))
    code = Column(String(100))

    rel_tugas = relationship("Tugas", back_populates="rel_kelas")
