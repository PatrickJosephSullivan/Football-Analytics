import os
from playwright.sync_api import sync_playwright
from random import randrange

# PP login credentials obfuscated by environment variables
email = os.getenv('email')
password = os.getenv('pp_pass')


with sync_playwright() as p:
    # Launch Firefox browser
    browser = p.firefox.launch(headless=False)  # Set headless=True for headless mode
    # Spoofs geolocation
    context = browser.new_context(
        geolocation={"latitude": 37.7749, "longitude": -122.4194},  # Example: San Francisco
        permissions=["geolocation"],  # Allow geolocation permissions
    )
    page = context.new_page()

    # Navigate to a webpage
    page.goto("https://app.prizepicks.com/login")

    # Locate and click the input field by its ID
    page.locator("#email-input").click()

    # Optionally, clear and type new text into the input field
    page.locator("#email-input").fill(email)

    # Locate and click the password field
    page.locator("input[placeholder='Type here...'][type='password']").click()
    page.locator("input[placeholder='Type here...'][type='password']").fill(password)
    page.locator("#submit-btn").click()
    
    page.wait_for_timeout(randrange(2000, 5000))

    page.wait_for_timeout(10000000)

    # Save the HTML of the current page
    # html = page.content()
    # with open("webpage.html", "w", encoding="utf-8") as file:
    #     file.write(html)

    # Close the browser
    # browser.close()
