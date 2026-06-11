from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.supplier import Supplier


class SupplierService:


    @staticmethod
    def create(
        db:Session,
        data
    ):

        exists=(
            db.query(
                Supplier
            )
            .filter(
                Supplier.email
                ==
                data.email
            )
            .first()
        )

        if exists:

            raise HTTPException(
                400,
                "Supplier email already exists"
            )

        supplier=Supplier(
            **data.model_dump()
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

        return (
            db.query(
                Supplier
            )
            .all()
        )


    @staticmethod
    def get_by_id(
        db:Session,
        id:int
    ):

        supplier=(
            db.query(
                Supplier
            )
            .filter(
                Supplier.id
                ==
                id
            )
            .first()
        )

        if not supplier:

            raise HTTPException(
                404,
                "Supplier Not Found"
            )

        return supplier


    @staticmethod
    def update(
        db:Session,
        id:int,
        data
    ):

        supplier=(
            SupplierService
            .get_by_id(
                db,
                id
            )
        )

        values=(
            data
            .model_dump(
                exclude_unset=True
            )
        )

        for key,value in values.items():

            setattr(
                supplier,
                key,
                value
            )

        db.commit()

        db.refresh(
            supplier
        )

        return supplier


    @staticmethod
    def delete(
        db:Session,
        id:int
    ):

        supplier=(
            SupplierService
            .get_by_id(
                db,
                id
            )
        )

        db.delete(
            supplier
        )

        db.commit()

        return {

            "message":
            "Supplier Deleted"
        }