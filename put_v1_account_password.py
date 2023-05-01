import requests


def put_v1_account_password():
    """
    Change registered user password
    :return:
    """
    url = "http://localhost:5051/v1/account/password"

    payload = {
      "login": "login775",
      "token": "8b5b40eb-cc9d-4cee-92dd-021ac70ab337",
      "oldPassword": "login775",
      "newPassword": "login775"
    }
    headers = {
      'X-Dm-Auth-Token': '',
      'X-Dm-Bb-Render-Mode': '',
      'Content-Type': 'application/json',
      'Accept': 'text/plain'
    }

    response = requests.request(
        method="PUT",
        url=url,
        headers=headers,
        json=payload
    )
    return response
