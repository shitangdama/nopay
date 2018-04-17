# 近一个月股价的低点
# 一个月成交量的低点
# 1跌到基本价位

# 特殊信号识别
# 低位的清仓



import pandas as pd
# data = pd.read_csv("./input/tmp_002049.csv")

# 股价是一个月以来的最低值
# 成交量是一个月以来的最低值

# import datetime
# now = datetime.datetime.now()
# volume = data["volume"].std()
# print(volume)

# def find_fator(data):

#     for index, row in data.iterrows():
#         if index >= 60:
#             pro_data = data.loc[range(index-60,index),:]
#             close_limit = (pro_data["close"].max() - pro_data["close"].min())/10 + pro_data["close"].min()
#             limit_volume = (pro_data["volume"].max() - pro_data["volume"].min())/10 + pro_data["volume"].min()
#             if row["close"] < close_limit and row["volume"] < limit_volume:
#                 print(row["date"])


# find_fator(data)

data = pd.read_csv("./input/sz_result.csv")
sole_data = data[data["code"] == 300315]
print(sole_data)
first = sole_data.head(1)
first_num = first.index[0]

for index, row in sole_data.iterrows():

    data_volume = data.loc[range(first_num, index),["volume"]].std()/1000
    print(data_volume)