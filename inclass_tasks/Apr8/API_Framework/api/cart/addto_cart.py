from core.base_api import BaseAPI
from utils.config import BASE_URL


class CartAPI:

    def __init__(self):
        self.api = BaseAPI(BASE_URL)

    def cart(self, payload, shopper_id, headers):
        return self.api.post(f"/shoppers/{shopper_id}/carts", headers=headers, json=payload)

    def cartg(self, shopper_id, headers):
        return self.api.get(f"/shoppers/{shopper_id}/carts", headers=headers)

# class WishlistAPI:

# GET Wishlist
# def get_wishlist(self, shopper_id, headers):
#     return self.api.get(
#         f"/shoppers/{shopper_id}/wishlist",
#         headers=headers
#     )

# POST Add to Wishlist
# def add_to_wishlist(self, shopper_id, headers, product_id, quantity):
#     payload = {
#         "productId": product_id,
#         "quantity": quantity
#     }
#
#     return self.api.post(
#         f"/shoppers/{shopper_id}/wishlist",
#         headers=headers,
#         json=payload
#     )
