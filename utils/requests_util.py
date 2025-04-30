# utils/requests_util.py
import requests

def send_request(session, method, url, **kwargs):
    """
    发送 HTTP 请求的通用函数。
    :param session: requests.Session 对象，用于发送请求。
    :param method: 请求方法，如 'GET', 'POST' 等。
    :param url: 请求的 URL。
    :param kwargs: 其他关键字参数，如 headers, json, params 等。
    :return: requests.Response 对象。
    """
    response = session.request(method, url, **kwargs)
    response.raise_for_status()  # 如果响应状态码不是 200，将抛出异常
    return response