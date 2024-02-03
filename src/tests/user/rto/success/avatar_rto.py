from pydantic import BaseModel


class AvatarRto(BaseModel):
    id: str
    filepath: str
