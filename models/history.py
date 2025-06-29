from sqlalchemy import Column, Integer, String, DateTime, func
from app.database import Base


class History(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True, index=True)
    cep = Column(String, nullable=False)
    response_time = Column(String)
    source = Column(String)  # via cep ou brasil_api
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
