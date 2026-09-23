import httpx
from tools.fakers import get_random_email

create_user_payload = {
    "email": get_random_email(),
    "password": "25m",
    "lastName": "lake",
    "firstName": "adison",
    "middleName": "middle"
}

create_user_response = httpx.post("http://127.0.0.1:8000/api/v1/users", json=create_user_payload)

create_user_response_data = create_user_response.json()

login_user_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}

login_user_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_user_payload)
login_user_response_data = login_user_response.json()
print(login_user_response.status_code)
print(login_user_response.json())

authorization_headers = {"Authorization": f"Bearer {login_user_response_data["token"]["accessToken"]}"}

patch_user_payload = {
    "email": get_random_email(),
    "lastName": "река",
    "firstName": "мэдисон",
    "middleName": "центральный"
}
patch_user_response = httpx.patch(f"http://127.0.0.1:8000/api/v1/users/{create_user_response_data["user"]["id"]}",
                                  json=patch_user_payload, headers=authorization_headers)
print(patch_user_response.status_code)
print(patch_user_response.json())
