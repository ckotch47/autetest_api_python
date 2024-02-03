from .services import *
from .dto import *
from .rto import *
from ..auth import AuthService


class Test:
    name_space: str = "test name space"
    auth_service = AuthService()
    service = Services()

    def test_init(self):
        self.service.auth_role('OWNER')

    def test_get_space(self):
        res = self.service.get_space()
        assert res.status_code == 200
        assert SpaceRto(**res.json()[0])

    def test_create_space(self):
        res = self.service.create_space(CreateSpaceDto(**{'name': self.name_space}))
        assert res.status_code == 200
        assert SpaceRto(**res.json())
        temp = SpaceRto(**res.json())
        self.service.set_space_id(temp.id)
        self.space_id = temp.id

    def test_get_space_by_id(self):
        res = self.service.get_space_by_id()
        assert res.status_code == 200
        assert SpaceRto(**res.json())

    def test_delete_space(self):
        res = self.service.delete_space()
        assert res.status_code == 200

        res = self.service.get_space_by_id()
        assert res.status_code == 404
