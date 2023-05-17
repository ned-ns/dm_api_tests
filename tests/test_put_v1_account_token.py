from services.dm_api_account import DmApiAccount
from dm_api_account.models.user_envelope_model import UserRole
import structlog
from hamcrest import assert_that, has_properties

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_token():
    api = DmApiAccount(host="http://localhost:5051")
    response = api.account.put_v1_account_token(token='9b86eb2a-4880-4b46-8dbd-0e1abf8903eb', status_code=200)
    assert_that(response.resource, has_properties(
        {"login": "login753",
         "roles": [UserRole.guest, UserRole.player]
         }
    )
                )
