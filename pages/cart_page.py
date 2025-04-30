# pages/cart_page.py
from utils.requests_util import send_request

class CartPage:
    def __init__(self, session):
        self.session = session
        self.cart_url = "https://apipc-xiaotuxian-front.itheima.net/member/cart"

    def add_to_cart(self, sku_id, count):
        data = {"skuId": sku_id, "count": count}
        response = send_request(self.session, "POST", self.cart_url, json=data)
        return response.json()