from src.head_hunter_api import HeadHunterAPI
from unittest.mock import patch


@patch("requests.get")
def test_head_hunter_api_requests(test_requests_api):

    obj_api = HeadHunterAPI()
    assert type(obj_api) is HeadHunterAPI