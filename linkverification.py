import requests
from bs4 import BeautifulSoup

url = input('Enter the page you want to download\n')

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')

for link in soup.find_all('a'):
    print(link)
