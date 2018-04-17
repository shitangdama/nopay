# 第二个临时文件

# 三个目的。

# 是抓住该因子

# 对该因子进行统计

# 泛化到其他因子上去

# 下一步在做聚类统计

import pandas as pd
import tushare as ts
import matplotlib.pyplot as plt

data = pd.read_csv("./input/tmp_002049.csv")

# data.index = pd.to_datetime(data.date, format='%Y-%m-%d')

# 两个函数一个是diff，一个是shift
# pandas在移动时候多用平移方案
# 或者是对index进行操作，

collect_num = []
start = 0
dura = 0

# 上涨通道
# 上涨
def find_upper(data, day):
    start = 0
    dura = 0
    for index, row in data.iterrows():
        if index >= 3:
            num = index - 1
            if data.ix[num]["close"] > data.ix[num-1]["open"] or data.ix[num]["close"] > data.ix[num]["open"]:
                if data.ix[num-1]["close"] > data.ix[num-2]["open"] or data.ix[num-1]["close"] > data.ix[num-1]["open"]:
                    dura = dura + 1
                else:
                    if dura > day:
                        print(data.ix[start]["date"], dura)
                    start = num
                    dura = 0
find_upper(data, 4)