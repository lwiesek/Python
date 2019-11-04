from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,sys,os,bs4,requests


browser=webdriver.Firefox()
browser.get('https://play2048.co/')
searchElem=browser.find_element_by_tag_name('body')

while True:
    try:
        if browser.find_element_by_class_name('game-message game-over'):
            break
    except:
        searchElem.send_keys(Keys.UP)
        searchElem.send_keys(Keys.RIGHT)
        searchElem.send_keys(Keys.DOWN)
        searchElem.send_keys(Keys.LEFT)
        time.sleep(0.25)


