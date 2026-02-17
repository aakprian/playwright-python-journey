import pytest

@pytest.fixture
def database():
    # SETUP: Connect to database
    print("Connecting to database...")
    db = connect_to_database()

    yield db  # Give connection to test

    # TEARDOWN: Close connection
    print("Closing database connection...")
    db.close()


def test_insert_user(database):
    database.execute("INSERT INTO users VALUES ('John')")
    assert database.count_users() == 1

