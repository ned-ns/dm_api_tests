import requests
from services.dm_api_account import DmApiAccount
import structlog
from dm_api_account.models.change_password_model import ChangePasswordModel

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_password():
    api = DmApiAccount(host="http://localhost:5051")
    json = ChangePasswordModel(
        login="login756",
        token='8ce2900e-6e2f-4623-947c-a6547a381135',
        oldPassword="login756",
        newPassword="login756"
    )
    response = api.account.put_v1_account_password(json=json)
    assert response.status_code == 200, f'Статус код ответ должен быть равен 200, но он равен {response.status_code}'
