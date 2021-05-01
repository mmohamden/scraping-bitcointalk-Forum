import csv
import time
import json
import pandas as pd 
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui
from time import sleep
import time
import requests
import lxml.html
import os.path
import re
import os
import bs4 
import sys
import webbrowser
from random import randint
import numpy as np
from selenium.webdriver.firefox.options import Options as FirefoxOptions
firefox_options = FirefoxOptions()
firefox_options.add_argument("")
driver = webdriver.Firefox(executable_path = r"C:\webdriver\geckodriver.exe", options = firefox_options)
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd



pages = np.arange(0, 80, 40)

talent_urls = []
for url in pages:
    driver.get ("https://bitcointalk.org/index.php?board=1."+str(url))
    wait = WebDriverWait(driver, 6)
    
    talent_links = driver.find_elements_by_xpath('/html/body/div[2]/div[3]/table/tbody/tr/td[3]/span') 
    for i in talent_links:
    
        talent_url = i.find_element_by_tag_name('a').get_attribute("href")
        talent_urls.append(talent_url)
    print(len(talent_urls))
f = csv.writer(open(r"C:\webdriver\List.csv", 'w', encoding='UTF-8', newline=''))
f.writerow(['posted_time', 'title', 'table'])
for link in talent_urls:
    driver.get(link) 
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0,3182)")
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(5)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    sleep(5)
    lastPage = False
    try:
        navPages = driver.find_elements_by_xpath(
            "//a[contains(@class, 'navPages')]"
        )
        navPages[-2].click()
        os.system('sleep 0.5')
    except:
        print('{} does not have extra page button')
    while(not lastPage):
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        articles = soup.find('div', {'id': 'bodyarea'}).findAll('td', {'class':  ['windowbg', 'windowbg2']})
        for tab in articles: 
            sleep(5)
            try:
                post_article = tab.find('td', 'td_headerandpost')
                post_article_meta = post_article.find('table').findAll('div')
                posted_time = post_article_meta[1].text
                title = post_article_meta[0].text.strip()
                table = post_article.find('div', attrs={'class': 'post'}).text
            
            except:
                Restrictions = "Not Found"
            try:
                print('posted_time = {}'.format(posted_time),
                'title = {}'.format(title),
                'table = {}'.format(table))
            except NoSuchElementException:
                continue
                f.writerow([posted_time, title, table])
        try:
            previous = driver.find_elements_by_xpath(
                "//span[contains(@class, 'prevnext')]"
            )
            previous = previous[0]
            if previous.text != '«':
                raise ValueError('')
            previous.click()
            os.system('sleep 0.5')
        except:
            lastPage = True
            
        
driver.close()

                    


   

