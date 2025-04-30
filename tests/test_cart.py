# tests/test_cart.py
import pytest
from pages.cart_page import CartPage

class TestCart:
    @pytest.mark.order(3)
    def test_add_to_cart(self, session):
        cart_page = CartPage(session)
        response = cart_page.add_to_cart("3678050", 23)
        assert response["code"] == "1"
        print ("添加购物车成功")


if __name__ == "__main__":
    pytest.main(["-v", "-s", "tests/test_cart.py"])