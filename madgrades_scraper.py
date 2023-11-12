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
#dummy_names = ['COMP SCI 320', 'MATH 340' , 'ART HIST 102']
db = client['myDatabase']
collection = db['CourseInfo']

new_db = client['NewDatabase']
new_collection = new_db['NewCollection']
for document in collection.find({}, {"Class Title": 1, "_id": 0}):
#for class_title in dummy_names:
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
        
        if gpa is None:
            gpa = '0'
        
        # Update the database
        # collection.update_one(
        #     {"Class Title": class_title}, 
        #     {"$set": {"GPA": gpa}}, 
        #     upsert=True
        # )
        course_dick.update({str(class_title): str(gpa)})


        new_collection.insert_one({"Class Title": class_title, "GPA": gpa})
        
#list_of_dicts = [{"Class Title": class_title, "GPA": gpa} for class_title, gpa in course_dick.items()]

#mangoSave(list_of_dicts)
driver.close()


