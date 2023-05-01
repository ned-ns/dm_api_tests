import requests
from services.dm_api_account import DmApiAccount


def test_put_v1_account_change_email():
    api = DmApiAccount(host="http://localhost:5051")
    json = {
            "login": "login775",
            "email": "login675@mail.ru",
            "password": "login775"
        }
    response = api.account.put_v1_account_change_email(
        json=json
    )
    print(response)
