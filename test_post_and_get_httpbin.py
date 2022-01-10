import pytest
import ipaddress
import requests
from httpbin_fixtures import origin_user_agent, ip_addresses, payloads_list


@pytest.mark.parametrize("ip_test", ip_addresses)
def test_origin_ip(ip_test):
    user_ip = ipaddress.ip_address(ip_test)
    assert user_ip.version == 4


def test_user_agent(origin_user_agent):
    assert origin_user_agent == "python-requests/2.26.0"


@pytest.mark.parametrize("payload_", payloads_list)
def test_response_form(payload_, origin_user_agent):
    url = "https://httpbin.org/post"

    req = requests.post(url, data=payload_)
    response = req.json()
    expected_result = payload_

    assert req.status_code == 200
    assert response["form"] == expected_result
    assert response["headers"]["User-Agent"] == origin_user_agent


@pytest.mark.parametrize("payload_", payloads_list)
def test_response_args(payload_, origin_user_agent):
    url = "https://httpbin.org/get"

    req = requests.get(url, params=payload_)
    response = req.json()
    expected_result = payload_

    assert req.status_code == 200
    assert response["args"] == expected_result
    assert response["headers"]["User-Agent"] == origin_user_agent
