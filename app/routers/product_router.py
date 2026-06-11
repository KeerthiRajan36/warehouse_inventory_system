from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database.connection import (
    get_db
)

from app.utils.dependencies import (

    get_current_user,

    admin_only
)

from app.schemas.product import *

from app.services.product_service import (
    ProductService
)


router=APIRouter(

    prefix="/products",

    tags=[
        "Products"
    ]
)


@router.post(
    ""
)
def create(

    data:ProductCreate,

    db=
    Depends(
        get_db
    ),

    user=
    Depends(
        admin_only
    )

):

    return (
        ProductService
        .create(
            db,
            data
        )
    )


@router.get(
    ""
)
def get_all(

    db=
    Depends(
        get_db
    ),

    user=
    Depends(
        get_current_user
    )

):

    return (
        ProductService
        .get_all(
            db
        )
    )


@router.get(
    "/{id}"
)
def get_by_id(

    id:int,

    db=
    Depends(
        get_db
    ),

    user=
    Depends(
        get_current_user
    )

):

    return (
        ProductService
        .get_by_id(
            db,
            id
        )
    )


@router.delete(
    "/{id}"
)
def delete(

    id:int,

    db=
    Depends(
        get_db
    ),

    user=
    Depends(
        admin_only
    )

):

    return (
        ProductService
        .delete(
            db,
            id
        )
    )