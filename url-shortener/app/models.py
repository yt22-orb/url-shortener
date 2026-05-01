from sqlalchemy import Column, Integer, String
from .db import Base

class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    original = Column(String, nullable=False)
