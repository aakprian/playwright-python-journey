#Setup and Teardown with yield

import pytest


# Without yield - No cleanup guarantee
@pytest.fixture
def fixture_without_yield():
    print("\n SETUP: Creating resource")
    resource = "Important Data"
    # If test crashes, no cleanup
    return resource


#With yield - Cleanup always run
@pytest.fixture
def fixture_with_yield():
    print("\n SETUP: Creating resource")
    resource = "Important Data"
    
    yield resource  #Test runs now
    
    print("TEARDOWN: Cleaning up resource")


def test_using_yield_fixture(fixture_with_yield):
    print(f"TEST: Using {fixture_with_yield}")
    assert fixture_with_yield == "Important Data"
    print("✅ Test completed")


#File handling with yield
@pytest.fixture
def temp_file():
    #Create a file, test uses it, then delete
    print("\n📁 SETUP: Creating temporary file")
    filename = "temp_test.txt"
    with open(filename, "w") as f:
        f.write("Test data for automation")
    
    yield filename 
    
    #Delete file
    print("TEARDOWN: Deleting temporary file")
    import os
    if os.path.exists(filename):
        os.remove(filename)


def test_read_temp_file(temp_file):
    #read the temporary file
    print(f"TEST: Reading {temp_file}")
    with open(temp_file, "r") as f:
        content = f.read()
    assert "automation" in content
    print("✅ File read successfully")


#Simulating browser setup/teardown
@pytest.fixture
def mock_browser():
    #Simulates browser launch and close
    print("\nSETUP: Launching browser")
    browser = {
        "name": "Chrome",
        "version": "120",
        "status": "running"
    }
    
    yield browser
    
    print("TEARDOWN: Closing browser")
    browser["status"] = "closed"


def test_browser_navigation(mock_browser):
    print(f"TEST: Navigating with {mock_browser['name']}")
    assert mock_browser["status"] == "running"
    print("✅ Navigation successful")


# Database connection simulation
@pytest.fixture
def mock_database():
    print("\nSETUP: Connecting to database")
    db = {
        "connected": True,
        "tables": ["users", "products"],
        "records": 0
    }
    
    yield db 
    
    print("TEARDOWN: Closing database connection")
    db["connected"] = False


def test_database_query(mock_database):
    print(f"TEST: Querying database")
    assert mock_database["connected"] == True
    assert "users" in mock_database["tables"]
    print("✅ Query successful")


#What happens when test FAILS?
@pytest.fixture
def cleanup_always_runs():
    print("\n SETUP: Preparing test environment")
    
    yield "Test Data"
    
    print("TEARDOWN: This ALWAYS runs, even if test fails!")


def test_that_fails(cleanup_always_runs):
    print(f"TEST: About to fail...")
    assert False  
    #assert True  


#Multiple yielding fixtures
@pytest.fixture
def setup_step_1():
    print("\nSETUP: Step 1")
    yield "Step 1 Complete"
    print("TEARDOWN: Cleaning Step 1")


@pytest.fixture
def setup_step_2():
    print("SETUP: Step 2")
    yield "Step 2 Complete"
    print("TEARDOWN: Cleaning Step 2")


@pytest.fixture
def setup_step_3():
    print("SETUP: Step 3")
    yield "Step 3 Complete"
    print("TEARDOWN: Cleaning Step 3")


def test_multi_step_setup(setup_step_1, setup_step_2, setup_step_3):
    #Test using multiple fixtures with yield
    print(f"TEST: All steps ready!")
    assert "Complete" in setup_step_1
    assert "Complete" in setup_step_2
    assert "Complete" in setup_step_3
    print("✅ Test finished")