import httpx

def create_account_json(email):
    create_user_payload = {
        "email": email,
        "password": "123",
        "lastName": "lake",
        "firstName": "adison",
        "middleName": "middle"
    }

    create_user_response = httpx.post("http://127.0.0.1:8000/api/v1/users", json=create_user_payload)

    print(create_user_response.json())

#create_account_json('test@mail.com')


# 1. Логинимся ОБЫЧНЫМ httpx, без клиента
login_payload = {"email": "test@mail.com", "password": "123"}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
print(login_response.status_code)
login_response_data = login_response.json()

# 2. Создаём клиента, сразу с токеном внутри
client = httpx.Client(
    base_url="http://localhost:8000",
    timeout=100,
    headers={"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}
)

# 3. Дальше все запросы — через клиента, заголовок уже не пишем
get_user_me_response = client.get("/api/v1/users/me")
get_user_me_json = get_user_me_response.json()
print(get_user_me_json)
get_courses = client.get('/api/v1/courses', params={"userId":get_user_me_json["user"]["id"]})
print(get_courses.json())