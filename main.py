from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome('/Users/utkarshpadia/Downloads/chromedriver-mac-arm64/chromedriver')
from bs4 import BeautifulSoup
import time
link = 'https://in.indeed.com'
driver.get('https://in.indeed.com/')
time.sleep(3)
job_title = driver.find_element_by_xpath('/html/body/div/div[1]/div/span/div[4]/div[1]/div/div/div/div/form/div/div[1]/div[1]/div/div/span/input')
job_title.send_keys('data scientist')
location = driver.find_element_by_xpath('/html/body/div/div[1]/div/span/div[4]/div[1]/div/div/div/div/form/div/div[1]/div[3]/div/div/span/input')
location.send_keys('Delhi')
driver.find_element_by_xpath('/html/body/div/div[1]/div/span/div[4]/div[1]/div/div/div/div/form/div/div[2]/button').click()
time.sleep(3)

soup = BeautifulSoup(driver.page_source,'lxml')
jobs = soup.find_all('li',class_ = 'css-5lfssm eu4oa1w0')
print (len(jobs))
# print (soup)
job_info = {'link':[],'title':[],'company':[],'Location':[],'Salary':[],'posted days':[]}
for i in range(len(jobs)):
    tables = jobs[i].find_all('tbody')
    for j in range(len(tables)):
        if (j==0):
            job_link = tables[j].find('a').get('href')
            complete_link = link+job_link
            job_info['link'].append(complete_link)
            job_title = tables[j].find('a').text
            job_info['title'].append(job_title)
            company = tables[j].find('span',attrs = {'data-testid':'company-name'}).text
            job_info['company'].append(company)
            location = tables[j].find('div',attrs = {'data-testid':'text-location'}).text
            job_info['Location'].append(location)
            try:
                salary = tables[j].find('div',attrs = {'class':'metadata salary-snippet-container'}).text
            except:
                salary = 'NA'
            job_info['Salary'].append(salary)
        else:

            try:
                date = tables[j].find('span',class_ = 'date').text
            except:
                date = 'NA'

            job_info['posted days'].append(date)

print (job_info['Salary'])


# driver.quit()