from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd

# URL of the location
url = "https://www.google.com/maps/place/Papa+John's+Pizza/@40.7936551,-74.0124687,17z/data=!3m1!4b1!4m5!3m4!1s0x89c2580eaa74451b:0x15d743e4f841e5ed!8m2!3d40.7936551!4d-74.0124687"

# Initialize the browser
driver = webdriver.Chrome()

# Open the URL
driver.get(url)

# Wait for the reviews section to load
wait = WebDriverWait(driver, 60)
try:
    reviews_section = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "section-review")))
except TimeoutException:
    print("TimeoutException: Reviews section not found.")
    # Print page source for debugging
    print(driver.page_source)
    driver.quit()
    exit()

# Extract review titles
review_titles = driver.find_elements(By.CLASS_NAME, "section-review-title")
titles = [a.text for a in review_titles]

# Extract review text
review_texts = driver.find_elements(By.CLASS_NAME, "section-review-review-content")
texts = [a.text for a in review_texts]

# Get the number of stars for each review
stars = driver.find_elements(By.CLASS_NAME, "section-review-stars")
stars_counts = []
for star_element in stars:
    active_stars = star_element.find_elements(By.CLASS_NAME, "section-review-star-active")
    stars_counts.append(len(active_stars))

# Extract phone numbers
phone_numbers = driver.find_elements(By.CLASS_NAME, "section-info-text")
phone_number = None
for info_text in phone_numbers:
    if "Call" in info_text.text:
        phone_number = info_text.text
        break

# Close the browser
driver.quit()

# Create a DataFrame
data = {
    'Title': titles,
    'Review Text': texts,
    'Stars': stars_counts
}
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel("reviews.xlsx", index=False)

print("Data saved to reviews.xlsx")
print("Phone Number:", phone_number)
