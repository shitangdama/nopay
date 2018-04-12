# 这个文件是一个用来处理将数据


# 第一步先把数据读取出来
# 读取quantos的数据


# def read_hd5(file_path):

import pandas as pd
# "benchmark": "000905.SH"

def _load_h5(fp):
    h5 = pd.HDFStore(fp)
    res = dict()
    for key in h5.keys():
        res[key] = h5.get(key)
    h5.close()
    return res


# h5 = pd.HDFStore('./input/data.hd5')

# res = dict()
# for key in h5.keys():
#     res[key] = h5.get(key)
    
# h5.close()

# print(res)

# 日期数据
data_d = dic.get('/data_d', None)
data_q = dic.get('/data_q', None)
_data_benchmark = dic.get('/data_benchmark', None)
_data_inst = dic.get('/data_inst', None)
data_custom = dic.get('/data_custom', None)