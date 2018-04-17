# 对股票数据进行泛化
# 编写特殊的的三个模块

# 流程是，获取数据，然后数据预处理，进行判断，收集数据，然后进行可视化
# 可视化主要分为三个图


# 该因子为寻找基础价位因子

# 判断基础价位

# 股盘定价公式

# 1两个月内的成交最低点
# 第一个图展示成交量小一定程度

import pandas as pd

data = pd.read_csv("./input/tmp_002049.csv")

limit_volume = (data["volume"].max() - data["volume"].min())/10 + data["volume"].min()

data = data[data["volume"] < limit_volume]

print(data)

# import matplotlib.pyplot as plt

# fig, ax = plt.subplots()


# ax.scatter(data.index, data["close"], s=data["volume"]/10000, alpha=0.5)
# ax.grid(True)
# fig.tight_layout()

# plt.show()