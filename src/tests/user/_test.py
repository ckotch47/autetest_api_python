from .services import *
from ..auth import *
from .rto import *
from .dto import *

user: AuthDto = AuthDto(**{
    'mail': os.getenv('USER_MAIL'),
    'password': os.getenv('USER_PASSWORD')
})


class Test:
    userService: UserService = UserService()
    new_username = 'new_username'
    search_user_mail = 'test@test.ts'
    auth_service = AuthService()

    def test__init__(self):
        res = self.auth_service.post_auth(user)
        temp_user = SuccessPostAuth(**res.json())
        self.userService.set_token(temp_user.access_token)

    def test_get_user(self):
        res = self.userService.get_user()
        assert res.status_code == 200
        assert UserRto(**res.json())
        self.userService.set_username(UserRto(**res.json()).username)

    def test_update_user(self):
        res = self.userService.update_username(UpdateUserRto(**{'username': self.new_username}))
        temp = UserRto(**res.json())

        assert res.status_code == 200
        assert temp.username == self.new_username

        res = self.userService.update_username(UpdateUserRto(**{'username': self.userService.username}))
        temp = UserRto(**res.json())

        assert res.status_code == 200
        assert temp.username == self.userService.username

    def test_user_search_by_mail(self):
        res = self.userService.search_by_mail(SearchByMailDto(**{'mail': self.search_user_mail}))
        assert res.status_code == 200


user_test = Test()
