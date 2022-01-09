import pytest
import requests
from httpbin_fixtures import origin_ip, origin_user_agent

ip = origin_ip()
ip_addresses = [ip,
                "10.32.3",
                "192.168.0.1.2",
                "192.168.10.256",
                "10.58.15.-1"]


@pytest.mark.parametrize("ip_test", ip_addresses)
def test_validate_origin_ip(ip_test):
    valid = False
    qty_of_octets = ip_test.split(".")

    for octet in qty_of_octets:
        if int(octet) in range(0, 255):
            valid = True
        else:
            valid = False
            break

    if len(qty_of_octets) != 4:
        valid = False

    assert valid is True


def test_post_data(origin_ip, origin_user_agent):
    url = "https://httpbin.org/post"

    payload = {
        "accountName": "konfle",
        "characterName": "BatoN",
        "characterClass": "Sorceress",
        "serverRegion": "Europe",
        "gameMode": "Hardcore"
    }

    r = requests.post(url, data=payload)
    response = r.json()
    current_trace_id = response["headers"]["X-Amzn-Trace-Id"]

    expected_result = {
        "args": {},
        "data": "",
        "files": {},
        "form": {
            "accountName": "konfle",
            "characterClass": "Sorceress",
            "characterName": "BatoN",
            "gameMode": "Hardcore",
            "serverRegion": "Europe"
        },
        "headers": {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Content-Length": "101",
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "httpbin.org",
            "User-Agent": f"{origin_user_agent}",
            "X-Amzn-Trace-Id": f"{current_trace_id}"
        },
        "json": None,
        "origin": f"{origin_ip}",
        "url": "https://httpbin.org/post"
    }

    assert r.status_code == 200
    assert response == expected_result


def test_get_data(origin_ip, origin_user_agent):
    url = "https://httpbin.org/get"

    payload = {
        "accountName": "konfle",
        "characterName": "BatoN",
        "characterClass": "Sorceress",
        "gameMode": "Hardcore",
        "serverRegion": "Europe"
    }

    r = requests.get(url, params=payload)
    response = r.json()
    current_trace_id = response["headers"]["X-Amzn-Trace-Id"]
    body_url = r.url

    expected_result = {
        "args": {
            "accountName": "konfle",
            "characterName": "BatoN",
            "characterClass": "Sorceress",
            "gameMode": "Hardcore",
            "serverRegion": "Europe"
        },
        "headers": {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Host": "httpbin.org",
            "User-Agent": f"{origin_user_agent}",
            "X-Amzn-Trace-Id": f"{current_trace_id}"
        },
        "origin": f"{origin_ip}",
        "url": f"{body_url}"
    }

    assert r.status_code == 200
    assert response == expected_result
