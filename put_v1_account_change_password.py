import requests
import json

url = "http://localhost:5051/v1/account/password"

payload = json.dumps({
  "login": "login775",
  "token": "8b5b40eb-cc9d-4cee-92dd-021ac70ab337",
  "oldPassword": "login775",
  "newPassword": "login775"
})
headers = {
  'X-Dm-Auth-Token': '',
  'X-Dm-Bb-Render-Mode': '',
  'Content-Type': 'application/json',
  'Accept': 'text/plain'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
