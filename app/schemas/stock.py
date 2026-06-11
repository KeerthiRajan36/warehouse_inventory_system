from pydantic import (
    BaseModel,
    Field
)

from datetime import datetime


class StockInward(
    BaseModel
):

    product_id:int

    quantity:int=Field(
        gt=0
    )


class StockOutward(
    BaseModel
):

    product_id:int

    quantity:int=Field(
        gt=0
    )


class StockHistoryResponse(
    BaseModel
):

    id:int

    product_id:int

    created_by:int

    movement_type:str

    quantity:int

    created_at:datetime

    class Config:

        from_attributes=True