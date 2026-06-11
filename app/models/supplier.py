from sqlalchemy import Column,Integer,String,DateTime
from datetime import datetime

from app.database.connection import Base

class Supplier(Base):
    __tablename__="suppliers"

    id = Column(Integer,primary_key=True,index=True)

    supplier_name = Column(String(150),nullable=False)
    email = Column(String(150),unique=True,nullable=False)
    phone = Column(String(15),nullable=False)

    created_at=Column(
        DateTime,
        default=datetime.utcnow
    )