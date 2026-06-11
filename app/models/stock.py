from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)

from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.connection import Base


class StockHistory(Base):

    __tablename__="stock_history"

    id=Column(
        Integer,
        primary_key=True,
        index=True
    )

    product_id=Column(
        Integer,
        ForeignKey(
            "products.id"
        )
    )

    created_by=Column(
        Integer,
        ForeignKey(
            "users.id"
        )
    )

    movement_type=Column(
        String(20)
    )

    quantity=Column(
        Integer
    )

    created_at=Column(
        DateTime,
        default=datetime.utcnow
    )

    product=relationship(
        "Product",
        back_populates="stock_history"
    )

    created_user=relationship(
        "User",
        back_populates="stock_history"
    )