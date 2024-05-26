from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import openpyxl
import os

# Loading Selenium Webdriver
driver = webdriver.Edge()
wait = WebDriverWait(driver, 30)  # Increasing the timeout to 20 seconds

# Opening Google Maps
driver.get("https://www.google.com/maps")
time.sleep(3)

# Closing the Google consent form
try:
    widget = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
    driver.switch_to.frame(widget)
    button = wait.until(EC.presence_of_element_located((By.ID, 'introAgreeButton')))
    button.click()
    print("Consent form closed successfully.")
except TimeoutException:
    print("Consent form not found or not loaded within the timeout.")

# Finding the search box
driver.switch_to.default_content()
searchbox = wait.until(EC.presence_of_element_located((By.ID, 'searchboxinput')))
location = "Málaga"
searchbox.send_keys(location)
searchbox.send_keys(Keys.ENTER)
print("Searching for location:", location)
time.sleep(2)
try:
    cancelbut = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'gsst_a')))
    cancelbut.click()
    print("Cancel button clicked successfully.")
except NoSuchElementException:
    print("Cancel button not found.")

searchbox = wait.until(EC.presence_of_element_located((By.ID, 'searchboxinput')))
searchbox.clear()
searchbox.send_keys("seguro")
searchbox.send_keys(Keys.ENTER)
print("Searching for 'seguro'.")
time.sleep(3)

# Locating the results section
entries = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'section-result')))

if entries:
    print("Results found!")
else:
    print("No results found.")

# Close the browser
driver.quit()
