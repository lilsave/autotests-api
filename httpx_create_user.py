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
