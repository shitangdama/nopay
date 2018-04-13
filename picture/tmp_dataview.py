# 主要进行两个测试

# 对基本面的分析

# 技术指标的过滤

#首先下载一只股票
import pandas as pd
import tushare as ts

data = ts.get_k_data("002049", start='2017-06-02', end='2018-04-12')
data.to_csv("./input/tmp_002049.csv")

####################

data = pd.read_csv("./input/tmp_002049.csv")

data.index = pd.to_datetime(data.date, format='%Y-%m-%d')
# data = data.drop(["date"], axis=1)

# print(data)


# 临时的收集
# def tmp_glean(data):
# 第一步先绘制出两个图
# 一个是k线图
# close图
# 找出连续上涨5天，和连续上涨3天
# 画出区块

# ax.set_xticks(range(0, len(data['date']), 10))
# ax.set_xticklabels(data['date'][::10])
import talib
import numpy as np
import tushare as ts
import matplotlib.pyplot as plt
import matplotlib.finance as mpf

sma_10 = talib.SMA(np.array(data['close']), 10)
sma_30 = talib.SMA(np.array(data['close']), 30)

fig = plt.figure(figsize=(24, 8))
ax = fig.add_subplot(1, 1, 1)
ax.set_xticks(range(0, len(data['date']), 30))
ax.set_xticklabels(data['date'][::30])
ax.plot(sma_10, label='10 日均线')
ax.plot(sma_30, label='30 日均线')
ax.legend(loc='upper left')

mpf.candlestick2_ochl(ax, data['open'], data['close'], data['high'], data['low'],
                     width=0.5, colorup='r', colordown='green',
                     alpha=0.6)
plt.show()

