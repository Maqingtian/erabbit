# tests/test_address.py
import pytest
from pages.address_page import AddressPage

class TestAddress:
    @pytest.mark.order(4)
    def test_add_address(self, session):
        address_page = AddressPage(session)
        data = {
            "receiver": "马情天",
            "contact": "13800138000",
            "provinceCode": "120000",
            "cityCode": "120100",
            "countyCode": "120101",
            "address": "地方撒撒打发",
            "postalCode": "111333",
            "addressTags": "1",
            "isDefault": 1,
            "fullLocation": "天津 天津市 和平区"
        }
        response = address_page.add_address(data)
        print(response)
        # 将地址 ID 存入全局变量
        session.address_id = response.get("result", {}).get("id")
        print(session.address_id)
        assert response["code"] == "1"

if __name__ == "__main__":
    pytest.main(["-v", "-s", "tests/test_address.py"])