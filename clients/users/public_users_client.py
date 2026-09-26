from typing import TypedDict

import httpx

from clients.api_client import APIClient


class CreateUserRequestDict(TypedDict):
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """
    def create_user_api(self, request: CreateUserRequestDict) -> httpx.Response:
        """
        Метод создаёт нового пользователя.
        :param request: данные для создания аккаунта
        :return: ответ от сервера
        """
        return self.post("/api/v1/users", json=request)
