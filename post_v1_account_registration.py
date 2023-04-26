import requests
import json

url = "http://localhost:5051/v1/account"

payload = json.dumps({
  "login": "login775",
  "email": "login775@mail.ru",
  "password": "login775"
})
headers = {
  'X-Dm-Auth-Token': '',
  'X-Dm-Bb-Render-Mode': '',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
