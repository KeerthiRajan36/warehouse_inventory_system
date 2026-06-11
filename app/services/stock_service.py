from fastapi import HTTPException

from app.models.product import Product

from app.models.stock import (
    StockHistory
)


class StockService:


    @staticmethod
    def inward(
        db,
        user,
        data
    ):

        product=(
            db.query(
                Product
            )
            .filter(
                Product.id
                ==
                data.product_id
            )
            .first()
        )

        if not product:

            raise HTTPException(
                404,
                "Product not found"
            )

        product.stock_quantity+=(
            data.quantity
        )

        history=StockHistory(

            product_id=data.product_id,

            quantity=data.quantity,

            movement_type="INWARD",

            created_by=user.id
        )

        db.add(
            history
        )

        db.commit()

        return {

            "message":"Stock Added"
        }


    @staticmethod
    def outward(
        db,
        user,
        data
    ):

        product=(
            db.query(
                Product
            )
            .filter(
                Product.id
                ==
                data.product_id
            )
            .first()
        )

        if not product:

            raise HTTPException(
                404,
                "Product not found"
            )

        if (
            product.stock_quantity
            <
            data.quantity
        ):

            raise HTTPException(
                400,
                "Insufficient stock"
            )

        product.stock_quantity-=(
            data.quantity
        )

        history=StockHistory(

            product_id=data.product_id,

            quantity=data.quantity,

            movement_type="OUTWARD",

            created_by=user.id
        )

        db.add(
            history
        )

        db.commit()

        return {

            "message":"Stock Removed"
        }


    @staticmethod
    def history(
        db
    ):

        return (
            db.query(
                StockHistory
            )
            .all()
        )