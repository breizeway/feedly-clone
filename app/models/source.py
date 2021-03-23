from .db import db
from app.models import feeds_sources
from sqlalchemy.orm import relationship


class Source(db.Model):
    __tablename__ = 'sources'

    id = db.Column(db.Integer, primary_key=True)
    source_url = db.Column(db.String(500), nullable=False)
    alt_name = db.Column(db.String(100))

    feeds = relationship("Feed",
                         secondary=feeds_sources,
                         back_populates="sources")

    def to_dict(self):
        return {"id": self.id,
                "source_url": self.source_url,
                "alt_name": self.alt_name}
