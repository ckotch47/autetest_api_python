from pydantic import BaseModel


class AuthRefreshDto(BaseModel):
    refresh_token: str
