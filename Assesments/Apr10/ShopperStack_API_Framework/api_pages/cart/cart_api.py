from core.base_api import BaseAPI
from utils.config import BASE_URL


class CartAPI:

    def __init__(self):
        self.api = BaseAPI(BASE_URL)

    def cart_add(self, user_id, headers, payload):
        return self.api.post(f"/shoppers/{user_id}/carts", headers=headers, json=payload)

    def cart_items(self, user_id, headers):
        return self.api.get(f"/shoppers/{user_id}/carts", headers=headers)

    def cart_update(self, user_id, itemid, headers, payload):
        return self.api.put(f"/shoppers/{user_id}/carts/{itemid}", headers=headers, json=payload)

    def cart_delete(self, user_id, productid, headers):
        return self.api.delete(f"/shoppers/{user_id}/carts/{productid}", headers=headers)
