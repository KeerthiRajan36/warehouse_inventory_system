from fastapi import *

from app.schemas.stock import StockInward, StockOutward
from app.services.stock_service import *

from app.database.connection import *

from app.utils.dependencies import *


router=APIRouter(

    prefix="/stock",

    tags=[
        "Stock"
    ]
)


@router.post(
    "/inward"
)
def inward(

    data:StockInward,

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
        StockService
        .inward(
            db,
            user,
            data
        )
    )


@router.post(
    "/outward"
)
def outward(

    data:StockOutward,

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
        StockService
        .outward(
            db,
            user,
            data
        )
    )


@router.get(
    "/history"
)
def history(

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
        StockService
        .history(
            db
        )
    )