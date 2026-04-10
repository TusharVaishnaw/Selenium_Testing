from api.cart.addto_cart import CartAPI
from utils.read_data import read_json


def test_add_to_cart(auth_data, headers):
    cart_api = CartAPI()
    shopper_id = auth_data["shopper_id"]
    payload = read_json("test_data/cart_data.json")

    response = cart_api.cart(payload, shopper_id=shopper_id,
                             headers=headers
                             )
    assert response.status_code in [201, 200, 409]

    print(response.json())


def test_get_cart(auth_data, headers):
    cart_api = CartAPI()
    shopper_id = auth_data["shopper_id"]
    response = cart_api.cartg(shopper_id=shopper_id,
                             headers=headers
                             )
    assert response.status_code in [201, 200, 409]

    print(response.json())
# def test_add_to_wishlist(auth_data, headers):
#     wishlist_api = WishlistAPI()
#
#     shopper_id = auth_data["shopper_id"]
#
#     response = wishlist_api.add_to_wishlist(
#         shopper_id=shopper_id,
#         headers=headers,
#         product_id=52,
#         quantity=1
#     )
#
#     print(response.json())
#
#     assert response.status_code in [200, 201,409], f"Failed: {response.text}"

#
# def test_get_wishlist(auth_data, headers):
#     wishlist_api = WishlistAPI()
#
#     shopper_id = auth_data["shopper_id"]
#
#     response = wishlist_api.get_wishlist(shopper_id, headers)
#
#     print(response.json())
#
#     assert response.status_code == 200
