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
    headers = {
        'X-Dm-Auth-Token': 'IQJh+zgzF5AKs9qFsN67MZOtTuclvYlTMLZG65pwG+skEuW5bLuh6o2B3yU/Qt9U1JY2X0bRCU4whI/Is50i+bkvuPSnEXQKv9pJJ79hur4b0928XWEEAH7YpfW9J4lTpXwYBZnbgk8='
    }
    response = api.account.get_v1_account(headers=headers)
    assert response.status_code == 200, f'Статус код ответ должен быть равен 200, но он равен {response.status_code}'
