@pytest.fixture
def temp_file():
    # SETUP: Create a temporary file
    print("Creating temp file...")
    file = open("temp.txt", "w")
    file.write("Test data")
    file.close()

    yield "temp.txt"  # Give filename to test

    # TEARDOWN: Delete the file
    print("Deleting temp file...")
    import os
    os.remove("temp.txt")


def test_read_file(temp_file):
    # Test can use the file
    with open(temp_file, "r") as f:
        content = f.read()
    assert content == "Test data"
