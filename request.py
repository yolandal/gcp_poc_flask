import requests

payload = {
    "message": "This is a test message."
}

# headers = {'user-agent': 'customize header string', 'Content-Type': 'application/json; charset=utf-8'}
response = requests.post("http://0.0.0.0:8000/msg", json=payload)

print(response.status_code)
print(response.text)
# print(response.headers)
