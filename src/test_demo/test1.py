# from __future__ import print_function
# from __future__ import absolute_import
import time
import numpy as np
import pandas as pd

# import jaqs.trade.analyze as ana
from test_demo.rjaqs.data.dataservice import RemoteDataService
# from jaqs.data import DataView

from test_demo.config.config import data_config, trade_config

# def test_import():
#     print(data_config)  
dataview_dir_path = './output/test/dataview'
backtest_result_dir_path = './output/Graham'

def date_test():
    ds = RemoteDataService()
    ds.init_from_config(data_config)




# ds = RemoteDataService()
# ds.init_from_config(data_config)
# dv = DataView()

# props = {'start_date': 20171001, 'end_date': 20180330, 'universe': '000905.SH',
#             'fields': ('tot_cur_assets,tot_cur_liab,inventories,pre_pay,deferred_exp,'
#                     'eps_basic,ebit,pe,pb,float_mv,sw1'),
#             'freq': 1}

# dv.init_from_config(props, ds)
# dv.prepare_data()

# dv.save_dataview(folder_path=dataview_dir_path)
    
    # factor_formula = 'pe < 30'
    # dv.add_formula('pe_condition', factor_formula, is_quarterly=False)
    # factor_formula = 'pb < 3'
    # dv.add_formula('pb_condition', factor_formula, is_quarterly=False)
    # factor_formula = 'Return(eps_basic, 4) > 0'
    # dv.add_formula('eps_condition', factor_formula, is_quarterly=True)
    # factor_formula = 'Return(ebit, 4) > 0'
    # dv.add_formula('ebit_condition', factor_formula, is_quarterly=True)
    # factor_formula = 'tot_cur_assets/tot_cur_liab > 2'
    # dv.add_formula('current_condition', factor_formula, is_quarterly=True)
    # factor_formula = '(tot_cur_assets - inventories - pre_pay - deferred_exp)/tot_cur_liab > 1'
    # dv.add_formula('quick_condition', factor_formula, is_quarterly=True)
    
    # dv.add_formula('mv_rank', 'Rank(float_mv)', is_quarterly=False)
    
