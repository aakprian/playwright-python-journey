# Playwright Python Automation Framework

A professional test automation framework built with **Playwright**, **Pytest**, and **Python** — covering UI, API, hybrid, and network interception testing with full CI/CD integration.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Playwright | Browser automation & network interception |
| Pytest | Test runner, fixtures, parameterization |
| Python 3.11+ | Core language |
| pytest-bdd | BDD / Gherkin scenario testing |
| pytest-html | HTML test reports |
| pytest-xdist | Parallel test execution |
| GitLab CI | Automated pipeline on every push |

---

## Framework Structure
```
playwright-python-journey/
│
├── conftest.py                  # Global fixtures, browser setup, CLI options
├── pytest.ini                   # Markers, test paths, global config
├── requirements.txt             # Dependencies
├── .gitlab-ci.yml               # CI/CD pipeline
│
├── pages/                       # Page Object Model layer
│   ├── login.py                 # Login page actions
│   ├── dashboard.py             # Dashboard navigation
│   ├── orders_history.py        # Orders table interactions
│   └── order_detail_page.py     # Order detail assertions
│
├── tests/
│   ├── ui/
│   │   └── test_order_flow.py   # End to end UI test via POM
│   ├── api/
│   │   └── test_order_api.py    # Hybrid API + UI test
│   └── network/
│       ├── test_intercept_fulfill.py   # Mock API responses
│       └── test_intercept_continue.py  # Redirect requests
│
├── bdd/
│   ├── features/
│   │   └── order_flow.feature   # Gherkin scenarios
│   └── step_definitions/
│       └── test_order_steps.py  # Step implementations
│
├── utils/
│   └── api_utils.py             # API utility class (auth + order creation)
│
└── data/
    └── test_data.json           # External test data (credentials)
```

---

## Key Features

### Page Object Model
Each page is a class. Each action returns the next page object — enabling clean method chaining across the full user journey:
```python
login_page.login(email, password)
    .navigate_to_orders()
    .get_first_order(email)
    .confirm_order_placed()
```

### Hybrid API + UI Testing
Orders are created via API (fast, reliable test data setup) then verified in the UI — the gold standard for modern SDET test design:
```python
order_id = api_utils.create_order(playwright, email, password)
# → UI navigates to orders and asserts the order exists
```

### Network Interception
Two interception strategies covered:
- `route.fulfill()` — mock API responses to test edge cases
- `route.continue_()` — redirect requests to specific test data

### Data Driven Testing
Credentials and test data loaded from `data/test_data.json` — no hardcoded values anywhere in the test code:
```python
@pytest.mark.parametrize("user_credentials", user_cred, indirect=True)
def test_order_flow(browser_instance, user_credentials):
```

### Multi-Browser Support
Run tests on any browser via CLI:
```bash
pytest tests/ --browser_name=chrome
pytest tests/ --browser_name=firefox
pytest tests/ --browser_name=webkit
```

---

## Getting Started

### Prerequisites
- Python 3.11+
- pip

### Installation
```bash
git clone https://github.com/aakprian/playwright-python-journey.git
cd playwright-python-journey
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install
```

### Running Tests
```bash
# Run all tests
pytest tests/ -v

# Run specific suite
pytest tests/ui/ -v
pytest tests/api/ -v
pytest tests/network/ -v

# Run on specific browser
pytest tests/ --browser_name=firefox

# Generate HTML report
pytest tests/ --html=reports/report.html --self-contained-html
```

---

## CI/CD

Every push to `main` triggers the GitLab CI pipeline which:
1. Installs dependencies
2. Installs Playwright browsers
3. Runs the full test suite in headless mode
4. Publishes test artifacts

---

## Author

**Aakash Senthil Kumar**
QA Automation Engineer — Playwright · Python · Pytest · CI/CD
[GitHub](https://github.com/aakprian)