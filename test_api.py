import pytest
import api as service


@pytest.fixture
def api():
    return service.api


def test_hello_world(api):
    r = api.requests.post(
        "/german", data={'text': ['Hallo mein Name ist Johannes', 'Und du bist Peter, oder?']})
    assert r.json()['isGerman'] == True
