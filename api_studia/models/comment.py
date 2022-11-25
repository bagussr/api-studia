from .modules import Base, Integer, Column, DateTime, json, ForeignKey, relationship, datetime, Text, UUID
import uuid


class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    release_date = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def __repr__(self):
        return json.dumps(
            {
                "id": self.id,
                "konten_id": self.konten_id,
                "user_id": self.user_id,
                "release_date": self.release_date,
                "text": self.text,
                "updated_at": self.updated_at,
            }
        )
