import requests

payload = {
    "id": 12,
    "category": {
        "id": 12,
        "name": "string"
    },
    "name": "cobra",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 12,
            "name": "string"
        }
    ],
    "status": "available"
}


def test_pst():
    response = requests.post('https://petstore.swagger.io/v2/pet', json=payload)
    return response.json()['id']


id = test_pst()


def test_get():
    response = requests.get(f'https://petstore.swagger.io/v2/pet/{id}')
    print(response.status_code)


def test_dell():
    response = requests.delete(f'https://petstore.swagger.io/v2/pet/{id}')
    print(response.status_code)


print(id)

# get()
# dell()
#
