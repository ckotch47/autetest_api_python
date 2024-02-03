from pydantic import BaseModel


class AuthDto(BaseModel):
    mail: str
    password: str
