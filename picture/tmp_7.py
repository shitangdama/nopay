


import pandas as pd
import tushare as ts

# 
# data = ts.get_hs300s()
# data.to_csv("./input/hs300.csv")


hs300 = pd.read_csv("./input/hs300.csv")
data = pd.read_csv("./input/sz_result.csv")

from datetime import datetime
now = datetime.now()
all_date = []
stop_stock = [600485]


def find_fator(data):

    if data.shape[0] == 0:
        return


    # 加入20日均线

    first = data.head(1)
    first_num = first.index[0]
    for index, row in data.iterrows():



        if index - first_num >= 30:
            # 判断市场活跃度
            # data_volume = data.loc[range(first_num, index),["volume"]].std()/1000
            # pro_data = data.loc[range(index-30,index),:]
            # volume_mean = pro_data["volume"].mean()

            # if data_volume["volume"] > 100 and volume_mean > 200000:
                
            close_limit = (pro_data["close"].max() - pro_data["close"].min())/10 + pro_data["close"].min()
            limit_volume = (pro_data["volume"].max() - pro_data["volume"].min())/10 + pro_data["volume"].min()
            if row["close"] < close_limit and row["volume"] < limit_volume:
                date_1 = datetime.strptime(row["date"], "%Y-%m-%d")
                if (now - date_1).days < 5:
                # 
                    all_date.append(row)



for index, row in hs300.iterrows():
    code = row["code"]
    print(code)
    sole_data = data[data["code"] == code]
    find_fator(sole_data)

print(11111111111111111111111111)
result = pd.DataFrame(all_date)

result.to_csv("./result/result_1.csv")