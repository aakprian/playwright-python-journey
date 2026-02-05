#Understanding Fixture Scopes
#function, class, module, session scopes

import pytest

# SCOPE 1: Function Scope (DEFAULT)
# Runs ONCE for EACH test
@pytest.fixture  # No scope = function scope (default)
def function_scope_fixture():
    print("\n🎯 FUNCTION SCOPE: Creating fresh data")
    return {"counter": 0}


def test_function_1(function_scope_fixture):
    function_scope_fixture["counter"] += 1
    print(f"Test 1 - Counter: {function_scope_fixture['counter']}")
    assert function_scope_fixture["counter"] == 1


def test_function_2(function_scope_fixture):
    function_scope_fixture["counter"] += 1
    print(f"Test 2 - Counter: {function_scope_fixture['counter']}")
    assert function_scope_fixture["counter"] == 1  # Still 1! Fresh fixture each time


def test_function_3(function_scope_fixture):
    function_scope_fixture["counter"] += 1
    print(f"Test 3 - Counter: {function_scope_fixture['counter']}")
    assert function_scope_fixture["counter"] == 1  # Still 1! Fresh fixture each time


#SCOPE 2: Module Scope
# Runs ONCE for the ENTIRE FILE
@pytest.fixture(scope="module")
def module_scope_fixture():
    print("\n🏢 MODULE SCOPE: Creating shared resource (runs once!)")
    return {"shared_counter": 0}


def test_module_1(module_scope_fixture):
    module_scope_fixture["shared_counter"] += 1
    print(f"Test 1 - Shared Counter: {module_scope_fixture['shared_counter']}")
    assert module_scope_fixture["shared_counter"] == 1


def test_module_2(module_scope_fixture):
    module_scope_fixture["shared_counter"] += 1
    print(f"Test 2 - Shared Counter: {module_scope_fixture['shared_counter']}")
    assert module_scope_fixture["shared_counter"] == 2  # Incremented! Same fixture


def test_module_3(module_scope_fixture):
    module_scope_fixture["shared_counter"] += 1
    print(f"Test 3 - Shared Counter: {module_scope_fixture['shared_counter']}")
    assert module_scope_fixture["shared_counter"] == 3  # Still incrementing!


# SCOPE 3: Class Scope
# Runs ONCE per TEST CLASS
@pytest.fixture(scope="class")
def class_scope_fixture():
    print("CLASS SCOPE: Creating class resource")
    return {"class_counter": 0}


class TestGroupA:
    def test_a1(self, class_scope_fixture):
        class_scope_fixture["class_counter"] += 1
        print(f"Group A - Test 1: {class_scope_fixture['class_counter']}")
        assert class_scope_fixture["class_counter"] == 1
    
    def test_a2(self, class_scope_fixture):
        class_scope_fixture["class_counter"] += 1
        print(f"Group A - Test 2: {class_scope_fixture['class_counter']}")
        assert class_scope_fixture["class_counter"] == 2


class TestGroupB:
    #gets a NEW fixture(fresh counter!)
    
    def test_b1(self, class_scope_fixture):
        class_scope_fixture["class_counter"] += 1
        print(f"Group B - Test 1: {class_scope_fixture['class_counter']}")
        assert class_scope_fixture["class_counter"] == 1  # Fresh counter!
    
    def test_b2(self, class_scope_fixture):
        class_scope_fixture["class_counter"] += 1
        print(f"Group B - Test 2: {class_scope_fixture['class_counter']}")
        assert class_scope_fixture["class_counter"] == 2


# Why scopes matter
@pytest.fixture(scope="module")
def expensive_browser_setup():
    print("EXPENSIVE OPERATION: Launching browser (once per file)")
    return "Browser Instance"


def test_scenario_1(expensive_browser_setup):
    print(f"✅ Scenario 1 using: {expensive_browser_setup}")
    assert expensive_browser_setup == "Browser Instance"


def test_scenario_2(expensive_browser_setup):
    print(f"✅ Scenario 2 using: {expensive_browser_setup}")
    assert expensive_browser_setup == "Browser Instance"


def test_scenario_3(expensive_browser_setup):
    print(f"✅ Scenario 3 using: {expensive_browser_setup}")
    assert expensive_browser_setup == "Browser Instance"

