from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
def getBrowser():
    return webdriver.Firefox()
    
def lolKing(summonerName, browser):
    count = 0
    browser.get('http://www.lolnexus.com/NA/search?name='+summonerName)
    while("player-name" not in browser.page_source and count<400):
        time.sleep(.1)
        count+=1
    return browser.page_source