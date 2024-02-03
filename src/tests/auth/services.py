import os
import requests as req
from requests import Response

from ..auth.dto import AuthDto, AuthRefreshDto
from ..auth.rto import SuccessPostAuth


class AuthService:
    access_token: str
    refresh_token: str
    url: str = os.getenv('BASE_URL')

    def post_auth(self, body: AuthDto) -> Response:
        res = req.post(self.url + '/api/v1/auth',
                       data=body.model_dump_json())
        return res

    def save_token(self, body: SuccessPostAuth):
        self.access_token = body.access_token
        self.refresh_token = body.refresh_token
        os.environ["ACCESS_TOKEN"] = body.access_token
        os.environ["REFRESH_TOKEN"] = body.refresh_token
        return

    def post_auth_refresh(self) -> Response:
        body = AuthRefreshDto(**{'refresh_token': self.refresh_token})
        res = req.post(self.url + '/api/v1/auth/refresh',
                       data=body.model_dump_json())
        return res

    def auth_def_user(self) -> SuccessPostAuth:
        user = AuthDto(**{
            'mail': os.getenv('USER_MAIL'),
            'password': os.getenv('USER_PASSWORD')
        })
        return SuccessPostAuth(**self.post_auth(user).json())