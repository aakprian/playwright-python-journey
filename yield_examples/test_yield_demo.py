import pytest


@pytest.fixture
def my_resource():
    print("\n🔧 SETUP: Creating resource")
    resource = "Important Data"

    yield resource  # Pause here!

    print("🧹 TEARDOWN: Cleaning up resource")


def test_one(my_resource):
    print(f"🧪 TEST 1: Using {my_resource}")
    assert my_resource == "Important Data"


def test_two(my_resource):
    print(f"🧪 TEST 2: Using {my_resource}")
    assert len(my_resource) > 0

