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

    rel_kelas_tugas = relationship("Kelas", back_populates="rel_tugas_kelas")


class MediaPhoto(Base):
    __tablename__ = "media_photo"

    id = Column(Integer, primary_key=True, index=True)
    konten_id = Column(String(10), ForeignKey("konten.id"))
    name = Column(String(50))
    url = Column(String(255))
    base_url = Column(String(255))
    size = Column(String(255))

    rel_konten_media = relationship(
        "Konten", back_populates="rel_media_konten")


class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, index=True)
    konten_id = Column(String(10))
    user_id = Column(Integer)
    release_date = Column(String)
    text = Column(Text)

    rel_konten_comment = relationship(
        "Konten", back_populates="rel_comment_konten")


class Konten(Base):
    __tablename__ = "konten"

    id = Column(String(10), primary_key=True, index=True)
    kelas_id = Column(String(10), ForeignKey("kelas.id"))
    photo_id = Column(String(10), ForeignKey("kelas.id"))
    name = Column(String(255))
    release_date = Column(String)
    synopsis = Column(Text)

    rel_kelas_konten = relationship("Kelas", back_populates="rel_konten_kelas")
    rel_media_konten = relationship(
        "MediaPhoto", back_populates="rel_konten_media")
    rel_comment_konten = relationship(
        "Comment", back_populates="rel_konten_comment")


class Kelas(Base):
    __tablename__ = "kelas"

    id = Column(String(10), primary_key=True, index=True)
    name = Column(String(100))
    section = Column(String(100))
    code = Column(String(100))

    rel_tugas_kelas = relationship("Tugas", back_populates="rel_kelas_tugas")
    rel_konten_kelas = relationship(
        "Konten", back_populates="rel_kelas_konten")
