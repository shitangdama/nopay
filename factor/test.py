# 300504

import tushare as ts
import datetime


start_date = '2017-03-10'
today = datetime.datetime.today()
print(ts.get_hist_data("603214", start=start_date, end=str(today)))
print(ts.get_hist_data("603214", start=start_date, end=str(today)).sort_index(ascending=False))