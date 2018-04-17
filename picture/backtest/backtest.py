class Backtest(object):

    def __init__(self, data):
        self.data = data
        # 交易信息
        self.trade_plot = []
        self.trade_income = []
        # 当前订单
        self.orders = []
        # 所有收入
        self.income = 0

        # 止赢止损
        self.stop_trade_value = 0.012

        # 初始资金
        self.money = 100000


    def test_run_backtest(self):
        i = 0
        while True:
            

            if self.jedge_latest_day(self.data, i):
                pass
            else:
                break

            # if
            # 止损函数
            self.stop_trade(i)


            # 从第二个数据开始
            if i > 0:
                pro_ma5 = self.data.ix[i-1]["ma5"]
                pro_ma50 = self.data.ix[i-1]["ma50"]
                now_ma5 = self.data.ix[i]["ma5"]
                now_ma50 = self.data.ix[i]["ma50"]
                now_data = self.data.ix[i]

                if pro_ma5 < pro_ma50 and now_ma5 > now_ma50:
                    # 在这里买入
                    now_data["order"] = 1
                    now_data["income"] = 0
                    now_data = self.buy(now_data)
                    self.orders.append(now_data)
                    self.trade_plot.append(now_data)

                if pro_ma5 > pro_ma50 and now_ma5 < now_ma50:
                    for order in self.orders:
                        now_data["order"] = 2
                        one_income = now_data["close"] - order["close"]
                        now_data["income"] = one_income
                        self.income = self.income + one_income
                        now_data["all_income"] = self.income
                        
                        self.trade_income.append(one_income)
                        self.orders.remove(order)


                        now_data = self.sell(order["order_num"], now_data)
                        self.trade_plot.append(now_data)

            i = i + 1


    def stop_trade(self, i):
        now_data = self.data.ix[i]
        for order in self.orders:

            tmp = (now_data["close"] - order["trade"])/order["close"] <= -1*self.stop_trade_value
            if tmp:
                now_data["order"] = 3
                one_income = now_data["close"] - order["close"]
                now_data["income"] = one_income
                self.income = self.income + one_income
                now_data["all_income"] = self.income
                self.trade_income.append(one_income)


                now_data = self.sell(order["order_num"], now_data)
                self.trade_plot.append(now_data)
                self.orders.remove(order)

            else:
                            # 判断之赢
            # 如果该订单存在，就更新他的trade
                order["trade"] = now_data["close"]

    def buy(self, now_data):
        now_data["order_num"] = self.money//now_data["close"]
        self.money = self.money - (now_data["order_num"] * now_data["close"])
        return now_data

    def sell(self, order_num, now_data):
        self.money = self.money + (order_num * now_data["close"])
        return now_data

    def get_data(self):
        return self.data

    def jedge_latest_day(self, data, i):
        if data.shape[0] < i+1:
            return False
        else:
            return True