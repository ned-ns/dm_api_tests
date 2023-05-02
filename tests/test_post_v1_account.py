from services.dm_api_account import DmApiAccount
from services.mailhog import MailHogApi


def test_post_v1_account():
    mailhog = MailHogApi(host="http://localhost:5052")
    api = DmApiAccount(host="http://localhost:5051")
    json = {
        "login": "login768",
        "email": "login768@mail.ru",
        "password": "login768"
    }
    response = api.account.post_v1_account(json=json)
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)
    print(response)
    print(response.json())
