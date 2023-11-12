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
from mango import mangoify as mangoSave

# Simulating a click with Selenium
driver = webdriver.Chrome()  # You'll need the appropriate WebDriver for your browser
driver.get('https://public.enroll.wisc.edu/search?term=1244')  # Replace this with the URL you want to scrape
driver.fullscreen_window()
# Perform clicks or interactions using Selenium, for example:   
# driver.find_element_by_xpath("xpath_to_element").click()

# Once the page is in the state you want, retrieve the page source
#page_source = driver.page_source

# Now, you can use BeautifulSoup to parse the page
#soup = BeautifulSoup(page_source, 'html.parser')

def handelNone(x):
    if x == None:
        x = ''
    else:
        x = x.text
    x = x.rstrip().lstrip()
    return x

time.sleep(1)

broken_classes = []

for page in range(111):
    time.sleep(2)
    python_button = driver.find_elements(By.CSS_SELECTOR, 'button.wrapper.ng-star-inserted')
    #print(python_button)<button _ngcontent-ng-c3866329737="" color="primary" mat-raised-button="" class="mdc-button mdc-button--raised mat-mdc-raised-button mat-primary mat-mdc-button-base ng-star-inserted"><span class="mat-mdc-button-persistent-ripple mdc-button__ripple"></span><span class="mdc-button__label"> See sections </span><span class="mat-mdc-focus-indicator"></span><span class="mat-mdc-button-touch-target"></span><span class="mat-mdc-button-ripple"></span></button>

    for button in python_button:
        try:
            button.click()

            #WebDriverWait(driver, 10).until(EC.((By.XPATH, '//*[@id="details"]/section/section/cse-course-details/section/header/div[2]/button')))
            time.sleep(0.3)
        
            sessionButton = driver.find_element(By.XPATH, '//*[@id="details"]/section/section/cse-course-details/section/header/div[2]/button')
            sessionButton.click()

            time.sleep(0.25)
            
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            classTitle = soup.select_one('#sections > section > mat-toolbar > span').text.split(':')[0]

            #Finding how many lecutres there are and finding the prof of each one
            lecs = soup.select('#sections > section > section > cse-course-packages > cse-detail-topic > section > cse-package-group')
            prof_names = []

            sections = []

            for lec in range(len(lecs)):
                prof_name = lecs[lec].select_one('#sections > section > section > cse-course-packages > cse-detail-topic > section > cse-package-group > details > summary > cse-parent-header > cse-pack-header > div > div.cell.instructors.ng-star-inserted > span').text
                #print(prof_name)

                lec_n = (handelNone(lecs[lec].find('div', {'class': 'catalog-ref'})) + 'saved').split('saved')[1].lstrip()
                lec_location = handelNone(lecs[lec].find('span', {'class': 'has-location'}))
                lec_time = handelNone(lecs[lec].find('span', {'class': 'days-times'}))
                lec_credit = handelNone(lecs[lec].find('div', {'class': 'credits'}))
                print(lec_credit)

                if prof_name == 'See details':
                    prof_name = str(lecs[lec]).split('class="instructor ')[1].split('</strong>')[0].split('""> ')[1]

                discs = lecs[lec].find_all("summary", {'class': "child-summary"})
                if len(discs) == 0:
                    discs = lecs[lec].find_all("summary", {'class': "parent-summary"})

                
                for disc in range(len(discs)):
                    try:
                        sessionInfo = {}
                        sessionInfo['Class Title'] = classTitle
                        sessionInfo['Professor'] = prof_name
                        sessionInfo['Credits'] = lec_credit
                        sessionInfo['LecLoc'] = lec_location
                        sessionInfo['LecTime'] = lec_time
                        sessionInfo['LecNumber'] = lec_n
                        sessionInfo['DisLoc'] = ''
                        sessionInfo['DisTime'] = ''
                        sessionInfo['DisNumber'] = ''
                        sessionInfo['LabLoc'] = ''
                        sessionInfo['LabTime'] = ''
                        sessionInfo['LabNumber'] = ''
                        
                        if disc == 0:
                            if len(discs) > 1:
                                print('skip')
                                continue
                                

                        else:
                            section_ns = discs[disc].find_all('div', {'class', 'catalog-ref'})
                            section_times = discs[disc].find_all('span', {'class': 'days-times'})
                            section_locs = discs[disc].find_all('span', {'class': 'has-location'})
                            section_credits = handelNone(discs[disc].find('div', {'class': 'credits'}))

                            for sec in range(len(section_ns)):
                                num = (handelNone(section_ns[sec]) + 'saved').split('saved')[1].lstrip()
                                tim = (handelNone(section_times[sec])).lstrip()
                                loc = (handelNone(section_locs[sec])).lstrip()
                                if num[0:3] == 'DIS':
                                    sessionInfo['DisLoc'] = loc
                                    sessionInfo['DisTime'] = tim
                                    sessionInfo['DisNumber'] = num
                                else:
                                    sessionInfo['LabLoc'] = loc
                                    sessionInfo['LabTime'] = tim
                                    sessionInfo['LabNumber'] = num

                            if sessionInfo['Credits'] == '':
                                sessionInfo['Credits'] = section_credits
                        print(sessionInfo)
                        sections.append(sessionInfo)
                        #mangoSave([sessionInfo])
                    except Exception as e:
                        broken_classes.append(classTitle)
                        print(broken_classes, e)
            mangoSave(sections)
        except Exception as e:
            print('This is sad :(', e)
        
        #Exiting session menu
        #WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="sections"]/section/mat-toolbar/button')))
        time.sleep(0.1)
                                    
        driver.find_element(By.XPATH, '//*[@id="sections"]/section/mat-toolbar/button').click()

    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="results"]/section/section/cse-search-results/div[2]/button[2]').click()
    

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
