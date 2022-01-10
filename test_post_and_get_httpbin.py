import pytest
import ipaddress
import requests
from httpbin_fixtures import origin_ip, origin_user_agent, origin_ip_without_fixutre, ip_addresses, payloads_list


@pytest.mark.parametrize("ip_test", ip_addresses)
def test_origin_ip(ip_test):
    user_ip = ipaddress.ip_address(ip_test)
    assert user_ip.version == 4


def test_user_agent(origin_user_agent):
    assert origin_user_agent == "python-requests/2.26.0"


@pytest.mark.parametrize("payload_", payloads_list)
def test_response_form(payload_, origin_user_agent):
    url = "https://httpbin.org/post"

    r = requests.post(url, data=payload_)
    response = r.json()
    expected_result = payload_

    assert r.status_code == 200
    assert response["form"] == expected_result
    assert response["headers"]["User-Agent"] == origin_user_agent


@pytest.mark.parametrize("payload_", payloads_list)
def test_response_args(payload_, origin_user_agent):
    url = "https://httpbin.org/get"

    r = requests.get(url, params=payload_)
    response = r.json()
    expected_result = payload_

    assert r.status_code == 200
    assert response["args"] == expected_result
    assert response["headers"]["User-Agent"] == origin_user_agent
