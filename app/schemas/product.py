from pydantic import (
    BaseModel,
    Field
)

from typing import Optional


class ProductCreate(
    BaseModel
):

    product_name:str

    sku:str

    category:str

    price:float=Field(
        gt=0
    )

    stock_quantity:int=Field(
        default=0,
        ge=0
    )


class ProductUpdate(
    BaseModel
):

    product_name:Optional[str]=None

    category:Optional[str]=None

    price:Optional[
        float
    ]=Field(
        default=None,
        gt=0
    )


class ProductResponse(
    BaseModel
):

    id:int

    product_name:str

    sku:str

    category:str

    price:float

    stock_quantity:int

    class Config:

        from_attributes=True