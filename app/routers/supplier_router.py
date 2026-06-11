from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database.connection import (
    get_db
)

from app.schemas.supplier import *

from app.services.supplier_service import (
    SupplierService
)

from app.utils.dependencies import (
    get_current_user,
    admin_only
)


router=APIRouter(

    prefix="/suppliers",

    tags=[
        "Supplier"
    ]
)


@router.post(
    "",
    response_model=
    SupplierResponse
)
def create_supplier(

    data:
    SupplierCreate,

    db:
    Session=
    Depends(
        get_db
    ),

    user=
    Depends(
        admin_only
    )

):

    return (
        SupplierService
        .create(
            db,
            data
        )
    )


@router.get(
    "",
    response_model=
    list[
        SupplierResponse
    ]
)
def get_suppliers(

    db:
    Session=
    Depends(
        get_db
    ),

    user=
    Depends(
        get_current_user
    )

):

    return (
        SupplierService
        .get_all(
            db
        )
    )


@router.put(
    "/{id}",
    response_model=
    SupplierResponse
)
def update_supplier(

    id:int,

    data:
    SupplierUpdate,

    db:
    Session=
    Depends(
        get_db
    ),

    user=
    Depends(
        admin_only
    )

):

    return (
        SupplierService
        .update(
            db,
            id,
            data
        )
    )


@router.delete(
    "/{id}"
)
def delete_supplier(

    id:int,

    db:
    Session=
    Depends(
        get_db
    ),

    user=
    Depends(
        admin_only
    )

):

    return (
        SupplierService
        .delete(
            db,
            id
        )
    )