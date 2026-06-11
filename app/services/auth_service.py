from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.user import User

from app.schemas.auth import (
    RegisterRequest,
    LoginRequest
)

from app.utils.hash import (
    hash_password,
    verify_password
)

from app.utils.jwt import (
    create_token
)


class AuthService:


    @staticmethod
    def register(
        db:Session,
        data:RegisterRequest
    ):

        user=db.query(
            User
        ).filter(
            User.email==data.email
        ).first()

        if user:

            raise HTTPException(
                400,
                "Email already exists"
            )

        new_user=User(

            name=data.name,

            email=data.email,

            password=hash_password(
                data.password
            ),

            role=data.role
        )

        db.add(
            new_user
        )

        db.commit()

        db.refresh(
            new_user
        )

        return new_user


    @staticmethod
    def login(
        db:Session,
        data:LoginRequest
    ):

        user=db.query(
            User
        ).filter(
            User.email==data.email
        ).first()

        if not user:

            raise HTTPException(
                401,
                "Invalid Credentials"
            )

        if not verify_password(
            data.password,
            user.password
        ):

            raise HTTPException(
                401,
                "Invalid Credentials"
            )

        token=create_token({

            "id":user.id,

            "role":user.role
        })

        return {

            "access_token":token,

            "token_type":"Bearer"
        }