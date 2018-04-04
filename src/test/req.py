# from DataApi import DataApi  # 这里假设项目目录名为DataApi, 且存放在工作目录下
from dataapi.data_api import DataApi

token = "eyJhbGciOiJIUzI1NiJ9.eyJjcmVhdGVfdGltZSI6IjE1MjI0MjUxMzgwNjIiLCJpc3MiOiJhdXRoMCIsImlkIjoiMTM1NjQ1NDIxNDUifQ.eDmGunsBAch6Q4IUJJIFKl6z01esSijBHkv6U1EZHoA"

data_config = {
    "remote.data.address": "tcp://data.tushare.org:8910",
    "remote.data.username": "13564542145",
    "remote.data.password": token
}
# ['000651.SZ', '600036.SH', '600519.SH', '601318.SH']
# ['sw1', 'open_adj', 'high_adj', 'low_adj', 'close_adj', 'open', 'high', 'low', 'close', 'vwap', 'vwap_adj']

api = DataApi(addr="tcp://data.tushare.org:8910")
result, msg = api.login("13564542145", token) # 示例账户，用户需要改为自己在www.quantos.org上注册的账户
print(result)
print(msg)