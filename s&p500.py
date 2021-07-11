import bs4 as bs
import requests
import yfinance as yf
from datetime import date
import datetime

headers = {'User-Agent': 'Firefox'}

resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
soup = bs.BeautifulSoup(resp.text, 'lxml')
table = soup.find('table', {'class': 'wikitable sortable'})
tickers = []
for row in table.findAll('tr')[1:]:
    ticker = row.findAll('td')[0].text
    tickers.append(ticker)

tickers = [s.replace('\n', '') for s in tickers]

today = date.today().strftime("%Y-%m-%d")

start = datetime.datetime(2021, 7, 7)
end = datetime.datetime(2021, 7, 8)

print(today)

data = yf.download('AAPL', start="2021-07-07", end="2021-07-08")
print(data)