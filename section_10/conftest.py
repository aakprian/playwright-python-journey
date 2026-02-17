import pytest
import json


with open('section_10/data/credentials.json') as f:
    test_data = json.load(f)
    user_cred = test_data["user_credentials"]


@pytest.fixture(scope="function")
def user_credentials(request):
    return request.param

