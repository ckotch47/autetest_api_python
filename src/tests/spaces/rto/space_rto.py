from pydantic import BaseModel


class SpaceRto(BaseModel):
    id: str
    name: str
    role: str | None = None
    sort: int
    short_name: str | None = None
