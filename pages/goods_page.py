# pages/goods_page.py
from utils.requests_util import send_request

class GoodsPage:
    def __init__(self, session):
        self.session = session
        self.goods_url = "https://apipc-xiaotuxian-front.itheima.net/goods"

    def get_goods(self, goods_id):
        params = {"id": goods_id}
        response = send_request(self.session, "GET", self.goods_url, params=params)
        return response.json()