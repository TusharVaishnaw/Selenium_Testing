import requests

payload = {
    "city": "jaipur",
    "country": "india",
    "email": "tvw11x@gmail.com",
    "firstName": "tushar",
    "gender": "MALE",
    "lastName": "vw",
    "password": "Password0",
    "phone": 9509994140,
    "state": "Rajasthan",
    "zoneId": "ALPHA"
}


def reg_post():
    response = requests.post('https://www.shoppersstack.com/shopping/shoppers', json=payload, verify=False)
    return response.json()

reg_post()

logindata={
  "email": "tvw11@gmail.com",
  "password": "Password0",
  "role": "SHOPPER"
}


def login_post():
    response = requests.post('https://www.shoppersstack.com/shopping/users/login', json=logindata, verify=False)
    return response.json()


lres = login_post()
print(lres)
# id = res.data['userId']
data = lres['data']
idu = data['userId']
tkn = data['jwtToken']
print(tkn)


def get():
    header = {'Authorization': f"Bearer {tkn}"}
    response = requests.get(f'https://www.shoppersstack.com/shopping/shoppers/{idu}', headers=header,verify=False)
    return response.status_code


print(get())
