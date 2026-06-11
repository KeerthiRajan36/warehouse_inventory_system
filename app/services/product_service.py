from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.product import Product


class ProductService:


    @staticmethod
    def create(
        db,
        data
    ):

        sku=db.query(
            Product
        ).filter(
            Product.sku==data.sku
        ).first()

        if sku:

            raise HTTPException(
                400,
                "SKU already exists"
            )

        product=Product(
            **data.dict()
        )

        db.add(
            product
        )

        db.commit()

        db.refresh(
            product
        )

        return product


    @staticmethod
    def get_all(
        db:Session
    ):

        return db.query(
            Product
        ).all()


    @staticmethod
    def get_by_id(
        db,
        id
    ):

        product=db.query(
            Product
        ).filter(
            Product.id==id
        ).first()

        if not product:

            raise HTTPException(
                404,
                "Product Not Found"
            )

        return product


    @staticmethod
    def delete(
        db,
        id
    ):

        product=(
            ProductService
            .get_by_id(
                db,
                id
            )
        )

        db.delete(
            product
        )

        db.commit()

        return {

            "message":"Deleted"
        }