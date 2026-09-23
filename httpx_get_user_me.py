import httpx

login_payload = {
    "email": "kir@example.com",
    "password": "123"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)

login_response_json = login_response.json()

access_token = login_response_json["token"]["accessToken"]

get_user_me_headers = {"Authorization": f"Bearer {access_token}"}

get_user_me_response = httpx.get(
    "http://localhost:8000/api/v1/users/me",
    headers=get_user_me_headers
)

print(f'Status code: {get_user_me_response.status_code}')
print(get_user_me_response.json())