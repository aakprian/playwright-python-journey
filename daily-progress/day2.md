
## ⏰ Time Invested
Start: [10.30am]
End: [9pm]

## 🎯 Goals for Today
- [x] Learn pytest framework basics ✅
- [x] Understand pytest fixtures ✅
- [x] Learn fixture scopes ✅
- [x] Setup and teardown with yield ✅
- [x] Launch Chromium with playwright fixture ✅
- [ ] Understand page and playwright fixtures
- [ ] Identify web components using get_by_label and get_by_role
- [ ] Learn limitations of get_by_label

## 📝 What I Learned

### pytest Framework Basics
- pytest is a powerful testing framework for Python
- Simplifies test organization and execution
- Provides better assertions and reporting than standard unittest

### pytest Fixtures
**What are fixtures?**
- Functions that run before/after tests
- Provide data, objects, or setup for tests
- Help eliminate code duplication
- Make tests cleaner and more maintainable

**Example:**
```python
@pytest.fixture
def browser():
    # Setup code
    browser = launch_browser()
    yield browser  # Test runs here
    # Teardown code
    browser.close()
```

### Fixture Scopes
- **function** (default): Runs once per test function
- **class**: Runs once per test class
- **module**: Runs once per module (file)
- **session**: Runs once per entire test session

**Example:**
```python
@pytest.fixture(scope="session")
def browser():
    # Browser launches once for all tests
    pass
```

### Setup and Teardown with yield
- Code before `yield` = setup (runs before test)
- Code after `yield` = teardown (runs after test)
- Ensures cleanup happens even if test fails
```python
@pytest.fixture
def setup_browser():
    browser = chromium.launch()
    yield browser
    browser.close()  # Always runs, even if test fails
```

### Playwright Automation Testing

#### Running pytest from Terminal
```bash
pytest                          # Run all tests
pytest test_file.py            # Run specific file
pytest -v                      # Verbose output
pytest -s                      # Show print statements
pytest -k "test_name"          # Run tests matching pattern
pytest --headed                # Run with browser visible
pytest --browser chromium      # Specify browser
```

#### Launching Chromium with Playwright Fixture
- Playwright provides built-in pytest fixtures
- `playwright` fixture: gives access to Playwright instance
- `browser` fixture: provides browser instance
- `page` fixture: provides page instance

**Example:**
```python
def test_example(page):
    # 'page' fixture automatically provided by playwright
    page.goto("https://google.com")
    # Browser and page automatically cleaned up after test
```

## 💻 Tests Written
- day2_pytest_fixtures/
│   ├── 01_test_fixtures_intro.py          ✅ NEW
│   ├── 02_test_fixture_scopes.py          ✅ NEW
│   ├── 03_test_yield_setup_teardown.py    ✅ NEW
│   ├── 04_test_browser_fixture.py         ✅ NEW
│   └── 05_test_page_fixture.py            ✅ NEW
│
├── day2_browser_launching/
│   ├── 06_test_chromium_launch.py         ✅ NEW
│   ├── 07_test_browser_contexts.py        ✅ NEW
│   └── 08_test_multiple_pages.py          ✅ NEW
│
└── day2_locators/
    ├── 09_test_get_by_role.py             ✅ NEW
    └── 10_test_get_by_label.py            ✅ NEW

## 🔥 Key Takeaways

### pytest Fixtures
- ✅ Eliminate code repetition
- ✅ Guaranteed cleanup with yield
- ✅ Different scopes for different needs
- ✅ Module scope = efficient browser reuse

### Browser Launching
- ✅ Chromium can be headless (fast) or headed (debugging)
- ✅ Contexts = isolated sessions (like incognito)
- ✅ Multiple pages = multiple tabs in same browser
- ✅ slow_mo helps you see what's happening

### Locators
- ✅ get_by_role is BEST PRACTICE (accessibility)
- ✅ get_by_label works ONLY with proper <label> elements
- ✅ get_by_label FAILS with placeholders, aria-label
- ✅ Use get_by_placeholder, get_by_role as alternatives

## ✅ Completed
- ✅ pytest framework basics understood
- ✅ Fixtures and scopes learned
- ✅ Setup/teardown with yield keyword
- ✅ Chromium browser launching with fixtures

## 🚧 In Progress
- Understanding page and playwright fixtures in depth
- Learning get_by_label and get_by_role methods
- Understanding limitations of get_by_label

## 📅 Tomorrow's Plan (Day 3)
- How Auto wait works in playwright to handle wait mechanisms
- Understand how filter works on dynamic selection of card items from the list
- Applying Python string methods to retrieve the values with assertion checks 
- Advanced selectors and locators
- Page Object Model implementation
- More complex test scenarios
EOF