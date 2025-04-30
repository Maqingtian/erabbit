# conftest.py
import pytest
import requests
import json

@pytest.fixture(scope="session")
def session():
    session = requests.Session()
    # 定义全局变量
    session.address_id = None
    
    login_url = "https://apipc-xiaotuxian-front.itheima.net/login"
    credentials = {"account": "demo", "password": "456ITheima@.20250430"}

    try:
        response = session.post(login_url, json=credentials)
        response.raise_for_status()  # 确保登录成功
        # 登录成功后，从响应的 JSON 中提取 token
        login_response_data = response.json()
        token = login_response_data.get("result", {}).get("token")
        if token:
            # 设置 Authorization 头部用于后续请求
            session.headers.update({'Authorization': f'Bearer {token}'})
        else:
            pytest.fail("Login failed: token not found in response")
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Login failed: {e}")

    yield session
    session.close()