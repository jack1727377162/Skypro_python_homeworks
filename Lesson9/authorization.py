import requests


class MyAuthorization:
    def __init__(self, my_url):
        self.my_url = my_url

    def auth_user(self, user="raphael", password="cool-but-crude"):
        user_info = {"username": user, "password": password}
        result_auth = requests.post(
            self.my_url + "/auth/login", json=user_info
            )
        return result_auth.json()["userToken"]
