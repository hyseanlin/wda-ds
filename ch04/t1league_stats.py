from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://t1league.basketball/stats/team")

# Find the dropdown element by its ID, name, XPath, or other suitable locators
dropdown_locator = '//*[@id="__layout"]/main/div[3]/article/div[3]/section[1]/div/div/div/div[1]/div/select'  # Replace with the actual locator
dropdown_element = driver.find_element(By.XPATH, dropdown_locator)

# Create a Select object to interact with the dropdown
select = Select(dropdown_element)

# Select an option by its visible text
option_text = "2021-22 球季"
select.select_by_visible_text(option_text)

# Find the dropdown element by its ID, name, XPath, or other suitable locators
table_id = "vgt-table"  # Replace with the actual locator
table_element = driver.find_element(By.ID, table_id)
tr_tags = table_element.find_elements(By.TAG_NAME, "tr")
for tr_tag in tr_tags:
    td_tags = tr_tag.find_elements(By.TAG_NAME, "td")
    for td_tag in td_tags:
        print(td_tag.text, end=', ')
    print()

# Wait for a moment to see the change (you may need to adjust this based on the webpage)
time.sleep(2)

driver.quit()
