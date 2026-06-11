from sqlalchemy import Column,Integer,String,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.connection import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100))
    email = Column(String(150), unique=True)
    password = Column(String(100))
    role = Column(String(50), default="STAFF")
    created_at = Column(DateTime, default=datetime.utcnow)
    
    stock_history=relationship(
            "StockHistory",
            back_populates="created_user"
        )