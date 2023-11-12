import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from lxml import etree 
import re
# Simulating a click with Selenium
driver = webdriver.Chrome()  # You'll need the appropriate WebDriver for your browser
driver.get('https://madgrades.com/search')  # Replace this with the URL you want to scrape
driver.fullscreen_window()
# Perform clicks or interactions using Selenium, for example:
# driver.find_element_by_xpath("xpath_to_element").click()

# Once the page is in the state you want, retrieve the page source
#page_source = driver.page_source

# Now, you can use BeautifulSoup to parse the page
#soup = BeautifulSoup(page_source, 'html.parser')


#root > div > div.app-content > div > div > div.col-xs-12.col-md-8.col-lg-9 > div.dimmable > div:nth-child(2) > div > div > a
#root > div > div.app-content > div > div > div.col-xs-12.col-md-8.col-lg-9 > div.dimmable > div:nth-child(2) > div > div > a
#root > div > div.app-content > div > div > div.col-xs-12.col-md-8.col-lg-9 > div.dimmable > div:nth-child(2) > div > div > a

soup = BeautifulSoup(driver.page_source, "html.parser")

html_string =  soup.select_one("#root > div > div.app-content > div > div > div.col-xs-12.col-md-8.col-lg-9 > div.dimmable > div:nth-child(2) > div > div > a")
href_match = re.search(r'href="([^"]+)"', str(html_string))

# Check if a match was found
if href_match:
    href_value = href_match.group(1)
    print(href_value)
else:
    print("Href attribute not found")

driver.get("https://madgrades.com" + href_value)
driver.fullscreen_window()
#print(string)
#root > div > div.app-content > div > div.row > div.col-xs-12.col-lg-8 > div > div > div:nth-child(2) > div:nth-child(2) > div > div > div > ul > li > span
soup = BeautifulSoup(driver.page_source, "html.parser")
gpa_string =  soup.select_one("#root > div > div.app-content > div > div.row > div.col-xs-12.col-lg-8 > div > div > div:nth-child(2) > div:nth-child(2) > div > div > div > ul > li > span")
#print(gpa_string)
pattern = r'(\d+\.\d+)\s*GPA'
# Search for the pattern in the string
match = re.search(pattern, str(gpa_string))
# Extract the GPA value
gpa = match.group(1) if match else None
print(gpa)
driver.close()

