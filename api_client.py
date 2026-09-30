import requests

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, path, **kwargs):
        return self.session.get(self.base_url + path, timeout=10, **kwargs)

    def login(self, user):
        r= self.session.post(self.base_url + "/post", json={"user": user})
        token = r.json()["json"]["user"]
        self.session.headers["Authorization"] = f"Bearer {token}"
        return token
