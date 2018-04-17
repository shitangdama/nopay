import pandas as pd

class Research(object):
    def __init__(self, data):
        self.data = dict()
        self.stock_code = []
        self._init_data(data)

    # 最好能把股票信息选出来
    def _init_data(self, data):
        data_dict = dict()
        pd_code = pd.DataFrame(data["code"].drop_duplicates()) 
        for index, row in pd_code.iterrows():
            code = str(index).zfill(6)
            self.data[code] = data[data["code"] == index]
            self.stock_code.append(code)

    def find_factor(self):
        pass

    def test(self):
        print(11111111111111)