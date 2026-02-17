#fixtures
import pytest

@pytest.fixture
def preWork():
    print("Ill setup browser instance")

def test_initial_check(preWork):
    print("This is the first test!")


@pytest.fixture
def ingredients():  # ← This is the "helpful friend" (FIXTURE)
    return ["flour", "sugar", "eggs"]  # ← These are the ingredients

def test_make_cookies(ingredients):  # ← You receive the ingredients automatically!
    print(f"I got: {ingredients}")
    assert "flour" in ingredients  # Testing that we have flour
    assert "sugar" in ingredients  # Testing that we have sugar