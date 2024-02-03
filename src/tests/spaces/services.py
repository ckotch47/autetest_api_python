from .dto import *
from src import BaseService


class Services(BaseService):
    space_id: str

    def get_space(self):
        return self.get(url='/api/v1/space')

    def create_space(self, body: CreateSpaceDto):
        return self.post(url='/api/v1/space', body=body.model_dump_json())

    def delete_space(self):
        return self.delete(url=f'/api/v1/space/{self.space_id}')

    def get_space_by_id(self):
        return self.get(url=f'/api/v1/space/{self.space_id}')

    def set_space_id(self, space_id: str):
        self.space_id = space_id
