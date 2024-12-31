from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Hardcoded cookies (replace with your actual cookie values)
wa_web_session_cookie = "36000662-fdf3-4a00-abb3-0b5e25691ed7"  # Replace with your actual session cookie value
en_gb_cookie = "en_GB"  # Language cookie value, can be kept as is

# Set up headless WebDriver (no UI)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")

# Wait for the page to load (you can adjust time if necessary)
time.sleep(10)

# Add the hardcoded cookies to the session
cookies = [
    {"name": "WAWebSession", "value": wa_web_session_cookie, "domain": ".web.whatsapp.com"},
    {"name": "en_GB", "value": en_gb_cookie, "domain": ".web.whatsapp.com"}
]

# Add cookies to the browser session
for cookie in cookies:
    driver.add_cookie(cookie)

# Refresh the page to authenticate with the cookies
driver.refresh()

# Wait for WhatsApp Web to load and authenticate
time.sleep(5)

# Send a message to a contact using their phone number
phone_number = "9810261171"  # Replace with the phone number (in international format, e.g., +1 for USA)
message = "Hello, this is an automated message!"

# Open the WhatsApp chat for the specified phone number
driver.get(f"https://web.whatsapp.com/send?phone={phone_number}")

# Wait for the chat to load
time.sleep(5)

# Find the message input box and send the message
message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]')
message_box.send_keys(message)
message_box.send_keys(Keys.RETURN)

print(f"Message sent to {phone_number}")

# Close the browser after sending the message
time.sleep(2)
driver.quit()
