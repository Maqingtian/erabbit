# pages/order_page.py
from utils.requests_util import send_request

class OrderPage:
    def __init__(self, session):
        self.session = session
        self.Pre_order_url = "https://apipc-xiaotuxian-front.itheima.net/member/order/pre"
        self.order_url = "https://apipc-xiaotuxian-front.itheima.net/member/order"
    def submit_order(self, data):
        response_pre = send_request(self.session, "GET", self.Pre_order_url)
        response = send_request(self.session, "POST", self.order_url, json=data)
        return response.json()