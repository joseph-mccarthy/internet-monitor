from sqlalchemy import Column, Integer, Float, DateTime
from database import Base

class Result(Base):
    __tablename__ = "results"
    id = Column(Integer, primary_key=True)
    download = Column(Float(), unique=False, nullable=False)
    upload = Column(Float(), unique=False, nullable=False)
    ping = Column(Float(), unique=False, nullable=False)
    timestamp = Column(DateTime(), unique=False, nullable=False)
