import requests
import pytest
import random

ip_addresses = []
payloads_list = []
payload_number = 3
number_of_ip = 3


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


def payload_generator():
    accounts_list = ['konfe', 'american_WaRRioR', 'Josh123', 'Not_My_Account']
    names_list = ['BatoN', 'Sniper-TG', 'smiTeR', 'jAvA', 'WW']
    class_list = ['Amazon', 'Assasin', 'Necromancer', 'Barbarian', 'Paladin', 'Sorceress', 'Druid']
    region_list = ['Europe', 'North America', 'Asia']
    mode_list = ['Softcore', 'Hardcore']

    payload = {
        "accountName": random.choice(accounts_list),
        "characterName": random.choice(names_list),
        "characterClass": random.choice(class_list),
        "serverRegion": random.choice(region_list),
        "gameMode": random.choice(mode_list)
    }

    return payload


for _ in range(payload_number):
    payload_tmp = payload_generator()
    payloads_list.append(payload_tmp)


def ip_generator():
    octets = []
    number_of_octet = random.randint(1, 4)
    for _ in range(number_of_octet):
        number = random.randint(0, 255)
        octets.append(str(number))

    ip_output = '.'.join(octets)
    return ip_output


for address in range(number_of_ip):
    ip_tmp = ip_generator()
    ip_addresses.append(ip_tmp)
