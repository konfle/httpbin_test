import requests
import pytest

ip_addresses = ["10.32.3",
                "192.168.0.1.2",
                "192.168.10.256",
                "10.58.15.-1"]


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


def origin_ip_without_fixutre():
    url = "https://httpbin.org/ip"

    response = requests.request("GET", url)
    ip = response.json()

    return ip["origin"]


user_ip = origin_ip_without_fixutre()
ip_addresses.insert(0, user_ip)
