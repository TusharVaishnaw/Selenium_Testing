import pytest
from core.auth import get_authdata


@pytest.fixture(scope="session")
def authdata():
    return get_authdata()


@pytest.fixture(scope="session")
def headers(authdata):
    return {
        "Authorization": f"Bearer {authdata["tkn"]}",
        "Content-Type": "application/json"
    }
