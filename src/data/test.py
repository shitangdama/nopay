# from DataApi import DataApi  
from config.config import data_config, trade_config
from dataapi import DataApi

api = DataApi(addr="tcp://data.tushare.org:8910")
df, msg = api.login(data_config["remote.data.username"], data_config["remote.data.password"]) 
# #  请在www.quantos.org注册用户

# symbol = '000001.SH'
fields = 'open,high,low,last,volume,pe,pb'

# # 获取实时行情
# df, msg = api.query(
#                 symbol="600832.SH, 600030.SH", 
#                 start_date="2012-10-26",
#                 end_date="2012-11-30", 
#                 fields="", 
#                 adjust_mode="post")

df, msg = api.query(
                view="lb.secDailyIndicator", 
                fields="", 
                filter="", 
                data_format='pandas')
print(df)
# print(msg)