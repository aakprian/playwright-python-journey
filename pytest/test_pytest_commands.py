import pytest

# Fixture for setup
@pytest.fixture
def browser_setup():
    print("\n🔧 Setting up browser")
    yield "Chrome Browser"
    print("🧹 Closing browser")

# Test 1 - Simple test
def test_google_search(browser_setup):
    print(f"✅ Searching on Google using {browser_setup}")
    assert True

# Test 2 - Another simple test
def test_youtube_video(browser_setup):
    print(f"✅ Playing video on YouTube using {browser_setup}")
    assert True

# Test 3 - Login test
def test_login():
    print("✅ Testing login functionality")
    assert True

# Test 4 - Signup test
def test_signup():
    print("✅ Testing signup functionality")
    assert True

# Test 5 - This one will FAIL on purpose
def test_intentional_failure():
    print("❌ This test is designed to fail")
    assert False  # This will fail!

# Test 6 - Profile test
def test_profile_update():
    print("✅ Testing profile update")
    assert True