# tests/test_goods.py
import pytest
from pages.goods_page import GoodsPage

class TestGoods:
    @pytest.mark.order(2)
    def test_get_goods(self, session):
        goods_page = GoodsPage(session)
        response = goods_page.get_goods("4005091")
        print(response)
        assert response["code"] == "1"

if __name__ == "__main__":
    pytest.main(["-v", "-s", "tests/test_goods.py"])