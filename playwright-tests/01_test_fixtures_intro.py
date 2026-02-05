
#What are fixtures

import pytest


# PROBLEM: Without fixtures - Code repetition
def test_without_fixture_1():
    browser_name = "Chrome"
    print(f"\n🔧 Setting up {browser_name}")
    print(f"✅ Test 1 using {browser_name}")
    print(f"🧹 Cleaning up {browser_name}")
    assert True


def test_without_fixture_2():
    browser_name = "Chrome"  # Repeated!
    print(f"\n🔧 Setting up {browser_name}")  
    print(f"✅ Test 2 using {browser_name}")
    print(f"🧹 Cleaning up {browser_name}")  
    assert True


# Using fixtures - No repetition!
@pytest.fixture
def browser_setup():
    print("\n🔧 FIXTURE: Setting up browser")
    browser_name = "Chrome Browser"
    return browser_name


def test_with_fixture_1(browser_setup):
    print(f"✅ Test 1 using {browser_setup}")
    assert browser_setup == "Chrome Browser"


def test_with_fixture_2(browser_setup):
    print(f"✅ Test 2 using {browser_setup}")
    assert "Chrome" in browser_setup


def test_with_fixture_3(browser_setup):
    print(f"✅ Test 3 using {browser_setup}")
    assert len(browser_setup) > 0


# Multiple fixtures
@pytest.fixture
def test_data():
    return {
        "username": "testuser",
        "password": "testpass123",
        "email": "test@example.com"
    }


def test_using_multiple_fixtures(browser_setup, test_data):
    #using multiple fixtures
    print(f"✅ Using {browser_setup} with user: {test_data['username']}")
    assert test_data["username"] == "testuser"
    assert test_data["password"] == "testpass123"


