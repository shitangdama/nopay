# 主要进行两个测试

import pandas as pd
import tushare as ts
import matplotlib.pyplot as plt

data = pd.read_csv("./input/tmp_002049.csv")

data.index = pd.to_datetime(data.date, format='%Y-%m-%d')

# data = data.drop(["date"], axis=1)

# print(data)





# 之一对于日期比较重要的一个函数
# pandas.to_datetime¶


def find_max(data):
    tmp_day = data.head(1).index[0].strftime("%Y-%m-%d")
    tmp_max = 0
    tmp_num = 0
    count = 0 
    for index, row in data.iterrows():
        if row["close"] > tmp_max:
            tmp_num = count
            tmp_max = row["close"]
            tmp_day = index.strftime("%Y-%m-%d")
        count = count + 1
    
    return tmp_max, tmp_day, tmp_num

tmp_max, tmp_day, tmp_num = find_max(data)
print(tmp_num)
print(tmp_day)
print(tmp_max)


# 在看下获取最高点的图

# 用来练习先画出最高点最低点

import talib
import numpy as np
import tushare as ts
import matplotlib.pyplot as plt
import matplotlib.finance as mpf

sma_10 = talib.SMA(np.array(data['close']), 10)
sma_30 = talib.SMA(np.array(data['close']), 30)

fig = plt.figure(figsize=(17, 10))
ax = fig.add_axes([0,0.2,1,0.5])
ax2 = fig.add_axes([0,0,1,0.2])

mpf.candlestick2_ochl(ax, data['open'], data['close'], data['high'], data['low'], 
                     width=0.5, colorup='r', colordown='g', alpha=0.6)
ax.set_xticks(range(0, len(data['date']), 10))
# ax.plot(sma_10, label='10 日均线')
# ax.plot(sma_30, label='30 日均线')
ax.plot(tmp_num, tmp_max, 'gs')
ax.legend(loc='upper left')
ax.grid(True)

# mpf.volume_overlay(ax2, data['open'], data['close'], data['volume'], colorup='r', colordown='g', width=0.5, alpha=0.8)
# ax2.set_xticks(range(0, len(data['date']), 10))
# ax2.set_xticklabels(data['date'][::10], rotation=30)
# ax2.grid(True)

plt.show()