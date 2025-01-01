import pandas as pd

krx_list = pd.read_excel('C:\\work\\상장법인목록.xlsx', engine='openpyxl')

krx_list.종목코드 = krx_list.종목코드.map('{:06d}'.format)
krx_list = krx_list.query('지역 == "경상남도"')
print(krx_list)
