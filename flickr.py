from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,sys,os,bs4,requests

katalog=input("Podaj tematyke obrazkow: ")

os.makedirs(katalog,exist_ok=True)


browser=webdriver.Firefox()
browser.get('https://www.flickr.com')

time.sleep(3)

searchElem=browser.find_element_by_id('search-field')
searchElem.send_keys(katalog)
searchElem.send_keys(Keys.ENTER)

res=requests.get('https://www.flickr.com/search/?text=' + katalog)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,features="html.parser")

divy=soup.find_all("div", class_="view photo-list-photo-view requiredToShowOnServer awake")

for i in range(len(divy)):
    divyst=str(divy[i].get('style'))
    start=divyst.find('url')+4
    end=divyst.find('jpg')+3
    imageUrl='https:' + divyst[start:end]
    print('Pobieranie obrazu %s...' % imageUrl)
    res=requests.get(imageUrl)
    res.raise_for_status()
    imageFile=open(os.path.join(katalog,os.path.basename(imageUrl)),'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
print('Gotowe!')

