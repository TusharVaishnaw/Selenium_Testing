from utils.read_data import read_json
from api_pages.profile.profile_api import ProfileAPI

api = ProfileAPI()


def get_authdata():
    cred_data = read_json('test_data/login_data.json')
    response = api.login(cred_data)
    assert response.status_code in [200, 201]
    res = response.json()
    userid = res["data"]["userId"]
    tkn = res["data"]["jwtToken"]
    return {
        "userId": userid,
        "tkn": tkn
    }
