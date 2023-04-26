import requests

url = "http://localhost:5051/v1/account"

payload={}
headers = {
  'X-Dm-Auth-Token': 'IQJh+zgzF5AIx7OM+FBXIAR1BVkfK0ngviStstLuLYWLLfhLpqFA18ANo6mEicqyfElwD6lc/MSZ5XijHjphbEWKNL9POYEkU0xsBZN5/0eESWpsLtLx+UZiwmyo76qpDYRDz5tYohw=',
  'X-Dm-Bb-Render-Mode': '',
  'Accept': 'text/plain'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
