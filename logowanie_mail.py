from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,sys

if len(sys.argv) < 3:
    print('Too less arguments')

address=sys.argv[1]
topic=''.join(sys.argv[2:])

browser=webdriver.Firefox()
browser.get('https://login.yahoo.com/?.src=ym&.lang=pl-PL&.intl=pl&.done=https%3A%2F%2Fmail.yahoo.com%2Fd')

loginElem=browser.find_element_by_id('login-username')
loginElem.send_keys('wiesio52@yahoo.com')
loginElem.submit()

time.sleep(3)

passElem=browser.find_element_by_id('login-passwd')
passElem.send_keys('Fizyka11')
passElem.send_keys(Keys.ENTER)

time.sleep(5)

linkElem = browser.find_element_by_link_text('Redaguj')
linkElem.click()

time.sleep(5)

toElem=browser.find_element_by_id('message-to-field')
toElem.send_keys(address)

subjElem=browser.find_element_by_css_selector('[data-test-id="compose-subject"]')
subjElem.send_keys(topic)
