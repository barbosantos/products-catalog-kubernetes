import time

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Initialize a Selenium WebDriver (you need to have a compatible web driver installed)
# For example, using Chrome:
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get(
    "https://handlaprivatkund.ica.se/stores/1003777/categories?source=navigation"
)

# Wait for the page to load (you may need to adjust the time based on the page)
time.sleep(5)

# Handle the cookie consent pop-up
try:
    # Wait for the cookie consent pop-up to appear
    cookie_popup = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "cookie-consent-popup"))
    )

    # Accept the cookies
    accept_button = cookie_popup.find_element(By.CLASS_NAME, "accept-button")
    accept_button.click()
except:
    # If the pop-up doesn't appear, or if there is an error, continue without handling it
    pass

data = pd.DataFrame(
    columns=["product_name", "description1", "description2", "description3"]
)

# Get the initial page height
last_height = driver.execute_script("return document.body.scrollHeight")

# Number of iterations to scroll the page down
# TODO: Implement another way to reach bottom of the page instead of number of iterations
iterations = 55
# Scroll until the end of the page
for i in range(iterations):
    # Scroll down the page
    driver.find_element("tag name", "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(2)  # You may need to adjust the sleep duration

    # Get the updated page source and scrape data
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    soup = soup.find_all("div", {"class": "base__Body-sc-1mnb0pd-34 gRNUPx"})

    for elements in soup:
        if len(elements.contents) == 4:
            new_row = {
                "product_name": elements.contents[0].text,
                "description1": elements.contents[1].text,
                "description2": elements.contents[2].text,
                "description3": elements.contents[3].text,
            }
            data = data._append(new_row, ignore_index=True)

# Remove duplicates
data = data.drop_duplicates()
# Write all the scraped data to a CSV
data.to_csv("products.csv", index=False)

# Close the Selenium WebDriver
driver.quit()
