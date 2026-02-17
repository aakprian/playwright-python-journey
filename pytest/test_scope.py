import pytest

@pytest.fixture  # No scope = function scope (default)
def fresh_number():
    print("\n🎯 Creating a fresh number!")
    return 10

def test_one(fresh_number):
    print(f"Test 1 got: {fresh_number}")
    assert fresh_number == 10

def test_two(fresh_number):
    print(f"Test 2 got: {fresh_number}")
    assert fresh_number == 10

def test_three(fresh_number):
    print(f"Test 3 got: {fresh_number}")
    assert fresh_number == 10


"""
**Output:**
```
🎯 Creating a fresh number!
Test 1 got: 10
🎯 Creating a fresh number!
Test 2 got: 10
🎯 Creating a fresh number!
Test 3 got: 10
"""

