from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URL of the location
url = "https://www.google.com/maps/place/Papa+John's+Pizza/@40.7936551,-74.0124687,17z/data=!3m1!4b1!4m5!3m4!1s0x89c2580eaa74451b:0x15d743e4f841e5ed!8m2!3d40.7936551!4d-74.0124687"

# Initialize the browser
driver = webdriver.Chrome()

# Open the URL
driver.get(url)

# Wait for the reviews section to load
wait = WebDriverWait(driver, 10)
reviews_section = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "section-review")))

# Extract review titles
review_titles = driver.find_elements(By.CLASS_NAME, "section-review-title")
print([a.text for a in review_titles])

# Extract review text
review_text = driver.find_elements(By.CLASS_NAME, "section-review-review-content")
print([a.text for a in review_text])

# Get the number of stars for the first review
stars = driver.find_elements(By.CLASS_NAME, "section-review-stars")
if stars:
    first_review_stars = stars[0]
    active_stars = first_review_stars.find_elements(By.CLASS_NAME, "section-review-star-active")
    print(f"The stars the first review got was {len(active_stars)}")
else:
    print("No reviews found.")

# Close the browser
driver.quit()
