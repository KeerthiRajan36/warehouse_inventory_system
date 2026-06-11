from sqlalchemy.orm import Session
from app.models.supplier import Supplier


class SupplierService:


    @staticmethod
    def create(
        db,
        data
    ):

        supplier=Supplier(
            **data.dict()
        )

        db.add(
            supplier
        )

        db.commit()

        db.refresh(
            supplier
        )

        return supplier


    @staticmethod
    def get_all(
        db:Session
    ):

        return db.query(
            Supplier
        ).all()