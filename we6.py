from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def scrape_papa_johns_locations(url):
    # Set up the Chrome driver
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode for faster performance
    driver = webdriver.Chrome(service=service, options=options)

    # Open the URL
    driver.get(url)
    time.sleep(5)  # Wait for the page to load

    # Extract the page source
    page_source = driver.page_source

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Close the driver
    driver.quit()

    # Extract locations
    locations = []
    for location_div in soup.find_all('div', class_='store-address'):
        name = location_div.find('h2').text.strip()
        address = location_div.find('address').text.strip()
        locations.append({'name': name, 'address': address})

    return locations

# Example URLs
bronx_url = "https://locations.papajohns.com/united-states/ny/10455/bronx"
edmonton_url = "https://locations.papajohns.com/canada/ab/t6t1a7/edmonton"

bronx_locations = scrape_papa_johns_locations(bronx_url)
edmonton_locations = scrape_papa_johns_locations(edmonton_url)

print("Bronx Locations:")
for location in bronx_locations:
    print(location)

print("\nEdmonton Locations:")
for location in edmonton_locations:
    print(location)
