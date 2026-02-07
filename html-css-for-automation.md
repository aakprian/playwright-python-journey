# HTML & CSS for Automation Testing
## Complete Guide for Test Automation Engineers

---

##  Table of Contents
1. [HTML basic understanding]
2. [The 4 Core Concepts]
3. [CSS Selectors]
4. [Inspection Workflow]
5. [Common HTML Elements]
6. [Selector Strategy]
7. [Real-World Examples]
8. [Troubleshooting]
9. [Best Practices]
10. [Quick Reference]

---


- HTML = The house structure (walls, doors, windows)
- CSS = The paint, decorations, colours
- JavaScript = The electricity, plumbing (makes things work)

### For Automation Testing:
You only need to read HTML to find elements! You don't need to write it.

### Basic Structure:
```html
<tagname attribute="value">Content</tagname>
```

Example:
```html
<button id="login" class="btn-primary">Click Me</button>
```

*Breaking it down:
- `<button>` - Opening tag (start of element)
- `id="login"` - Attribute with value
- `class="btn-primary"` - Another attribute
- `Click Me` - Content (what you see)
- `</button>` - Closing tag (end of element)

---

#The 4 Core Concepts

### 1. TAG NAME (Element Type)

What it is: The type/category of the element

Common Tags:

| Tag | Purpose | Example |
|-----|---------|---------|
| `<button>` | Clickable button | `<button>Submit</button>` |
| `<input>` | Input field | `<input type="text">` |
| `<a>` | Link | `<a href="...">Click here</a>` |
| `<div>` | Container box | `<div>Content</div>` |
| `<span>` | Inline container | `<span>Text</span>` |
| `<form>` | Form wrapper | `<form>...</form>` |
| `<h1>` to `<h6>` | Headings | `<h1>Title</h1>` |
| `<p>` | Paragraph | `<p>Some text</p>` |
| `<ul>`, `<ol>`, `<li>` | Lists | `<ul><li>Item</li></ul>` |
| `<table>`, `<tr>`, `<td>` | Tables | `<table><tr><td>Cell</td></tr></table>` |
| `<img>` | Image | `<img src="photo.jpg">` |
| `<select>`, `<option>` | Dropdown | `<select><option>Value</option></select>` |

In Playwright:
```python
page.locator("button")    # Finds all <button> elements
page.locator("input")     # Finds all <input> elements
page.locator("a")         # Finds all <a> (link) elements
```

When to use:
- When the tag itself is unique enough
- When combined with other selectors
- ❌ Alone (too generic, finds many elements)

---

### 2. ID (Unique Identifier)

What it is: A unique name for ONE element on the page (like a passport number)

*Rules:
- Each ID must be *unique* on the page
- Only ONE element can have a specific ID
- Most reliable selector for automation
- Never changes in well-designed apps

*Example:
```html
<input id="username" type="text">
<input id="password" type="password">
<button id="login-btn">Login</button>
```

*In Playwright:
```python
page.locator("#username")     The # means ID
page.locator("#password")
page.locator("#login-btn")
```

*Visual in Browser DevTools:
```html
<input id="email-field" class="form-input" type="email">
       ↑↑↑↑↑↑↑↑↑↑↑↑↑↑
       This is the ID!
```

*Why IDs are BEST for testing:
- Unique - only one per page
- Stable - rarely changes
- Fast - browser finds them quickly
- Clear - human-readable names

*Naming conventions you'll see:
- `id="login-button"` (kebab-case)
- `id="loginButton"` (camelCase)
- `id="login_button"` (snake_case)

---

### 3. CLASS (Group Label)

*What it is: A label that multiple elements can share (like a team jersey)

*Rules:
- Multiple elements can have the same class
- One element can have multiple classes
- Used for styling (CSS) and grouping
- Can change more often than IDs

*Example:
```html
<button class="btn btn-primary">Login</button>
<button class="btn btn-danger">Delete</button>
<button class="btn btn-success">Save</button>
<input class="form-input">
<input class="form-input">
```

*In Playwright:
```python
page.locator(".btn-primary")    # The . means CLASS
page.locator(".form-input")
page.locator(".btn")            # Finds ALL buttons with class="btn"
```

*Multiple Classes:
```html
<button class="btn btn-primary btn-large">Click</button>
```
This button has THREE classes:
1. `btn`
2. `btn-primary`
3. `btn-large`

*In Playwright (any of these work):
```python
page.locator(".btn")
page.locator(".btn-primary")
page.locator(".btn-large")
page.locator(".btn.btn-primary")  # Must have BOTH classes
```

*When to use:
- When no ID is available
- When the class is unique enough
- Be careful - classes can apply to many elements
- Classes may change when design changes

---

### 4. ATTRIBUTES (Properties)

*What they are: Extra information about an element (like labels on a product)

*Common Attributes:

| Attribute | Purpose | Example |
|-----------|---------|---------|
| `id` | Unique identifier | `id="login"` |
| `class` | Group label | `class="btn-primary"` |
| `type` | Input type | `type="text"`, `type="password"` |
| `name` | Form field name | `name="username"` |
| `placeholder` | Hint text | `placeholder="Enter email"` |
| `value` | Current value | `value="John"` |
| `href` | Link destination | `href="https://example.com"` |
| `src` | Image/script source | `src="logo.png"` |
| `alt` | Image description | `alt="Company logo"` |
| `disabled` | Disabled state | `disabled` |
| `required` | Required field | `required` |
| `data-testid` | Testing identifier | `data-testid="submit-button"` |
| `aria-label` | Accessibility label | `aria-label="Close dialog"` |

**Example with many attributes:
```html
<input 
  id="email"
  class="form-input"
  type="email"
  name="user_email"
  placeholder="Enter your email"
  value=""
  required
  aria-label="Email address"
  data-testid="email-input"
>
```

*In Playwright (selecting by attribute):
```python
# By type
page.locator("[type='email']")
page.locator("[type='password']")

# By name
page.locator("[name='username']")

# By placeholder
page.locator("[placeholder='Enter email']")
# OR better:
page.get_by_placeholder("Enter email")

# By data-testid (BEST for testing!)
page.locator("[data-testid='submit-button']")
# OR:
page.get_by_test_id("submit-button")

# By aria-label
page.locator("[aria-label='Close dialog']")
```

**Special: `data-testid`

This is a **testing-specific attribute** that developers add just for automation:

```html
<button data-testid="checkout-button">Checkout</button>
<input data-testid="username-input" type="text">
```

*Why it's great:
- Won't change when design changes
- Made specifically for testing
- Clear purpose
- Developer and tester friendly

**In Playwright:
```python
page.get_by_test_id("checkout-button")
page.get_by_test_id("username-input")
```

---

## CSS Selectors

**CSS Selectors** are patterns used to find elements. Think of them as **search queries** for HTML.

### Basic Selectors

#### 1. Tag Selector (no prefix)
```css
button      /* Finds all <button> elements */
input       /* Finds all <input> elements */
div         /* Finds all <div> elements */
```

**Playwright:**
```python
page.locator("button")
page.locator("input")
page.locator("div")
```

---

#### 2. ID Selector (# prefix)
```css
#login          /* Finds id="login" */
#username       /* Finds id="username" */
#submit-btn     /* Finds id="submit-btn" */
```

**Playwright:**
```python
page.locator("#login")
page.locator("#username")
page.locator("#submit-btn")
```

**Remember: `#` = ID

---

#### 3. Class Selector (. prefix)
```css
.btn-primary        /* Finds class="btn-primary" */
.form-input         /* Finds class="form-input" */
.error-message      /* Finds class="error-message" */
```

**Playwright:
```python
page.locator(".btn-primary")
page.locator(".form-input")
page.locator(".error-message")
```

**Remember: `.` = CLASS

---

#### 4. Attribute Selector ([ ] brackets)
```css
[type='text']                   /* Finds type="text" */
[name='username']               /* Finds name="username" */
[placeholder='Email']           /* Finds placeholder="Email" */
[data-testid='submit']          /* Finds data-testid="submit" */
```

**Playwright:
```python
page.locator("[type='text']")
page.locator("[name='username']")
page.locator("[placeholder='Email']")
page.locator("[data-testid='submit']")
```

---

### Combined Selectors

#### Combining Tag + Class
```css
button.btn-primary      /* <button class="btn-primary"> */
input.form-input        /* <input class="form-input"> */
div.error-message       /* <div class="error-message"> */
```

**Playwright:**
```python
page.locator("button.btn-primary")
page.locator("input.form-input")
```

---

#### Combining Tag + ID
```css
button#login        /* <button id="login"> */
input#username      /* <input id="username"> */
```

**Playwright:**
```python
page.locator("button#login")
page.locator("input#username")
```

---

#### Multiple Classes
```css
.btn.btn-primary            /* Must have BOTH classes */
.form-input.is-valid        /* Must have BOTH classes */
```

**Playwright:**
```python
page.locator(".btn.btn-primary")
page.locator(".form-input.is-valid")
```

---

### Advanced Selectors (Use Sparingly!)

#### Child Selector (>)
```css
div > button        /* Button that is direct child of div */
form > input        /* Input that is direct child of form */
```

**Playwright:
```python
page.locator("div > button")
page.locator("form > input")
```

---

#### Descendant Selector (space)
```css
div button          /* Button anywhere inside div */
form input          /* Input anywhere inside form */
```

**Playwright:**
```python
page.locator("div button")
page.locator("form input")
```

---

#### Attribute Contains
```css
[class*='btn']              /* class contains "btn" */
[id*='submit']              /* id contains "submit" */
[href*='google.com']        /* href contains "google.com" */
```

**Playwright:**
```python
page.locator("[class*='btn']")
page.locator("[id*='submit']")
```

---

## Inspection Workflow

### How to Find Elements in Browser

#### Step 1: Open Developer Tools
- **Windows/Linux:** `F12` or `Ctrl + Shift + I`
- **Mac: `Cmd + Option + I`
- **Or: Right-click → Inspect

#### Step 2: Inspect Element
1. Click the **selector tool** (arrow icon) in DevTools
2. Hover over the element you want to test
3. Click on it

**OR:**

1. Right-click directly on the element
2. Click "Inspect" or "Inspect Element"

#### Step 3: Read the HTML

```html
<button 
  id="login-button"           ← ID (BEST!)
  class="btn btn-primary"     ← Classes
  type="submit"               ← Attribute
  data-testid="login-btn"     ← Test ID (EXCELLENT!)
>
  Login                       ← Text content
</button>
```

#### Step 4: Choose Your Selector

**Priority (Best to Worst):

1. `data-testid` → `page.get_by_test_id("login-btn")`
2. `id` → `page.locator("#login-button")`
3. Playwright methods → `page.get_by_role("button", name="Login")`
4. `class` → `page.locator(".btn-primary")`
5. `tag + class` → `page.locator("button.btn-primary")`
6. ❌ Complex CSS → `page.locator("div > form > button:nth-child(2)")`

#### Step 5: Test in Browser Console
Before writing your test, verify the selector works:

**In browser console (F12 → Console tab):
```javascript
// Test your selector
document.querySelector("#login-button")
document.querySelectorAll(".btn-primary")

// Should highlight the element when you hover over the result
```

---

## Common HTML Elements

### Form Elements

#### Text Input
```html
<input id="username" type="text" placeholder="Username">
<input id="email" type="email" placeholder="Email">
```

**Playwright:**
```python
page.locator("#username").fill("testuser")
page.get_by_placeholder("Email").fill("test@example.com")
```

---

#### Password Input
```html
<input id="password" type="password">
```

**Playwright:**
```python
page.locator("#password").fill("secret123")
```

---

#### Checkbox
```html
<input id="terms" type="checkbox">
<label for="terms">I agree to terms</label>
```

**Playwright:**
```python
page.locator("#terms").check()
page.locator("#terms").uncheck()
```

---

#### Radio Button
```html
<input id="male" type="radio" name="gender" value="male">
<input id="female" type="radio" name="gender" value="female">
```

**Playwright:**
```python
page.locator("#male").check()
page.locator("#female").check()
```

---

#### Dropdown (Select)
```html
<select id="country">
  <option value="us">United States</option>
  <option value="ca">Canada</option>
  <option value="uk">United Kingdom</option>
</select>
```

**Playwright:**
```python
page.locator("#country").select_option("us")
page.locator("#country").select_option(label="Canada")
```

---

#### Button
```html
<button id="submit" type="submit">Submit</button>
<button id="cancel" type="button">Cancel</button>
```

**Playwright:**
```python
page.locator("#submit").click()
page.get_by_role("button", name="Submit").click()
```

---

### Content Elements

#### Links
```html
<a href="https://example.com" id="more-info">More Information</a>
```

**Playwright:**
```python
page.locator("#more-info").click()
page.get_by_role("link", name="More Information").click()
```

---

#### Headings
```html
<h1>Main Title</h1>
<h2>Subtitle</h2>
<h3>Section Title</h3>
```

**Playwright:**
```python
page.locator("h1").inner_text()
page.get_by_role("heading", level=1).inner_text()
```

---

#### Paragraphs
```html
<p class="description">This is a paragraph of text.</p>
```

**Playwright:**
```python
page.locator(".description").inner_text()
page.locator("p").inner_text()
```

---

#### Divs (Containers)
```html
<div id="container">
  <div class="header">Header</div>
  <div class="content">Content</div>
  <div class="footer">Footer</div>
</div>
```

**Playwright:**
```python
page.locator("#container")
page.locator(".header")
```

---

### Lists

#### Unordered List (bullets)
```html
<ul id="products">
  <li>Product 1</li>
  <li>Product 2</li>
  <li>Product 3</li>
</ul>
```

**Playwright:**
```python
page.locator("#products li")  # All list items
page.locator("#products li").count()  # Count items
page.locator("#products li").nth(0)  # First item
```

---

#### Ordered List (numbers)
```html
<ol id="steps">
  <li>Step 1</li>
  <li>Step 2</li>
  <li>Step 3</li>
</ol>
```

**Playwright:**
```python
page.locator("#steps li")
```

---

### Tables

```html
<table id="users">
  <thead>
    <tr>
      <th>Name</th>
      <th>Email</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>John</td>
      <td>john@example.com</td>
    </tr>
    <tr>
      <td>Jane</td>
      <td>jane@example.com</td>
    </tr>
  </tbody>
</table>
```

**Playwright:**
```python
# All rows
page.locator("#users tbody tr")

# Specific cell
page.locator("#users tbody tr").nth(0).locator("td").nth(1)

# Count rows
page.locator("#users tbody tr").count()
```

---

## 🎯 Selector Strategy

### Decision Tree: Which Selector to Use?

```
Start Here
    ↓
Has data-testid? 
    YES → Use get_by_test_id() BEST
    NO ↓
    
Has unique ID?
    YES → Use #id EXCELLENT
    NO ↓
    
Has role + name?
    YES → Use get_by_role() GREAT
    NO ↓
    
Has label?
    YES → Use get_by_label() GOOD
    NO ↓
    
Has placeholder?
    YES → Use get_by_placeholder() GOOD
    NO ↓
    
Has unique class?
    YES → Use .class OK
    NO ↓
    
Can combine selectors?
    YES → Use tag.class or tag#id OK
    NO ↓
    
Ask developer to add data-testid! 
```

---

### Selector Stability Ranking

**Most Stable (Rarely Changes):**
1. `data-testid` - Made for testing
2. `id` - Should be unique and stable
3. Playwright methods (`get_by_role`, `get_by_label`)

**Medium Stability:**
4. `name` attribute
5. `placeholder` text
6. `aria-label`

**Least Stable (Can Change Often):**
7. `class` - Changes with design
8. Text content - Changes with copy
9. Complex CSS paths - Very brittle

---

### Examples by Scenario

#### Login Form
```html
<form id="login-form">
  <input id="username" type="text" placeholder="Username">
  <input id="password" type="password" placeholder="Password">
  <button id="login-btn" type="submit">Login</button>
</form>
```

**Best Approach:**
```python
# Use IDs (most stable)
page.locator("#username").fill("testuser")
page.locator("#password").fill("password123")
page.locator("#login-btn").click()
```

**Alternative:**
```python
# Use Playwright methods
page.get_by_placeholder("Username").fill("testuser")
page.get_by_placeholder("Password").fill("password123")
page.get_by_role("button", name="Login").click()
```

---

#### Product Card (No IDs)
```html
<div class="product-card" data-testid="product-123">
  <h3 class="product-name">iPhone X</h3>
  <p class="product-price">$999</p>
  <button class="btn-add-cart">Add to Cart</button>
</div>
```

**Best Approach:
```python
# Use data-testid for container
product = page.get_by_test_id("product-123")

# Then find elements within
product.locator(".product-name").inner_text()
product.locator(".btn-add-cart").click()
```

**Alternative:
```python
# Use text content
page.locator("text=iPhone X")
page.locator("button:has-text('Add to Cart')").click()
```

---

#### Navigation Menu
```html
<nav id="main-nav">
  <a href="/home">Home</a>
  <a href="/products">Products</a>
  <a href="/about">About</a>
  <a href="/contact">Contact</a>
</nav>
```

**Best Approach:
```python
# Use role with name
page.get_by_role("link", name="Products").click()
page.get_by_role("link", name="Contact").click()
```

**Alternative:
```python
# Use href attribute
page.locator("[href='/products']").click()
```

---

## Real-World Examples

### Example 1: SauceDemo Login

**HTML:**
```html
<div class="login_wrapper">
  <input id="user-name" class="input_error" type="text" 
         placeholder="Username" name="user-name">
  <input id="password" class="input_error" type="password" 
         placeholder="Password" name="password">
  <input id="login-button" class="submit-button btn_action" 
         type="submit" value="Login">
</div>
```

**Automation Code:**
```python
def test_login(page):
    page.goto("https://www.saucedemo.com")
    
    # Option 1: Use IDs (BEST)
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    
    # Option 2: Use placeholders
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    
    # Verify login
    assert "inventory.html" in page.url
```

---

### Example 2: E-commerce Product Selection

**HTML:**
```html
<div class="inventory_list">
  <div class="inventory_item" data-testid="product-4">
    <div class="inventory_item_name">Sauce Labs Backpack</div>
    <div class="inventory_item_price">$29.99</div>
    <button class="btn_inventory" id="add-to-cart-sauce-labs-backpack">
      Add to cart
    </button>
  </div>
  <div class="inventory_item" data-testid="product-0">
    <div class="inventory_item_name">Sauce Labs Bike Light</div>
    <div class="inventory_item_price">$9.99</div>
    <button class="btn_inventory" id="add-to-cart-sauce-labs-bike-light">
      Add to cart
    </button>
  </div>
</div>
```

**Automation Code:**
```python
def test_add_products_to_cart(page):
    page.goto("https://www.saucedemo.com/inventory.html")
    
    # Method 1: Use button IDs (most specific)
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    page.locator("#add-to-cart-sauce-labs-bike-light").click()
    
    # Method 2: Use data-testid + find button within
    page.get_by_test_id("product-4").locator("button").click()
    page.get_by_test_id("product-0").locator("button").click()
    
    # Method 3: Use text content
    page.locator("text=Sauce Labs Backpack").locator("..").locator("button").click()
    
    # Verify cart count
    cart_badge = page.locator(".shopping_cart_badge")
    assert cart_badge.inner_text() == "2"
```

---

### Example 3: Form with Validation

**HTML:**
```html
<form id="registration-form">
  <div class="form-group">
    <label for="email">Email:</label>
    <input id="email" type="email" required 
           aria-label="Email address" data-testid="email-input">
    <span class="error-message" style="display: none;">Invalid email</span>
  </div>
  
  <div class="form-group">
    <label for="age">Age:</label>
    <input id="age" type="number" min="18" max="100" 
           data-testid="age-input">
    <span class="error-message" style="display: none;">Must be 18+</span>
  </div>
  
  <button type="submit" id="submit-btn" data-testid="submit-button">
    Register
  </button>
</form>
```

**Automation Code:**
```python
def test_form_validation(page):
    page.goto("https://example.com/register")
    
    # Fill form using best selectors
    page.get_by_test_id("email-input").fill("invalid-email")
    page.get_by_test_id("age-input").fill("15")
    page.get_by_test_id("submit-button").click()
    
    # Check error messages appear
    email_error = page.locator(".form-group").nth(0).locator(".error-message")
    age_error = page.locator(".form-group").nth(1).locator(".error-message")
    
    assert email_error.is_visible()
    assert age_error.is_visible()
    
    # Fix errors
    page.get_by_test_id("email-input").fill("valid@email.com")
    page.get_by_test_id("age-input").fill("25")
    page.get_by_test_id("submit-button").click()
    
    # Verify success
    assert page.url == "https://example.com/success"
```

---

### Example 4: Dynamic Lists

**HTML:**
```html
<ul id="todo-list">
  <li class="todo-item" data-id="1">
    <input type="checkbox" class="todo-checkbox">
    <span class="todo-text">Buy groceries</span>
    <button class="btn-delete">Delete</button>
  </li>
  <li class="todo-item" data-id="2">
    <input type="checkbox" class="todo-checkbox">
    <span class="todo-text">Walk the dog</span>
    <button class="btn-delete">Delete</button>
  </li>
  <li class="todo-item" data-id="3">
    <input type="checkbox" class="todo-checkbox">
    <span class="todo-text">Write tests</span>
    <button class="btn-delete">Delete</button>
  </li>
</ul>
```

**Automation Code:**
```python
def test_todo_list(page):
    page.goto("https://example.com/todos")
    
    # Count all todos
    todos = page.locator(".todo-item")
    initial_count = todos.count()
    assert initial_count == 3
    
    # Check first todo
    todos.nth(0).locator(".todo-checkbox").check()
    
    # Verify specific todo text
    first_todo_text = todos.nth(0).locator(".todo-text").inner_text()
    assert first_todo_text == "Buy groceries"
    
    # Delete second todo
    todos.nth(1).locator(".btn-delete").click()
    
    # Verify count decreased
    assert todos.count() == 2
    
    # Find specific todo by text
    write_tests_todo = page.locator(".todo-item:has-text('Write tests')")
    write_tests_todo.locator(".todo-checkbox").check()
```

---

## 🔧 Troubleshooting

### Common Issues

#### Issue 1: "Element not found"

**Cause:** Wrong selector or element not loaded yet

**Solutions:**
```python
# Wait for element
page.wait_for_selector("#login-button")
page.locator("#login-button").click()

# Or use Playwright's auto-wait
page.locator("#login-button").click()  # Waits automatically

# Check if element exists
if page.locator("#login-button").count() > 0:
    page.locator("#login-button").click()
```

---

#### Issue 2: "Multiple elements found"

**Cause:** Selector matches multiple elements

**Solutions:**
```python
# Get first match
page.locator(".btn").first.click()

# Get last match
page.locator(".btn").last.click()

# Get specific index
page.locator(".btn").nth(2).click()  # Third button

# Make selector more specific
page.locator("#form1 .btn-submit").click()  # Only submit button in form1
```

---

#### Issue 3: "Element is not clickable"

**Cause:** Element hidden, covered, or not ready

**Solutions:**
```python
# Wait for element to be visible
page.locator("#button").wait_for(state="visible")
page.locator("#button").click()

# Scroll into view
page.locator("#button").scroll_into_view_if_needed()
page.locator("#button").click()

# Force click (use carefully!)
page.locator("#button").click(force=True)
```

---

#### Issue 4: "Selector works in browser but not in test"

**Cause:** Dynamic content, different state

**Solutions:**
```python
# Add explicit wait
page.wait_for_load_state("networkidle")
page.locator("#button").click()

# Wait for specific element
page.wait_for_selector("#button", state="visible")

# Use more stable selector
# Instead of: page.locator(".dynamic-class-123")
# Use: page.locator("[data-testid='stable-id']")
```

---

### Debugging Tips

#### 1. Print what you're finding
```python
element = page.locator(".btn")
print(f"Found {element.count()} buttons")
print(f"First button text: {element.first.inner_text()}")
```

#### 2. Take screenshots
```python
page.screenshot(path="before_click.png")
page.locator("#button").click()
page.screenshot(path="after_click.png")
```

#### 3. Get element info
```python
element = page.locator("#button")
print(f"Tag: {element.evaluate('el => el.tagName')}")
print(f"Classes: {element.get_attribute('class')}")
print(f"ID: {element.get_attribute('id')}")
print(f"Text: {element.inner_text()}")
```

#### 4. Highlight element
```python
# Make element visible for debugging
page.locator("#button").evaluate("el => el.style.border = '3px solid red'")
page.wait_for_timeout(2000)  # Pause to see it
```

---

## Best Practices

### DO's 

1. **Use data-testid when available**
   ```python
   page.get_by_test_id("submit-button")
   ```

2. **Prefer IDs over classes**
   ```python
   # Good
   page.locator("#login-button")
   
   # Less good
   page.locator(".btn-login")
   ```

3. **Use Playwright's built-in selectors**
   ```python
   page.get_by_role("button", name="Submit")
   page.get_by_label("Email")
   page.get_by_placeholder("Search...")
   ```

4. **Be specific but not too complex**
   ```python
   # Good
   page.locator("#form1 button")
   
   # Too complex (brittle)
   page.locator("div > div > form > div:nth-child(2) > button")
   ```

5. **Use meaningful variable names**
   ```python
   login_button = page.locator("#login-btn")
   username_input = page.locator("#username")
   login_button.click()
   ```

---

### DON'Ts 

1. **Don't rely on generated class names**
   ```python
   # Bad - these change often
   page.locator(".css-1x2y3z")
   page.locator(".MuiButton-root-147")
   ```

2. **Don't use overly complex CSS**
   ```python
   # Bad - too fragile
   page.locator("div:nth-child(3) > span.text > a:first-child")
   
   # Better
   page.locator("[data-testid='main-link']")
   ```

3. **Don't use text content alone (if possible)**
   ```python
   # Risky - text can change
   page.locator("text=Click here")
   
   # Better
   page.locator("#action-button")
   ```

4. **Don't assume element positions**
   ```python
   # Bad - position can change
   page.locator("button").nth(2)
   
   # Better
   page.locator("#specific-button")
   ```

5. **Don't ignore wait conditions**
   ```python
   # Bad - may click before ready
   page.goto("https://example.com")
   page.locator("#button").click()  # Might fail!
   
   # Better
   page.goto("https://example.com")
   page.wait_for_load_state("networkidle")
   page.locator("#button").click()
   ```

---

## Quick Reference

### Selector Syntax Cheat Sheet

| What You Want | CSS Selector | Playwright Code |
|---------------|--------------|-----------------|
| Element by ID | `#login` | `page.locator("#login")` |
| Element by class | `.btn-primary` | `page.locator(".btn-primary")` |
| Element by tag | `button` | `page.locator("button")` |
| Element by attribute | `[type='text']` | `page.locator("[type='text']")` |
| Element by data-testid | `[data-testid='btn']` | `page.get_by_test_id("btn")` |
| Element by text | N/A | `page.locator("text=Login")` |
| Element by role | N/A | `page.get_by_role("button", name="Submit")` |
| Element by label | N/A | `page.get_by_label("Email")` |
| Element by placeholder | N/A | `page.get_by_placeholder("Search")` |

---

### Playwright Selector Methods

```python
# Best practices (use these!)
page.get_by_role("button", name="Submit")
page.get_by_label("Email")
page.get_by_placeholder("Search...")
page.get_by_test_id("submit-btn")
page.get_by_text("Click here")

# CSS selectors (use when above don't work)
page.locator("#id")
page.locator(".class")
page.locator("[attribute='value']")
page.locator("tag.class")

# Combining selectors
page.locator("#form").locator("button")
page.locator(".container").get_by_role("button")

# Multiple matches
page.locator(".btn").first
page.locator(".btn").last
page.locator(".btn").nth(2)
page.locator(".btn").count()

# Filtering
page.locator(".product").filter(has_text="iPhone")
page.locator(".item").filter(has=page.locator(".in-stock"))
```

---

### Common Patterns

#### Login
```python
page.locator("#username").fill("user")
page.locator("#password").fill("pass")
page.locator("#login-btn").click()
```

#### Form Submission
```python
page.get_by_label("Email").fill("test@test.com")
page.get_by_label("Password").fill("password")
page.get_by_role("button", name="Submit").click()
```

#### Dropdown Selection
```python
page.locator("#country").select_option("USA")
page.locator("#city").select_option(label="New York")
```

#### Checkbox/Radio
```python
page.locator("#terms").check()
page.locator("#newsletter").uncheck()
page.locator("#male").check()
```

#### Table Navigation
```python
# All rows
rows = page.locator("table tbody tr")

# Specific cell
cell = page.locator("table tbody tr").nth(0).locator("td").nth(1)

# Count rows
row_count = page.locator("table tbody tr").count()
```

---

### Element Actions

```python
# Click
page.locator("#btn").click()
page.locator("#btn").dblclick()
page.locator("#btn").click(button="right")  # Right click

# Type
page.locator("#input").fill("text")  # Clear then type
page.locator("#input").type("text")  # Type character by character
page.locator("#input").press("Enter")

# Get values
text = page.locator("#element").inner_text()
html = page.locator("#element").inner_html()
value = page.locator("#input").input_value()
attribute = page.locator("#element").get_attribute("class")

# Checks
is_visible = page.locator("#element").is_visible()
is_enabled = page.locator("#button").is_enabled()
is_checked = page.locator("#checkbox").is_checked()

# Waits
page.locator("#element").wait_for(state="visible")
page.locator("#element").wait_for(state="hidden")
page.wait_for_selector("#element")
```

---

## Summary

### The Essentials

**4 Core Concepts:
1. **Tag Name - Type of element (button, input, div)
2. **ID - Unique identifier (#id)
3. **Class - Group label (.class)
4. **Attributes - Extra properties ([attribute='value'])

**Selector Priority:
1. `data-testid`
2. `id`
3. Playwright methods (`get_by_role`, `get_by_label`)
4. `class`
5. Complex CSS

**Key Symbols:
- `#` = ID
- `.` = Class
- No symbol = Tag name
- `[ ]` = Attribute

**Inspection Workflow:
1. Right-click → Inspect
2. Read the HTML
3. Choose best selector
4. Test in browser console
5. Use in Playwright

**Golden Rule:**
> Always use the most stable, specific, and readable selector available!

---
