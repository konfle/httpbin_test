import requests
from httpbin_fixtures import get_ip, get_user_agent


def test_post_data(get_ip, get_user_agent):
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
            "User-Agent": f"{get_user_agent}",
            "X-Amzn-Trace-Id": f"{current_trace_id}"
        },
        "json": None,
        "origin": f"{get_ip}",
        "url": "https://httpbin.org/post"
    }

    assert r.status_code == 200
    assert response == expected_result


def test_get_data(get_ip, get_user_agent):
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
            "User-Agent": f"{get_user_agent}",
            "X-Amzn-Trace-Id": f"{current_trace_id}"
        },
        "origin": f"{get_ip}",
        "url": f"{body_url}"
    }

    assert r.status_code == 200
    assert response == expected_result
