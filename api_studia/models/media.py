from .modules import Base, Integer, String, Column, datetime, json, DateTime, relationship


class Media(Base):
    __tablename__ = "media"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    url = Column(String(255))
    base_url = Column(String(255))
    size = Column(String(255))
    created_at = Column(DateTime, default=datetime.datetime.now)
    update_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    users = relationship("Users", back_populates="media")
    rel_konten_media = relationship("Konten", back_populates="rel_media_konten")

    def __repr__(self):
        return json.dumps(
            {"id": self.id, "name": self.name, "url": self.url, "base_url": self.base_url, "size": self.size}
        )
