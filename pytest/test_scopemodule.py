import pytest

@pytest.fixture(scope="module")  # ← Notice: scope="module"
def shared_number():
    print("🎯 Fixture running ONCE for the whole file!")
    return 10

def test_one(shared_number):
    print(f"Test 1 got: {shared_number}")
    assert shared_number == 10

def test_two(shared_number):
    print(f"Test 2 got: {shared_number}")
    assert shared_number == 10

def test_three(shared_number):
    print(f"Test 3 got: {shared_number}")
    assert shared_number == 10
