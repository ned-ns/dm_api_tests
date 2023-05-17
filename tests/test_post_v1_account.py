from services.dm_api_account import DmApiAccount
from services.mailhog import MailHogApi
import structlog
from dm_api_account.models.registration_model import Registration

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    mailhog = MailHogApi(host="http://localhost:5025")
    api = DmApiAccount(host="http://localhost:5051")
    json = Registration(
         login="login753",
         email="login753@mail.ru",
         password="login753"
    )
    response = api.account.post_v1_account(json=json)
    # token = mailhog.get_token_from_last_email()
    # response = api.account.put_v1_account_token(token=token)
