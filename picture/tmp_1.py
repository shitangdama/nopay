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
    for index, row in data.iterrows():
        if row["close"] > tmp_max:
            tmp_max = row["close"]
            tmp_day = index.strftime("%Y-%m-%d")
    
    return tmp_max, tmp_day

tmp_max, tmp_day = find_max(data)
print(tmp_day)
print(tmp_max)


# 需要看一下股票的分布图



# 在看下获取最高点的图

# 用来练习先画出最高点最低点

# fig, ax = plt.subplots()
# ax.plot(data["close"], "r-o")

# plt.xticks(rotation=45)

# # ax.set(xlabel='价格', ylabel='时间',
# #        title='初始')

# plt.xlabel("时间")
# plt.ylabel("股价（元）")
# plt.title("股票代码")
# ax.grid()

# # fig.savefig("./pic/test1.png")
# plt.show()