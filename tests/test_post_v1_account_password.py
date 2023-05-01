import requests
from services.dm_api_account import DmApiAccount


def test_post_v1_account_password():
    api = DmApiAccount(host="http://localhost:5051")
    json = {
        "login": "login775",
        "email": "login675@mail.ru"
    }
    response = api.account.post_v1_account_password(
        json=json
    )
    print(response)
