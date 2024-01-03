import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
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
job_info = {'link':[],'title':[],'company':[],'Location':[],'Salary':[],'posted days':[]}
count = 0
previous_url = driver.current_url
current_url = ''
while(True):
    count += 1
    print (count,"  count")
    soup = BeautifulSoup(driver.page_source, 'lxml')

    jobs = soup.find_all('li',class_ = 'css-5lfssm eu4oa1w0')
    print (len(jobs))
    # print (soup)

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
    try:
        time.sleep(2)
        popup = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/button')
        popup.click()
    except:
        pass
    try:
        # element = soup.find('a',{'data-testid' :'pagination-page-next'})
        # print (element.text)
        # button_link = driver.find_element_by_link_text(element.text)
        # print (button_link)
        buttons = soup.find_all('li',class_ = 'css-227srf eu4oa1w0')
        print (len(buttons) , " buttons ")
        # button_bar = driver.find_element_by_xpath('/html/body/main/div/div[1]/div/div[5]/div[1]/nav/ul')

        button_link = driver.find_element_by_xpath('/html/body/main/div/div[1]/div/div[5]/div[1]/nav/ul/li['+str(len(buttons))+']/a')
        # button_link = driver.find_element_by_class_name('css-akkh0a e8ju0x50')
        driver.execute_script("arguments[0].scrollIntoView(true);", button_link)
        time.sleep(9)
        button_link.click()
        time.sleep(3)
        current_url = driver.current_url
        if (current_url==previous_url):
            break;
        else:
            previous_url = current_url

    except Exception as e:
        print (e)
        break
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # try:
    #     # print (soup.find_all('a'))
    #     button_link = soup.find('a',class_='css-akkh0a e8ju0x50')
    #     print(button_link)
    #     button_link = button_link.get('href')
    #
    #     complete_link = link+button_link
    #
    #     next_page = requests.get(complete_link)
    #     soup = BeautifulSoup(next_page.text,'lxml')
    #     print (soup)
    # except Exception as e:
    #     print (e)
    #     break

    if (count>8):
        break
# print (job_info['Salary'])

try:
    jobs = pd.DataFrame(job_info)
    jobs.to_csv('jobs.csv')
except:
    pass

driver.quit()