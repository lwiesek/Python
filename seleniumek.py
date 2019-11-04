from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('display-3')
    print('Znaleziono element <%s> wraz z taka nazwa klasy!' % (elem.tag_name))
except:
    print('Nie udalo się znalezc elementu wraz z podana nazwa klasy.')
