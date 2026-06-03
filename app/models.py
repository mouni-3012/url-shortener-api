from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime


class Base(DeclarativeBase):
    pass

class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    short_code = Column(String, unique=True, index=True)
    original_url = Column(String)
    clicks = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)