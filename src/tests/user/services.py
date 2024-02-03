import os
import requests as req

from .dto import *


class UserService:
    access_token: str
    username: str
    url: str = os.getenv('BASE_URL')
    header = {}

    def get_user(self) -> req.Response:
        res = req.get(self.url + '/api/v1/user', headers=self.header)
        return res

    def update_username(self, body: UpdateUserRto) -> req.Response:
        res = req.patch(self.url + '/api/v1/user', headers=self.header, data=body.model_dump_json())
        return res

    def search_by_mail(self, body: SearchByMailDto) -> req.Response:
        res = req.get(self.url + f'/api/v1/user/search/by-mail?mail="{body.mail}"', headers=self.header)
        return res

    def set_token(self, token: str):
        self.access_token = token
        self.header = {
            'Authorization': f'Bearer {token}'
        }

    def set_username(self, username: str):
        self.username = username
