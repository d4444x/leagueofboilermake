from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
def getBrowser():
    return webdriver.Firefox()

def lolKing(summonerName, browser):
    count = 0
    browser.get('http://www.lolking.net/now/na/'+summonerName)
    while("purple-team lknow-team-table" not in browser.page_source and count<40):
        time.sleep(.1)
        count+=1
    if(count>=40):
    	return -1
    return browser.page_source
