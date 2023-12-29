from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome('/Users/utkarshpadia/Downloads/chromedriver-mac-arm64/chromedriver')
from bs4 import BeautifulSoup
import time

driver.get('https://in.indeed.com/')
time.sleep(5)
job_title = driver.find_element_by_xpath('/html/body/div/div[1]/div/span/div[4]/div[1]/div/div/div/div/form/div/div[1]/div[1]/div/div/span/input')
job_title.send_keys('data scientist')
location = driver.find_element_by_xpath('/html/body/div/div[1]/div/span/div[4]/div[1]/div/div/div/div/form/div/div[1]/div[3]/div/div/span/input')
location.send_keys('Delhi')
driver.find_element_by_xpath('/html/body/div/div[1]/div/span/div[4]/div[1]/div/div/div/div/form/div/div[2]/button').click()
time.sleep(4)



driver.quit()