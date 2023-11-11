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

# Simulating a click with Selenium
driver = webdriver.Chrome()  # You'll need the appropriate WebDriver for your browser
driver.get('https://public.enroll.wisc.edu/search?term=1244&keywords=phsyics')  # Replace this with the URL you want to scrape
driver.fullscreen_window()
# Perform clicks or interactions using Selenium, for example:
# driver.find_element_by_xpath("xpath_to_element").click()

# Once the page is in the state you want, retrieve the page source
#page_source = driver.page_source

# Now, you can use BeautifulSoup to parse the page
#soup = BeautifulSoup(page_source, 'html.parser')



python_button = driver.find_elements(By.CSS_SELECTOR, 'button.wrapper.ng-star-inserted')
#print(python_button)<button _ngcontent-ng-c3866329737="" color="primary" mat-raised-button="" class="mdc-button mdc-button--raised mat-mdc-raised-button mat-primary mat-mdc-button-base ng-star-inserted"><span class="mat-mdc-button-persistent-ripple mdc-button__ripple"></span><span class="mdc-button__label"> See sections </span><span class="mat-mdc-focus-indicator"></span><span class="mat-mdc-button-touch-target"></span><span class="mat-mdc-button-ripple"></span></button>

for button in python_button:
    #Clicking into the class
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.wrapper.ng-star-inserted')))
    time.sleep(0.2)
    button.click()

    #Clicking the session info
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="details"]/section/section/cse-course-details/section/header/div[2]/button')))
    time.sleep(0.2)
    sessionButton = driver.find_element(By.XPATH, '//*[@id="details"]/section/section/cse-course-details/section/header/div[2]/button')
    sessionButton.click()

    #Getting the sessions info
    time.sleep(0.5)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    dom = etree.HTML(str(soup)) 
    sessionInfos = dom.xpath('//*[@id="sections"]/section/section/cse-course-packages/cse-detail-topic/section/cse-package-group/details')[0]

    #Finding how many lecutres there are and finding the prof of each one
    lecs = soup.select('#sections > section > section > cse-course-packages > cse-detail-topic > section > cse-package-group')
    #print(lecs)
    prof_names = []
    for lec in range(len(lecs)):
        prof_name = lecs[lec].select_one('#sections > section > section > cse-course-packages > cse-detail-topic > section > cse-package-group > details > summary > cse-parent-header > cse-pack-header > div > div.cell.instructors.ng-star-inserted > span').text

        if prof_name == 'See details':
            prof_name = str(lecs[lec]).split('class="instructor ')[1].split('</strong>')[0].split('""> ')[1]

        print(lec, prof_name)
    
    #Exiting session menu
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="sections"]/section/mat-toolbar/button')))
    time.sleep(0.2)
                                   
    driver.find_element(By.XPATH, '//*[@id="sections"]/section/mat-toolbar/button').click()

    
    

    #    time.sleep(100)
    #except:
    #   print('no')
    #

time.sleep(5)

# Find elements or data on the page
# For example, to find all the links on the page
#classes = soup.find_all('div', {"class": "left grow catalog"})

#print(classes)
#print(classes[0].text)

#print(driver.find_elements_by_xpath("//input[@name='lang' and @value='Python']")[0])#.click();

#classButtons = driver.find_elements_by_class_name("ng-star-inserted")
#print(classButtons)

#for _class in classes:
#    driver.click()
#    print(_class.get(''))

# Remember to close the driver after you're done
driver.close()
