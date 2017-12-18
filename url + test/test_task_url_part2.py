import pytest
import urllib.request
from task_url_part2 import url_constractor

@pytest.fixture
def test_search():
    assert urllib.request.urlopen(url_constractor(100,777,'dm','skorking')).getcode() == 200
    assert urllib.request.urlopen(url_constractor(100, '*')).getcode() == 200
    assert urllib.request.urlopen("https://api.vkcom/method/users.get?user_ids=*,100&v=5.8&fields=nickname").getcode() == 500


def test_url_constractor():
    link = "https://api.vk.com/method/users.get?user_ids=100,777,dm,skorking&v=5.8&fields=nickname,sex,status,education,online,last_seen"
    assert url_constractor(100,777,'dm','skorking') == link
