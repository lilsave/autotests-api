class APIClient:
    def __init__(self, client):
        self.client = client

    def get(self, url, params=None):
        return self.client.get(url, params=params)

    def post(self, url, json=None, data=None, files=None):
        return self.client.post(url, json=json, data=data, files=files)

    def patch(self, url, json=None):
        return self.client.patch(url, json=json)

    def delete(self, url):
        return self.client.delete(url)
