


# 這裏

# 合并成一个

# 传入是当天的数据

# 这里要注意的是
# 第一要存储历史数据


class Strategy(object):
    pass

# 这里的两个策略

# AlphaStrategy是不直接买卖的，是提供ic因子给pm，由pm进行择时策略进行卖出

# EventDrivenStrategy是直接进行买卖，算是择时策略

class AlphaStrategy(Strategy):
    pass



# 在多因子情况下，考虑两个时刻
# 一个开盘价，一个收盘价
class EventDrivenStrategy(Strategy):
    pass