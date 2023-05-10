import requests
from services.dm_api_account import DmApiAccount
import structlog


structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_get_v1_account():
    api = DmApiAccount(host="http://localhost:5051")
    response = api.account.get_v1_account()
    assert response.status_code == 200, f'Статус код ответ должен быть равен 200, но он равен {response.status_code}'
