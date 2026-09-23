import httpx

from tools.fakers import get_random_email

create_user_payload = {
    "email": get_random_email(),
    "password": "123",
    "lastName": "крутой",
    "firstName": "аккаунт",
    "middleName": "диджей"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
print(create_user_response.status_code)
print(create_user_response.json())

create_user_response_data = create_user_response.json()

login_user_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}

login_user_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_user_payload)
print(login_user_response.status_code)
print(login_user_response.json())

login_user_response_data = login_user_response.json()

get_user_headers = {"Authorization": f"Bearer {login_user_response_data["token"]["accessToken"]}"}

get_user_response = httpx.get(f"http://localhost:8000/api/v1/users/{create_user_response_data["user"]["id"]}",
                              headers=get_user_headers)
print(get_user_response.status_code)
print(get_user_response.json())

print('КОНЕЦ ПРОГРАММЫ')



