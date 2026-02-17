# Playwright Python Automation Framework

A production-ready test automation framework built with **Python**, **Playwright**, and **pytest**, demonstrating real-world testing patterns including Page Object Model, data-driven testing, API automation, and BDD.

---

## 🛠️ Tech Stack

- **Python 3.12+**
- **Playwright** - Browser automation
- **pytest** - Test framework
- **pytest-playwright** - Playwright plugin for pytest
- **pytest-bdd** - BDD / Gherkin support
- **pytest-xdist** - Parallel test execution
- **pytest-html** - HTML test reporting

---

## 📁 Project Structure

```
playwright-python-journey/
├── conftest.py                  # Shared fixtures and browser setup
├── data/
│   └── credentials.json         # Test data (data-driven testing)
├── page_objects/
│   ├── login.py                 # Login page actions
│   ├── dashboard.py             # Dashboard page actions
│   ├── orders_history.py        # Orders history page actions
│   └── order_detail_page.py     # Order detail page actions
├── utils/
│   ├── apiBase.py               # Basic API utilities
│   └── apiBaseFramework.py      # Parameterized API utilities
├── features/
│   └── orderTransaction.feature # BDD feature files
├── tests/
│   ├── test_POM.py              # Page Object Model E2E test
│   ├── test_framework_web_api.py # Web + API combined test
│   ├── test_Network1.py         # API response mocking
│   ├── test_Network2.py         # Request interception & session injection
│   ├── test_UIValidations_1.py  # UI validations (popups, dynamic elements)
│   ├── test_MoreValidations.py  # Advanced UI (frames, tables, alerts)
│   ├── test_playwrightBasics.py # Core locators and browser basics
│   └── test_pytest-bddTest.py   # BDD step definitions
└── requirements.txt
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/aakprian/playwright-python-journey.git
cd playwright-python-journey
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
playwright install
```

---

## ▶️ Running Tests

### Run all tests
```bash
pytest -v
```

### Run specific test file
```bash
pytest tests/test_POM.py -v -s
```

### Run only smoke tests
```bash
pytest -m smoke -v
```

### Run in parallel (3 workers)
```bash
pytest -n 3 -v
```

### Run with HTML report
```bash
pytest --html=report.html -v
```

### Run with specific browser
```bash
pytest --browser_name firefox -v
```

---

## 🧠 Key Concepts Demonstrated

### 1. Page Object Model (POM)
Each page of the application is represented as a class. Each page method returns the next page object, creating a clean readable chain:

```python
login_page.navigate()
dashboard_page = login_page.login(user_name, user_password)
orders_page = dashboard_page.select_orders_nav_link()
order_detail_page = orders_page.right_order_view(user_name)
order_detail_page.confirm_order_placement()
```

### 2. Data-Driven Testing
Test credentials are stored in `data/credentials.json` and loaded dynamically:

```json
{
  "user_credentials": [
    { "user_email": "user1@example.com", "user_password": "pass1" },
    { "user_email": "user2@example.com", "user_password": "pass2" }
  ]
}
```

### 3. Parameterization
The same test runs automatically for multiple users using `@pytest.mark.parametrize`:

```python
@pytest.mark.parametrize("user_credentials", user_cred, indirect=True)
def test_POM(playwright, user_credentials):
    ...
```

### 4. API + UI Combined Testing
Orders are created via API and verified through the UI in the same test:

```python
api_utils = APIUtils()
orderId = api_utils.createOrder(playwright, user_credentials)  # API call
loginPage.navigate()                                           # UI verification
```

### 5. Network Interception & Mocking
Intercept and mock API responses to test edge cases:

```python
page.route("https://...get-orders-for-customer/*", intercept_response)
```

### 6. Session Injection
Skip login UI by injecting auth token directly into localStorage:

```python
page.add_init_script(f"""localStorage.setItem('token', '{getToken}')""")
```

### 7. BDD with pytest-bdd
Tests written in plain English using Gherkin syntax:

```gherkin
Given place the item order with <username> and <password>
And the user is on landing page
When I login to portal with <username> and <password>
And navigate to orders page
Then order message is successfully displayed
```

---

## 🌐 Test Application

All tests run against [Rahul Shetty Academy](https://rahulshettyacademy.com/client) - a dedicated e-commerce practice application for automation testing.

---

## 📊 Locator Strategy (Priority Order)

| Priority | Method | Example |
|----------|--------|---------|
| 1st | `get_by_role()` | `page.get_by_role("button", name="Login")` |
| 2nd | `get_by_label()` | `page.get_by_label("Email")` |
| 3rd | `get_by_placeholder()` | `page.get_by_placeholder("email@example.com")` |
| 4th | `get_by_text()` | `page.get_by_text("Checkout")` |
| Last | `page.locator()` | `page.locator("#userId")` |
