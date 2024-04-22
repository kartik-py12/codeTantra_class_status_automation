from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from twilio.rest import Client
import time

# Twilio credentials
account_sid = 'TWILIO_ACCOUNT_SID'
auth_token = 'TWILIO_AUTH_TOKEN'
twilio_phone_number = 'TWILIO_PHONE_NUMBER'
your_phone_number = 'YOUR_PHONE_NUMBER'


def login(username, password):
    while True:
        # Launch Chrome browser
        driver = webdriver.Chrome()

        # Navigate to the login page
        driver.get("https://myclass.lpu.in/")

        # Find the username and password fields and enter the credentials
        username_field = driver.find_element(By.CSS_SELECTOR, "input[aria-label='user name']")
        password_field = driver.find_element(By.CSS_SELECTOR, "input[aria-label='password']")
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Submit the form
        password_field.submit()

        # Click the "View Classes/Meetings" button
        view_button = driver.find_element(By.CSS_SELECTOR, "a[aria-label='View Classes and Meetings']")
        view_button.click()

        # Wait for the timetable page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "fc-event")))

        # Find the hyperlink element in the timetable and click it
        hyperlink_element = driver.find_element(By.XPATH, "//a[contains(@title, 'CSE101-Lecture')]")
        hyperlink_element.click()

        # Wait for the meeting page to load
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "meetingStatusPlaceholder")))

        # Find the meeting status element and print its text
        meeting_status_element = driver.find_element(By.ID, "meetingStatusPlaceholder")
        meeting_status = meeting_status_element.text.strip()
        print("Meeting Status:", meeting_status)

        # Check if meeting status is not equal to "Not started yet"
        if meeting_status != "Not started yet":
            # Initialize Twilio client
            client = Client(account_sid, auth_token)

            # Send a WhatsApp message
            message = client.messages.create(
                from_='whatsapp:' + twilio_phone_number,
                body='C class has been started',
                to='whatsapp:' + your_phone_number
            )
            print("WhatsApp message sent.")

            # Break out of the loop after sending the message
            break

        # Close the browser
        driver.quit()

        # Wait for 1 minute before checking again
        time.sleep(60)


# Call the login function with the provided username and password
login("YOUR_USERNAME", "YOUR_PASSWORD")
