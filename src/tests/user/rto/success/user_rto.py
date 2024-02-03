from pydantic import BaseModel
from .avatar_rto import AvatarRto


class UserRto(BaseModel):
    id: str
    username: str
    mail: str
    avatar_id: str
    avatar: AvatarRto | None = None
