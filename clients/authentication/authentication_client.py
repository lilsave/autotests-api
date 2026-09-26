from clients.api_client import APIClient


class AuthenticationClient(APIClient):
    def login_api(self, request):
        return self.post("/api/v1/authentication/login", json=request)

    def refresh_api(self, request):
        return self.post("/api/v1/authentication/refresh", json=request)