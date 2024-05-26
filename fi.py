from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# URL of the location to search
search_location = "Papa John's Pizza"

# Initialize the browser
driver = webdriver.Chrome()

# Open Google Maps
driver.get("https://www.google.com/maps")

# Find the search input field and enter the location
search_box = driver.find_element(By.ID, "searchboxinput")
search_box.send_keys(search_location)

# Submit the search query
search_box.submit()

# Wait for the search results to load
driver.implicitly_wait(5)

# Get the HTML content of the search results page
html_content = driver.page_source

# Close the browser
driver.quit()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the div element containing the phone number
phone_number_div = soup.find('span', class_='pp-place-title')

# Extract the phone number
phone_number = phone_number_div.text.strip()

print("Phone Number:", phone_number)
