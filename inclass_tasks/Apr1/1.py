import requests
# response = requests.get('https://petstore.swagger.io/v2/store/inventory')

# response = requests.get('https://petstore.swagger.io/v2/pet/findByStatus?=status=sold')
response = requests.get('https://petstore.swagger.io/v2/pet/17')

# print(response.text)
# print(response.status_code)
print(response.json()['id'])
# actual=response.status_code
# expected=200
# assert actual == expected, f"status not success, it is: {actual}"


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
# response = requests.post('https://petstore.swagger.io/v2/pet', json=payload)

# response = requests.delete('https://petstore.swagger.io/v2/pet/12')

# print(response.json())
