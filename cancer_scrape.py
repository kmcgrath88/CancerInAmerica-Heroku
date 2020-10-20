# Import dependencies and setup
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import requests

browser = None

# Function to scrape information - steps from jupyter notebook
def scrape():

    #####--Cancer News Site--#####
    url = "https://www.cancer.gov/news-events"
    # browser.visit(url)
    resp = requests.get(url)

    # Allow page to load
    time.sleep(1) 

    # Scrape page into Soup
    # html = browser.html
    soup = bs(resp.text, "html.parser")

    # Create empty dictionary
    news_data = {}
    # Retrieving the latest news title and text, and adding to dictionary
    article = soup.find('div', class_= 'feature-card')
    news_data['article_title'] = article.find('h3').text
    news_data['article_text'] = article.find('p').text
    # Retrieving the news url and adding to dictionary
    news_data['news_url'] = "https://www.cancer.gov" + article.find('a')['href']

    # Click first news article
    resp2 = requests.get(news_data['news_url'])
    soup2 = bs(resp2.text, "html.parser")
    # Retrieving date and adding to dictionary
    news_data['date'] = soup2.find('time').text

    # Return results
    return news_data