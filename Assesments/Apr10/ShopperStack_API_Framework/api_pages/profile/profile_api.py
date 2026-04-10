from core.base_api import BaseAPI
from utils.config import BASE_URL


class ProfileAPI:

    def __init__(self):
        self.api = BaseAPI(BASE_URL)

    def register(self, payload):
        return self.api.post("/shoppers", json=payload)

    def login(self, payload):
        return self.api.post("/users/login", json=payload)

    def user_info(self, user_id, headers):
        return self.api.get(f"/shoppers/{user_id}", headers=headers)

    def update_user_info(self, user_id, payload, headers):
        return self.api.patch(f"/shoppers/{user_id}", json=payload, headers=headers)
