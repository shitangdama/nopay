# 

# 双均线迭代

# 先获取数据


import pandas as pd
import tushare as ts
import talib
from backtest.backtest import Backtest

# data = ts.get_k_data('000001', index=True)
# data.to_csv("./input/sh000001.csv")


data = pd.read_csv("./input/sh000001.csv")



prices = data["close"]

MA5 = talib.MA(prices, timeperiod=5) # 计算5日均线
MA50 = talib.MA(prices, timeperiod=50) #计算60日均线

data["ma5"] = MA5
data["ma50"] = MA50

data["all_income"] = 0
data["income"] = 0
data["order"] = 0
data["order_num"] = 0
data["trade"] = data["close"]

data = data.dropna()
data.index = range(0,data.shape[0])

backtest = Backtest(data)

backtest.test_run_backtest()
# print(backtest.all_incomes)
# print(backtest.trade_income)

trade_data = pd.DataFrame(backtest.trade_plot)
print(trade_data)
print(backtest.money)


import matplotlib.pyplot as plt

fig, ax = plt.subplots()

color = trade_data["order"]*100

ax.scatter(trade_data.index, trade_data["close"], c=color, alpha=0.5)
ax.plot(data["close"])
ax.plot(data["ma5"])
ax.plot(data["ma50"])
data["all_income"] = data["all_income"]*100

ax.set_xlabel("close", fontsize=15)
ax.set_ylabel('volume', fontsize=15)
ax.set_title('Volume and percent change')

ax.grid(True)
fig.tight_layout()

plt.show()