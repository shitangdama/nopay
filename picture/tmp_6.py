import pandas as pd
import tushare as ts

# data = ts.get_k_data("600104", start='2017-01-01', end='2018-04-13')
# data.to_csv("./input/tmp_600104.csv")

import pandas as pd
data = pd.read_csv("./input/tmp_600104.csv")

# 股价是一个月以来的最低值
# 成交量是一个月以来的最低值

import datetime
now = datetime.datetime.now()



def find_fator(data):
    for index, row in data.iterrows():
        if index >= 60:
            pro_data = data.loc[range(index-30,index),:]
            close_limit = (pro_data["close"].max() - pro_data["close"].min())/10 + pro_data["close"].min()
            limit_volume = (pro_data["volume"].max() - pro_data["volume"].min())/10 + pro_data["volume"].min()
            if row["close"] < close_limit and row["volume"] < limit_volume:
                print(row["date"])

                
find_fator(data)