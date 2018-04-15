# 重写各类母选股法
# 1. pe ratio < 15 
# 2. pb ratio < 1.5
# 3. inc_earning_per_share > 0
# 4. inc_profit_before_tax > 0
# 5. current_ratio > 2
# 6. quick_ratio > 1
# 市盈率（pe ratio）低于 20
# 市净率（pb ratio）低于 2
# 同比每股收益增长率（inc_earning_per_share）大于 0
# 税前同比利润增长率（inc_profit_before_tax）大于 0
# 流动比率（current_ratio）大于 2
# 速动比率（quick_ratio）大于 1


import tushare as ts

# basics_data = ts.get_stock_basics()

# data_adj =  basics_data[(basics_data["pe"] < 15) & (basics_data["pb"] > 1.5) ]

# print(data_adj.head(1))

data = ts.get_report_data(2014,3)

print(data.loc[:, ["code", "name", "eps_yoy"]])