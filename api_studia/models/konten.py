from .modules import Base, Integer, String, Column, DateTime, json, ForeignKey, relationship, datetime, Text, UUID


class Konten(Base):
    __tablename__ = "konten"

    id = Column(Integer, primary_key=True, index=True)
    photo_id = Column(Integer, ForeignKey("media.id"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    name = Column(String(255))
    text = Column(Text)
    synopsis = Column(Text)
    release_date = Column(String, nullable=False, default=datetime.datetime.now)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    rel_media_konten = relationship("Media", back_populates="rel_konten_media")
    rel_user = relationship("Users", back_populates="rel_konten_userkonten")
    rel_comment_konten = relationship("Comment", back_populates="konten_rel")

    def __repr__(self):
        return json.dumps(
            {
                "id": self.id,
                "name": self.name,
                "release_date": self.release_date,
                "text": self.text,
                "synopsis": self.synopsis,
                "photo_id": self.photo_id,
                "owned_by": self.owned_by,
                "created_at": self.created_at,
                "updated_at": self.updated_at,
            }
        )
