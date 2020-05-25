import pytest
import requests
import json
from .const import *

class Test_httpbin():
    def test_get_ip(self):
        url = BASE_URL + IP_URL
        print(url)
        r = requests.get(url)
        print(r.headers)
        print(r.text)
        response_data = json.loads(r.text)
        print(response_data)
        assert 200 == r.status_code
        assert LOCAL_IP == response_data["origin"]
    def test_post_method(self):
        url = BASE_URL + POST_TEST_URL
        post_data = {"name": "ycq", "pwd": "123456"}
        r = requests.post(url, data=post_data)
        print(r.text)
        response_data = r.json()
        assert 200 == r.status_code
        assert post_data["name"] == response_data["form"]["name"]
        assert post_data["pwd"] == response_data["form"]["pwd"]

    def test_delete_method(self):
        url = BASE_URL + DELETE_TEST_URL
        delete_data = {"name": "lily", "pwd": "123456"}
        r = requests.delete(url, data=delete_data)
        print(r.text)
        response_data = r.json()
        print(response_data)
        # assert 200 == r.status_code
        assert delete_data["name"] == response_data["form"]["name"]
        assert delete_data["pwd"] == response_data["form"]["pwd"]