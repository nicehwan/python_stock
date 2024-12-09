from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# url = 'https://finance.naver.com/item/frgn.naver?code=334890'
# with urlopen(url) as doc:
#     html = BeautifulSoup(doc, 'lxml')
#     print(html)
#     pgrr = html.find('td', class_='pgRR')
#
#     if pgrr and pgrr.a:
#         print(pgrr.a['href'])
#     else:
#         print("Element not found")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = 'https://finance.naver.com/item/frgn.naver?code=334890'
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')

pgrr = soup.find('td', class_='pgRR')
if pgrr and pgrr.a:
    print(pgrr.a['href'])
else:
    print("Element not found")

driver.quit()