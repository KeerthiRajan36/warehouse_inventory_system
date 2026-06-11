from fastapi import (
    Depends,
    HTTPException
)

from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials
)

from jose import jwt

from sqlalchemy.orm import Session

from app.database.connection import (
    get_db
)

from app.models.user import User


SECRET_KEY="warehouse"

ALGORITHM="HS256"

security=HTTPBearer()


def get_current_user(

    credentials:
    HTTPAuthorizationCredentials
    =
    Depends(
        security
    ),

    db:Session=
    Depends(
        get_db
    )

):

    try:

        token=(
            credentials
            .credentials
        )

        payload=jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[
                ALGORITHM
            ]
        )

        user=(
            db.query(
                User
            )
            .filter(
                User.id
                ==
                payload["id"]
            )
            .first()
        )

        if not user:

            raise Exception()

        return user

    except:

        raise HTTPException(
            401,
            "Invalid Token"
        )


def admin_only(

    user=Depends(
        get_current_user
    )

):

    if user.role!="ADMIN":

        raise HTTPException(
            403,
            "Admin Access Only"
        )

    return user