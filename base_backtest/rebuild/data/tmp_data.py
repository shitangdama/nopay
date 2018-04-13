# 该文件的作用，抽取沪深300的股票并且吧他们合在一起
# 输出一个csv
import pandas as pd
import tushare as ts

#####################################
# 沪深300
# hs300 = ts.get_hs300s()
# hs300.to_csv("./input/hs300.csv")
##############################
# 上证50成份股

# sz30 = ts.get_sz50s()
# sz30.to_csv("./input/sz30.csv")
###########################
sz30 = pd.read_csv("./input/sz30.csv")
all_stock_data = []

count = 0
for index, row in sz30.iterrows():
    # print(row["code"])
    code = str(row.code).zfill(6)
    print("开始获取"+ code)
    stock_data = ts.get_k_data(code, start='2017-06-02', end='2018-04-12')
    stock_data.index = pd.to_datetime(stock_data.date, format='%Y-%m-%d')
    stock_data = stock_data.drop(["date"], axis=1)
    stock_data["code"] = code
    print("获取完成获取"+ code)
    print(count)
    count = count + 1
    all_stock_data.append(stock_data)
result = pd.concat(all_stock_data)
result.to_csv("./input/sz_result.csv")
#################################

# print(ts.get_k_data("600000"))