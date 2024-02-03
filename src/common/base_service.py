import os
import requests as req
from pydantic import BaseModel


class AuthDto(BaseModel):
    mail: str
    password: str


class BaseService:
    url: str = os.getenv('BASE_URL')
    header: dict = {}

    role = {
        'OWNER': {
            'mail': os.getenv('USER_MAIL'),
            'password': os.getenv('USER_PASSWORD')
        }
    }

    def set_token(self, token: str):
        self.header = {
            'Authorization': f'Bearer {token}'
        }

    def get(self, **args):
        return req.get(f"{self.url}{args.get('url')}", headers=self.header, params=args.get('params'))

    def post(self, **args):
        return req.post(f"{self.url}{args.get('url')}", headers=self.header, data=args.get('body'))

    def put(self, **args):
        return req.put(f"{self.url}{args.get('url')}", headers=self.header, data=args.get('body'))

    def patch(self, **args):
        return req.patch(f"{self.url}{args.get('url')}", headers=self.header, data=args.get('body'))

    def delete(self, **args):
        return req.delete(f"{self.url}{args.get('url')}", headers=self.header, params=args.get('params'))

    def auth_role(self, role: str):
        res = req.post(self.url + '/api/v1/auth',
                       data=AuthDto(**self.role[role]).model_dump_json())
        self.set_token(res.json()['access_token'])

