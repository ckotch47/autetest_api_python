from pydantic import BaseModel


class SearchByMailDto(BaseModel):
    mail: str
