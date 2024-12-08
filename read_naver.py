from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://finance.naver.com/item/frgn.naver?code=334890'
with urlopen(url) as doc:
    html = BeautifulSoup(doc, 'lxml')
    pgrr = html.find('td', class_='pgRR')
    print(pgrr.a['href'])