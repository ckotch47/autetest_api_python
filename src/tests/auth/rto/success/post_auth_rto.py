from pydantic import BaseModel




class SuccessPostAuth(BaseModel):
    access_token: str
    refresh_token: str
