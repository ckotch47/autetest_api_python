from pydantic import BaseModel


class UpdateUserRto(BaseModel):
    username: str | None = None
    avatarId: str | None = None
