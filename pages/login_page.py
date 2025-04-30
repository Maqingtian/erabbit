# pages/login_page.py
from utils.requests_util import send_request

class LoginPage:
    def __init__(self, session):
        self.session = session
        self.login_url = "https://apipc-xiaotuxian-front.itheima.net/login"

    def login(self, account, password):
        data = {"account": account, "password": password}
        response = send_request(self.session, "POST", self.login_url, json=data)
        return response.json()