import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = 'https://www.shoppersstack.com/shopping'

session = requests.Session()

# ----------------LOGIN--------------------
ldata={
  "email": "tvw11@gmail.com",
  "password": "Password0",
  "role": "SHOPPER"
}

lres = session.post(f'{base_url}/users/login', json = ldata, verify = False)

print(lres.json())
# ----------store token - ---------------
tkn = lres.json()['data']['jwtToken']
uid = lres.json()['data']['userId']
session.headers.update({
    "Authorization" : f"Bearer {tkn}"
})
gres = session.get(f'{base_url}/shoppers/{uid}' ,verify = False)

print(gres.json())
