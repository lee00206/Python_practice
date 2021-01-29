import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.google.com')

html = req.text

soup = BeautifulSoup(html, 'html.parser')
select = soup.head.find_all('meta')

for meta in select:
    print(meta.get('content'))

    
