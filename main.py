from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt

#yf.pdr_override()

#sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
#msft = pdr.get_data_yahoo('MSFT', start='2018-05-04')

sec = yf.download('005930.KS', start='2018-05-04')
msft = yf.download('MSFT', start='2018-05-04')
#
# plt.plot(sec.index, sec.Close, 'b', label='Samsung Electronics')
# plt.plot(msft.index, msft.Close, 'r--', label='Mircosoft')
plt.legend(loc='best')
#plt.show()

sec_dpc = (sec['Close']-sec['Close'].shift(1)) / sec['Close'].shift(1) * 100
sec_dpc.iloc[0] = 0
plt.hist(sec_dpc, bins=50)
plt.grid(True)
plt.show()