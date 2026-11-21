import os
from playwright.sync_api import sync_playwright

def test_mango_market_page():
    # Get the exact file path to index.html in the repo
    file_path = "file://" + os.path.abspath("index.html")

    with sync_playwright() as p:
        # Launch a headless Chrome browser
        browser = p.chromium.launch()
        page = browser.new_page()

        # 1. Open index.html
        page.goto(file_path)

        # 2. Verify the page heading loads
        heading = page.locator("header h1").inner_text()
        assert "Golden Orchard" in heading

        # 3. Verify initial cart count is 0
        assert page.locator("#cart-count").inner_text() == "0"

        # 4. Click the first "Add to Cart" button (Ratnagiri Alphonso - ₹1200)
        page.locator(".btn-add").first.click()

        # 5. Verify cart count becomes 1 and total updates to 1200
        assert page.locator("#cart-count").inner_text() == "1"
        assert page.locator("#cart-total").inner_text() == "1200"

        browser.close()
