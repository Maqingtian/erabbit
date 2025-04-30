# tests/test_order.py
import pytest
from pages.order_page import OrderPage

class TestOrder:
    @pytest.mark.order(5)
    def test_submit_order(self, session):
        order_page = OrderPage(session)
        # 从全局变量中获取地址 ID
        address_id = session.address_id
        data = {
            "deliveryTimeType": 1,
            "payType": 1,
            "payChannel": 1,
            "buyerMessage": "",
            "goods": [
                {
                    "skuId": "3678050",
                    "count": 23
                }
            ],
            "addressId": address_id
        }
        response = order_page.submit_order(data)
        print(address_id)
        print(response)
        assert response["code"] == "1"

if __name__ == "__main__":
    pytest.main(["-v", "-s", "tests/test_order.py"])