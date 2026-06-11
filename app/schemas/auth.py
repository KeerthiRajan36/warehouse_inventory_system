from pydantic import (
    BaseModel,
    EmailStr,
    Field
)

from typing import Literal


class RegisterRequest(BaseModel):

    username:str

    email:EmailStr

    password:str=Field(
        min_length=6
    )

    role:Literal[
        "ADMIN",
        "STAFF"
    ]="STAFF"



class LoginRequest(BaseModel):

    email:EmailStr

    password:str



class TokenResponse(BaseModel):

    access_token:str

    token_type:str



class UserResponse(BaseModel):

    id:int

    name:str

    email:str

    role:str

    class Config:

        from_attributes=True