import requests

url = "http://localhost:5051/v1/account/8607fe61-674d-4f31-8f10-e70cdc7667ab"

payload={}
headers = {
  'X-Dm-Auth-Token': '',
  'X-Dm-Bb-Render-Mode': '',
  'Accept': 'text/plain'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
