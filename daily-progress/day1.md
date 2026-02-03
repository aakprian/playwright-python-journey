# Day 1 - February 2, 2026

## ⏰ Time Invested
Start: 11:00 am
End: [Will update at end of day]

## 🎯 Goals for Today
- [x] Setup Python & Playwright ✅
- [x] Create GitHub repository ✅
- [x] Understand basic Playwright structure
- [ ] Write 5 basic tests
- [ ] Learn selectors (CSS, text, XPath)
- [ ] Practice waits and assertions

## 📝 What I Learned

### Setup
- Created virtual environment: `python3 -m venv venv`
- Installed Playwright: `pip install playwright`
- Installed browsers: `playwright install`
- Virtual env must be activated each session: `source venv/bin/activate`

### First Test
- Created basic test for example.com
- Learned browser launch options (headless=True/False)
- Practiced page navigation with `page.goto()`
- Used assertions to verify content

### Key Playwright Concepts
- `sync_playwright()` - Context manager for Playwright
- `browser.launch()` - Start browser instance
- `browser.new_page()` - Create new tab/page
- `page.goto(url)` - Navigate to URL
- `page.title()` - Get page title
- `page.inner_text(selector)` - Get text content

## 💻 Tests Written
1. `test_first.py` - Basic navigation and assertions test

## 🔥 Challenges Faced
- macOS externally-managed environment error → Solved with venv
- Needed to activate venv every session

## ✅ Completed
- ✅ Repository setup and structure
- ✅ Python virtual environment
- ✅ Playwright and pytest installed
- ✅ First test written
- ✅ Browsers installed

## 📅 Tomorrow's Plan
- pytest integration and fixtures
- Multiple test cases in one file
- Form interactions (fill, click, submit)
- Learn different selector strategies
- Screenshots and debugging