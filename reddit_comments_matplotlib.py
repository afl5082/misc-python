import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import pandas as pd
import datetime
from scipy.stats import mstats

df = pd.read_csv('fire_comments.csv', parse_dates=['date'],
                 index_col=['date'])  #can't index date column
new_df = df[df.average < df.average.quantile(.95)]

#date_list = list(df.date)
#average_list = list(df.average)

fig, ax = plt.subplots(figsize=(9, 7))

ax.plot(new_df.index.values, new_df.average)

ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.xaxis.set_major_formatter(DateFormatter("%m/%d"))

plt.show()
""" x = [3, 4, 2, 3]
y = [10, 5, 3, 5]

plt.plot(x, y)
plt.show() """

#https://realpython.com/python-csv/
