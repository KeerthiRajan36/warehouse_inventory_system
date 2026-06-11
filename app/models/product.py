from sqlalchemy import Column,Integer,String,Float,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.connection import Base


class Product(Base):
    __tablename__="products"

    id = Column(Integer,primary_key=True,index=True)
    product_name = Column(String(100),nullable=False)
    sku = Column(String(100),nullable=False)
    category=Column(String(100),nullable=False)
    price=Column(Float,nullable=False)
    stock_quantity =Column(Integer,default=0)

    created_at=Column(
        DateTime,
        default=datetime.utcnow
    )

    stock_history=relationship(
        "StockHistory",
        back_populates="product"
    )