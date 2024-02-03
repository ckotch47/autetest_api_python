import os

from .services import AuthService
from .dto import AuthDto
from .rto import SuccessPostAuth


class Test:
    authService = AuthService()

    user: AuthDto = AuthDto(**{
        'mail': os.getenv('USER_MAIL'),
        'password': os.getenv('USER_PASSWORD')
    })

    def test_get_auth_token(self):
        res = self.authService.post_auth(self.user)
        assert res.status_code == 200
        assert SuccessPostAuth(**res.json())
        self.authService.save_token(SuccessPostAuth(**res.json()))

    def test_refresh_token(self):
        res = self.authService.post_auth_refresh()
        assert res.status_code == 200
        assert SuccessPostAuth(**res.json())
        self.authService.save_token(SuccessPostAuth(**res.json()))


auth_test = Test()
