from fastapi import *

from app.schemas.supplier import SupplierCreate
from app.services.supplier_service import *

from app.database.connection import *

from app.utils.dependencies import *


router=APIRouter(

    prefix="/suppliers",

    tags=[
        "Suppliers"
    ]
)


@router.post("")
def create(

    data:SupplierCreate,

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
        SupplierService
        .create(
            db,
            data
        )
    )


@router.get("")
def all(

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
        SupplierService
        .get_all(
            db
        )
    )