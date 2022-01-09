import requests
import pytest


@pytest.fixture
def origin_ip():
    url = "https://httpbin.org/ip"

    response = requests.request("GET", url)
    ip = response.json()

    return ip["origin"]


@pytest.fixture
def origin_user_agent():
    url = "https://httpbin.org/user-agent"

    response = requests.request("GET", url)
    user_agent = response.json()

    return user_agent["user-agent"]
