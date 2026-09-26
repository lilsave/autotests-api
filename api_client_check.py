import httpx

from clients.users.public_users_client import PublicUsersClient
from tools.fakers import get_random_email

from clients.authentication.authentication_client import AuthenticationClient

client = httpx.Client(
    base_url="http://localhost:8000"
)

create_user_payload = {
    "email": get_random_email(),
    "password": "123",
    "lastName": "newclient",
    "firstName": "real",
    "middleName": "bobson"
}

public_users_client = PublicUsersClient(client=client)
create_user_response = public_users_client.create_user_api(create_user_payload)
print(create_user_response.status_code)
print(create_user_response.json())

