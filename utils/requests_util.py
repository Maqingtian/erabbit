import requests
import json

def send_request(session, method, url, **kwargs):
    """
    发送 HTTP 请求的通用函数。
    :param session: requests.Session 对象，用于发送请求。
    :param method: 请求方法，如 'GET', 'POST' 等。
    :param url: 请求的 URL。
    :param kwargs: 其他关键字参数，如 headers, json, params 等。
    :return: requests.Response 对象。
    """
    try:
        response = session.request(method, url, **kwargs)
        response.raise_for_status()  # 如果响应状态码不是 200，将抛出异常
        return response
    except requests.exceptions.HTTPError as http_err:
        # 处理 HTTP 错误
        try:
            error_data = response.json()
            error_message = error_data.get('message', '') or error_data.get('msg', '')
            status_code = error_data.get('code', '')
            print(f"HTTP error occurred: {http_err}, Status Code: {status_code}, Message: {error_message}")
        except json.JSONDecodeError:
            error_message = str(http_err)
            print(f"HTTP error occurred: {http_err}")
        raise
    except requests.exceptions.ConnectionError as conn_err:
        # 处理连接错误
        print(f"Connection error occurred: {conn_err}")
        raise
    except requests.exceptions.Timeout as timeout_err:
        # 处理请求超时
        print(f"Timeout error occurred: {timeout_err}")
        raise
    except requests.exceptions.RequestException as req_err:
        # 处理请求异常
        print(f"An error occurred: {req_err}")
        raise