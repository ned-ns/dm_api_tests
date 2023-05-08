import requests
from services.dm_api_account import DmApiAccount
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_password():
    api = DmApiAccount(host="http://localhost:5051")
    json = {
        "login": "login775",
        "token": "8b5b40eb-cc9d-4cee-92dd-021ac70ab337",
        "oldPassword": "login775",
        "newPassword": "login775"
    }
    response = api.account.put_v1_account_password(
        json=json
    )
    assert response.status_code == 200, f'Статус код ответ должен быть равен 200, но он равен {response.status_code}'
