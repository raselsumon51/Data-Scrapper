# Import the necessary libraries
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Make browser open in background
options = webdriver.ChromeOptions()
options.add_argument('headless')

# Set the path to your chromedriver executable
driver_path = "C:\chromedriver_win32\chromedriver.exe"

# Set Chrome binary location
options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"

# Create the webdriver object
browser = webdriver.Chrome(options=options)

# URLs to scrape
urls = [
    "https://www.google.com/maps/place/Papa+John's+Pizza/@40.7936551,-74.0124687,17z/data=!3m1!4b1!4m5!3m4!1s0x89c2580eaa74451b:0x15d743e4f841e5ed!8m2!3d40.7936551!4d-74.0124687",
    "https://www.google.com/maps/place/Lucky+Dhaba/@30.653792,76.8165233,17z/data=!3m1!4b1!4m5!3m4!1s0x390feb3e3de1a031:0x862036ab85567f75!8m2!3d30.653792!4d76.818712"
]

# Loop through URLs
for index, url in enumerate(urls, start=1):
    # Open the URL
    browser.get(url)

    # Obtain the title of the place
    title = browser.find_element_by_xpath("//h1[contains(@class, 'x3AX1-LfntMc-header-title-title')]").text
    print(index, "-", title)

    # Obtain the contact number of the place
    phone = browser.find_elements_by_xpath("//span[contains(@class, 'cs0vCd')]")
    if phone:
        print("Contact Number:", phone[-1].text)
    else:
        print("Contact number not found.")
    print("\n")

# Close the browser
browser.quit()
