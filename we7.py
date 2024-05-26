import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
url = "https://www.google.com/maps/place/Papa+Johns+Pizza/@38.8107569,-90.8627826,17z/data=!4m6!3m5!1s0x87dec8869d70dbd3:0x69ae0ea26b8e3f5c!8m2!3d38.8107569!4d-90.8627826!16s%2Fg%2F1td1dz54?entry=ttu"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")
print(soup)
# Find the div element containing the phone number
phone_number_element = soup.find("div", class_="Io6YTe fontBodyMedium kR99db")
print(phone_number_element)

if phone_number_element:
    phone_number = phone_number_element.text.strip()  # Get the text and remove leading/trailing whitespaces
    print("Phone number:", phone_number)
else:
    print("Phone number not found.")
