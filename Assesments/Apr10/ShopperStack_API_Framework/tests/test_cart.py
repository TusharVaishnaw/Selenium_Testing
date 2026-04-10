from api_pages.cart.cart_api import CartAPI
from utils.read_data import read_json


api = CartAPI()

def test_addtocart(headers,authdata):
    payload = read_json('test_data/items.json')
    response = api.cart_add(user_id=authdata["userId"], headers=headers, payload=payload["item1"])
    assert response.status_code in [200,201,409]


def test_getcart(headers,authdata):

    response = api.cart_items(user_id=authdata['userId'] ,headers=headers)
    res = response.json()
    global itemID
    itemID=res["data"][0]["itemId"]
    assert response.status_code in [200, 201]


def test_putcart(authdata, headers):
    payload = read_json('test_data/patch_items.json')
    response = api.cart_update(user_id=authdata['userId'] ,headers=headers, itemid=itemID, payload=payload["item1"])
    assert response.status_code in [200,201]


def test_delcart(authdata,headers):
    prodID = read_json('test_data/items.json')["item1"]["productId"]
    # prodID = data
    response = api.cart_delete(user_id=authdata['userId'] , headers=headers, productid=prodID)
    assert response.status_code in [200, 201]
