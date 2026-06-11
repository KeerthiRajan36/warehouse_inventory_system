from pydantic import (
    BaseModel,
    EmailStr
)

from typing import Optional


class SupplierCreate(
    BaseModel
):

    supplier_name:str

    email:EmailStr

    phone:str


class SupplierUpdate(
    BaseModel
):

    supplier_name:Optional[
        str
    ]=None

    email:Optional[
        EmailStr
    ]=None

    phone:Optional[
        str
    ]=None


class SupplierResponse(
    BaseModel
):

    id:int

    supplier_name:str

    email:str

    phone:str

    class Config:

        from_attributes=True