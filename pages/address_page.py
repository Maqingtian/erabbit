# pages/address_page.py
from utils.requests_util import send_request

class AddressPage:
    def __init__(self, session):
        self.session = session
        self.address_url = "https://apipc-xiaotuxian-front.itheima.net/member/address"

    def add_address(self, data):
        response = send_request(self.session, "POST", self.address_url, json=data)
        return response.json()