
# 首先确定一个对数据封装的一个类用于处理之后的输出
# 该文件用于处理对因子的查询功能
# 主要三个功能
# 第一是保存数据，对外快捷输出，例如每日数据，


# 每日数据
class DailyDataView(object):
    def __init__(self, daily_data):
        # 数据
        self.daily_data = daily_data

        # 基础属性
        self.start = 0
        self.end = 0

        # 用于迭代记录位置的属性
        self.limit = 0

    # 这个接口主要用于初始化内部的属性
    def _init_data(self, daily_data):
        pass

    # 用于backtest对外输出下一天的信息 
    def get_next_bar(self):
        pass

    # 得到一段时间的信息，
    def get_range_bar(self, start, end):
        pass

    # 的到前几天的数据
    # 需要一个过滤数据