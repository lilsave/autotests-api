import httpx

login_payload = {
    "email": "kir@example.com",
    "password": "123"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)

login_response_json = login_response.json()


refresh_token = login_response_json["token"]["refreshToken"]

refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json={"refreshToken": refresh_token})

print("Status Code:", refresh_response.status_code)
print(refresh_response.json())