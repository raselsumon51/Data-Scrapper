from selenium import webdriver
from bs4 import BeautifulSoup

# URL of the webpage
url = "https://www.google.com/maps/place/Agrani+Bank+Limited/@23.1657144,89.2115403,17z/data=!3m1!4b1!4m6!3m5!1s0x39ff105fe0735757:0x4bc72f23eb15f78a!8m2!3d23.1657144!4d89.2115403!16s%2Fg%2F11d_83_719?entry=ttu"

# Configure the webdriver
driver = webdriver.Chrome()  # Change this line according to your browser and driver location

# Open the webpage
driver.get(url)

# Extract the HTML content of the webpage
html_content = driver.page_source

# Close the webdriver
driver.quit()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all elements with class "Io6YTe"
matches = soup.find_all("div", class_="Io6YTe")

# Print the text of each match
for match in matches:
    value = match.text.strip()
    phone_number_without_hyphen = value.replace("-", "")

    # Check if the remaining string is numeric
    if phone_number_without_hyphen.isdigit():
        print("The phone number is numeric:", phone_number_without_hyphen)
    # else:
    #     print("The phone number contains non-numeric characters.")
    # print(value)


h1_element = soup.find("h1")
if h1_element:
    print("Text content of <h1>:", h1_element.text.strip())