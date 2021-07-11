import bs4 as bs
import requests
import yfinance as yf
from datetime import date
import datetime
from datetime import timedelta
from pandas_datareader import data

headers = {'User-Agent': 'Firefox'}

resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
soup = bs.BeautifulSoup(resp.text, 'lxml')
table = soup.find('table', {'class': 'wikitable sortable'})
tickers = []
for row in table.findAll('tr')[1:]:
    ticker = row.findAll('td')[0].text
    tickers.append(ticker)

#tickers = [s.replace('\n', '') for s in tickers]

start_mod = date.today() - timedelta(days=4)
end_mod = date.today() - timedelta(days=3)

start = start_mod.strftime("%Y-%m-%d")
end = end_mod.strftime("%Y-%m-%d")

#start = datetime.datetime(2021, 7, 7)
#end = datetime.datetime(2021, 7, 8)

#data = yf.download('AAPL', start=start, end=end)

tickers_data = {}
tickers = ['aapl', 'amzn']
for ticker in tickers:

    data = yf.Ticker(ticker).info['marketCap']
    tickers_data[ticker] = data

#data = data.get_quote_yahoo('AMZN')['marketCap']
print(tickers_data)

#https://algotrading101.com/learn/yfinance-guide/