import pandas as pd
import requests
from bs4 import BeautifulSoup

#krx_list = pd.read_html('c:\work\상장종목목록.xls')
#print(krx_list[0])
#krx_list[0].종목코드 = krx_list[0].종목코드.map('{:06d}'.format)
#print(krx_list[0].종목코드)
#print(krx_list[0])

url = 'https://kind.krx.co.kr/corpgeneral/corpList.do?method=download'
response = requests.get(url)
response.encoding = 'euc-kr'

# HTML을 파싱합니다.
soup = BeautifulSoup(response.text, 'html.parser')

# 테이블을 추출하여 데이터프레임으로 변환합니다.
tables = pd.read_html(str(soup))
krx_list = tables[0]

krx_list['종목코드'] = krx_list['종목코드'].map('{:06d}'.format)

print(krx_list)
