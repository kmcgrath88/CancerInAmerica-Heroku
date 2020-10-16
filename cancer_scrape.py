# Import dependencies and setup
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

browser = None
# Function to intialize brower
def init_browser():

    # executable_path = {"executable_path": "chromedriver.exe"}
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    # driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    # return driver.get("https://www.cancer.gov/news-events")

    # chrome_options = Options()
    # chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')

    # chrome_options.add_argument('--disable-gpu')
    
    # # driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)


    # browser = driver.get("https://www.cancer.gov/news-events")

    executable_path = {"executable_path": os.environ.get("CHROMEDRIVER_PATH")}
    browser = Browser("chrome", **executable_path, headless=False)

    # return Browser("chrome", **executable_path, headless=False)

# Function to scrape information - steps from jupyter notebook
def scrape():
    init_browser()

    #####--Cancer News Site--#####
    url = "https://www.cancer.gov/news-events"
    browser.visit(url)

    # Allow page to load
    time.sleep(1) 

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Create empty dictionary
    news_data = {}
    # Retrieving the latest news title and text, and adding to dictionary
    article = soup.find('div', class_= 'feature-card')
    news_data['article_title'] = article.find('h3').text
    news_data['article_text'] = article.find('p').text
    # Retrieving the news url and adding to dictionary
    news_data['news_url'] = "https://www.cancer.gov" + article.find('a')['href']

    # Click first news article
    browser.find_by_css('div.image-hover').click()
    # Retrieving date and adding to dictionary
    news_data['date'] = browser.find_by_css('time').text

    # Quit the browser after scraping
    browser.quit()

    # Return results
    return news_data