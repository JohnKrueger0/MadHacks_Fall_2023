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
import pymongo
import sys
from pymongo import MongoClient
from mango import mangoify as mangoSave


course_dick = {}

client = MongoClient('mongodb+srv://asanthanakri:dumbass@cluster0.9esju.mongodb.net/?retryWrites=true&w=majority')

driver = webdriver.Chrome()  # You'll need the appropriate WebDriver for your browser
driver.get('https://madgrades.com/search')  # Replace this with the URL you want to scrape
driver.fullscreen_window()

db = client['myDatabase']
collection = db['CourseInfo']
for document in collection.find({}, {"Class Title": 1, "_id": 0}):
    class_title = document.get("Class Title")
    if class_title in course_dick:
        continue
    else:
#root > div > div.app-content > div > div > div.col-xs-12.col-md-8.col-lg-9 > div.dimmable > div:nth-child(2) > div > div > a
        driver.get('https://madgrades.com/search?query=' + class_title.strip())  # Replace this with the URL you want to scrape

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
        time.sleep(1.25)
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
        
        if gpa = None:
            course_dick.update({str(class_title): '0'})
 
        course_dick.update({str(class_title): str(gpa)})
        


driver.close()


