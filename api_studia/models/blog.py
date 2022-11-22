from .modules import Base, Integer, String, Column, DateTime, json, ForeignKey, relationship, datetime, Text, UUID


class Konten(Base):
    __tablename__ = "konten"

    id = Column(Integer, primary_key=True, index=True)
    kelas_id = Column(UUID(as_uuid=True)), ForeignKey("kelas.id")
    photo_id = Column(Integer, ForeignKey("media.id"))
    name = Column(String(255))
    release_date = Column(String)
    text = Column(Text)
    synopsis = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    rel_kelas_konten = relationship("Kelas", back_populates="rel_konten_kelas")
    rel_media_konten = relationship("MediaPhoto", back_populates="rel_konten_media")
    rel_comment_konten = relationship("Comment", back_populates="rel_konten_comment")

    def __repr__(self):
        return json.dumps(
            {
                "id": self.id,
                "kelas_id": self.kelas_id,
                "photo_id": self.photo_id,
                "name": self.name,
                "release_date": self.release_date,
                "text": self.text,
                "synopsis": self.synopsis,
                "created_at": self.created_at,
                "updated_at": self.updated_at,
            }
        )
