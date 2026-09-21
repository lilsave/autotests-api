import httpx


def test_server_is_up():
    # Проверка окружения: учебный сервер должен быть запущен (run_server.bat)
    response = httpx.get("http://localhost:8000/docs")
    assert response.status_code == 200
