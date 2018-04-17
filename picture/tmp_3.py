# 抓住放量上行的股票

# 分析现在是否有上行放量的股票

# 因子判断
# 放量下行

import pandas as pd
import numpy as np
import tushare as ts
import matplotlib.pyplot as plt

data = pd.read_csv("./input/tmp_002049.csv")

date_array = []

# 画出关系图
# print(data.describe())

# import matplotlib.pyplot as plt

# fig, ax = plt.subplots()


# ax.scatter(data["close"], data["volume"], s=data["volume"]/10000, alpha=0.5)

# ax.set_xlabel("close", fontsize=15)
# ax.set_ylabel('volume', fontsize=15)
# ax.set_title('Volume and percent change')
# ax.grid(True)
# fig.tight_layout()

# plt.show()

# 在这里画一个成交量于价格的关系图
# 引入20日均线

# 最近五日成交量很低
# 并且波动不大
data["volume_var"] = 0
data["volume_mean"] = 0

# def find_fator(data):
#     # 获取因子
#     for index, row in data.iterrows():
#         if index > 5:
#             # 求近五天的成交量的值
#             pro_data = data.loc[range(index-5,index),:]
#             # if pro_data["volume"].mean() < 100000:
#             #     print(pro_data["volume"].var())
#             #     print(pro_data["volume"].mean())
#             #     print(pro_data["volume"].mad())
#             print(index)
#             data.ix[index-1]["volume_var"] = pro_data["volume"].var()/10000
#             data.ix[index-1]["volume_mean"] = pro_data["volume"].mean()
#             data.ix[index-1]["volume_mad"] = pro_data["volume"].mad()
            
def volume_var(row):    
    a = np.array([row["volume_1"], row["volume_2"],row["volume_3"],row["volume_4"],row["volume"]])
    # row["volume_var"] = np.var(a)
    # row["volume_mean"] = np.mean(a)
    return np.std(a/4000)

def volume_mean(row):    
    a = np.array([row["volume_1"], row["volume_2"],row["volume_3"],row["volume_4"],row["volume"]])
    # row["volume_var"] = np.var(a)
    # row["volume_mean"] = np.mean(a)
    return np.mean(a/10000)


# find_fator(data)
data["volume_1"] = data["volume"].shift(1)
data["volume_2"] = data["volume"].shift(2)
data["volume_3"] = data["volume"].shift(3)
data["volume_4"] = data["volume"].shift(4)
# data["volume_5"] = data["volume"].shift(5)
data = data.dropna()

data["volume_var"] = data.apply(volume_var, axis = 1)
data["volume_mean"] = data.apply(volume_mean, axis = 1)
data = data.drop(["volume_1","volume_2","volume_3","volume_4"],axis=1)
print(data)




import matplotlib.pyplot as plt

fig, ax = plt.subplots()

import talib

ax.set_xticks(range(0, len(data['date']), 30))
ax.set_xticklabels(data['date'][::30])

ax.plot(data["volume_var"], label='方差')
ax.plot(data["volume_mean"], label='均值')
ax.plot(data["close"], label='close')

plt.show()