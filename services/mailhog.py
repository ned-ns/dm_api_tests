import json
from requests import session, Response
from restclient.restclient import Restclient


class MailHogApi:
    def __init__(self, host="http://localhost:5025", headers=None):
        self.host = host
        self.client = Restclient(host=host)

    def get_api_v2_messages(self, limit=50) -> Response:
        """
        Get messages by limit
        :param limit:
        :return:
        """
        response = self.client.get(
            path=f"/api/v2/messages",
            params={
                'limit': limit
            }
        )

        return response

    def get_token_from_last_email(self) -> str:
        emails = self.get_api_v2_messages(limit=1).json()
        token_url = json.loads(emails['items'][0]['Content']['Body'])['ConfirmationLinkUrl']
        token = token_url.split('/')[-1]
        return token
