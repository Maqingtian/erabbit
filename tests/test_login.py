# tests/test_login.py
import pytest
from pages.login_page import LoginPage

class TestLogin:
    @pytest.mark.order(1)
    def test_login(self, session):
        login_page = LoginPage(session)
        response = login_page.login("demo", "456ITheima@.20250430")
        print(response)
        assert response["code"] == "1"


if __name__ == "__main__":
    pytest.main(["-v", "-s", "tests/test_login.py"])