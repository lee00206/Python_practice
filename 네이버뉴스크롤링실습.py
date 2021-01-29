import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001"
req = requests.get(url)

html = req.text
soup = BeautifulSoup(html, 'html.parser')

my_titles = soup.select("#main_content>div.list_body.newsflash_body>ul.type06_headline>li>dl>dt>a")

for title in my_titles:
    print(title.text)
    print(title.get('href'))
    #columnlist.append(title.get('href'))

df = pd.DataFrame(columns = columnlist)
