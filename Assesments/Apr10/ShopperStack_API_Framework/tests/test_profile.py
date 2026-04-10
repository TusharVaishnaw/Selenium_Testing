from utils.read_data import read_json
from api_pages.profile.profile_api import ProfileAPI

profile_api = ProfileAPI()


def test_register():
    payload = read_json('test_data/register_data.json')

    response = profile_api.register(payload)
    data = response.json()
    assert data["statusCode"] in [200, 201, 409]


def test_login():
    payload = read_json('test_data/login_data.json')

    response = profile_api.login(payload)
    data = response.json()
    assert data["statusCode"] in [200, 201]


def test_get_userdata(authdata, headers):
    # uid = authdata["userId"]
    # print('here comeeeeesssssssssssssss the daaaaataaaaaaaaaaaaaaa')
    # print(authdata["userId"],'\n',headers)
    response = profile_api.user_info(user_id=authdata["userId"], headers=headers)
    assert response.status_code in [200, 201]


def test_patchuser(authdata, headers):
    data = read_json('test_data/patchUser.json')
    response = profile_api.update_user_info(user_id=authdata["userId"], payload= data, headers=headers)
    assert response.status_code in [200, 201]
