#encoding: UTF-8
import json from time 
import strftime
import pandas as pd
from pandas.io.sql import *
from datetime import *
import tushare as ts
from tushare.stock import cons as ct
from sqlalchemy import *
from sqlalchemy.dialects.postgresql import *
import osclass 

MySQLApi(object):    
    today = datetime.today()    
    today_year = datetime.today().year    
    today_ISO = datetime.today().date().isoformat()    
    today_8digit = today_ISO.replace("-", "")    
    quarter_list = [1, 2, 3, 4]    
    year = 2013    
    engine_stock_fundamentals = create_engine("mysql+mysqldb://root:good@localhost:3306/TUSHARE_STOCK_FUNDAMENTALS", encoding='utf-8', echo=False)    
    engine_stock_d1 = create_engine("mysql+mysqldb://root:good@localhost:3306/TUSHARE_STOCK_D1", encoding='utf-8', echo=False)
    engine_stock_m1 = create_engine("mysql+mysqldb://root:good@localhost:3306/TUSHARE_STOCK_M1", encoding='utf-8', echo=False)    
    warning_list = pd.DataFrame(columns=['return code', 'description', 'additional info 1'])    
def __init__(self):
    self.engine_stock_fundamentals.connect()        
    self.engine_stock_d1.connect()        
    self.engine_stock_m1.connect()    
    #----------------------------------------------------------------------    
    # directly download - Market data    
def download_trade_cal(self):        
    """        
    get the trade calendar from datayes via tushare_download api        
    """        
    dtype = {            
        'seq': Integer,            
        'exchangeCD': VARCHAR(10),            
        'calendarDate': VARCHAR(10),            
        'isOpen': Integer,            
        'prevTradeDate': VARCHAR(10),            
        'isWeekEnd': Integer,            
        'isMonthEnd': Integer,            
        'isQuarterEnd': Integer,            
        'isYearEnd': Integer        
    }        
    token = '16abc96618f0d35bbf703e60011f2dcfadd916b2a46f1c3623f804ac133eef24'        
    print('Downloading Trade Calendar...')        
    total = 0        
    datayes_df = DataFrame([token], columns=['token'])        
    datayes_df.to_csv(ct.TOKEN_F_P, index=False)        
    mt = ts.Master()        
    stock_data = mt.TradeCal(exchangeCD='XSHG',                                 
    beginDate='20000101',                                 
    endDate='20161231',                    
    field='exchangeCD,calendarDate,isOpen,prevTradeDate,isWeekEnd,isMonthEnd,isQuarterEnd,isYearEnd')        
    if stock_data is not None:            
        total = total + len(stock_data)            
        print('Total records: ' + str(total))            
        stock_data.to_sql(name='StockTradeCal', con=self.engine_stock_fundamentals, if_exists='replace', index=False, dtype=dtype)        
    else:            
        warning_code = pd.DataFrame({'return code':1, 'description':'trade calendar download failed'})            
        self.warning_list = self.warning_list.append(warning_code)            
        print('Download Trade Calendar Failed.')        
        print('download_trade_cal successful ' + str(total))

def download_stock_D1(self):        
    print('downloading the stock daily info...')        
    stock_basics = ts.get_today_all()        
    stock_list = sorted(list(stock_basics.code.values))        
    print(stock_list)        
    total = 0        
    file_path = '/Users/yanghui/Documents/tushare/StockDaily/'        
    for stock in stock_list:            
        filename = stock + '.csv'            
        try:                
            stock_data = pd.read_csv(file_path + filename)                
            #stock_data.drop(['code'], inplace=True, axis=1, errors='ignore')                
            #stock_data.sort_values(by='date', ascending=False, inplace=True)                
            # #start_date = stock_data.head(1).index.value                
            # #end_date = self.today_ISO                
            #stock_data_latest = ts.get_k_data(stock, autype=None, start=start_date, end=end_date)     
            #stock_data = stock_data.append(stock_data_latest)            
        except:                
            stock_data = pd.DataFrame([])            
            print('downloading-' + stock + ' for the lost data...before count:' + str(len(stock_data)))
        year = 1990            
        while year <= self.today_year:                
            start_date = str(year) + '-01-01'                
            end_date = str(year) + '-12-31'                
            try:                    
                stock_data_latest = ts.get_k_data(stock, autype=None, start=start_date, end=end_date)
                stock_data = stock_data.append(stock_data_latest)                
            except:                    
                pass                
            year = year + 1            
            #stock_data['code'] = str(stock).zfill(6)            
            #stock_data.index = stock_data.index.map(lambda x: strftime("%Y-%m-%d", x))            
            stock_data.drop_duplicates(subset=['date'], keep='first', inplace=True)            
            stock_data.sort_values(by='date', ascending=False, inplace=True)            
            stock_data.set_index(keys=['date'], drop=True, inplace=True, append=False)            
            stock_data.to_csv(file_path + filename)            
            print('downloading-' + stock + ' for the lost data...after count:' + str(len(stock_data)))        
            print('download_stock_D1 successful ' + str(total))    
    def download_stock_D1_qfq(self):        
        print('downloading the stock qfq daily info...')        
        stock_basics = ts.get_today_all()        
        stock_list = sorted(list(stock_basics.code.values))        
        print(stock_list)       
        total = 0        
        file_path = '/Users/yanghui/Documents/tushare/StockDaily_qfq/'        
        for stock in stock_list:            
            filename = stock + '.csv'            
            try:                
                stock_data = pd.read_csv(file_path + filename)                
                #stock_data.drop(['code'], inplace=True, axis=1, errors='ignore')                
                #stock_data.sort_values(by='date', ascending=False, inplace=True)                
                #start_date = stock_data.head(1).index.value              
                #end_date = self.today_ISO                
                #stock_data_latest = ts.get_k_data(stock, autype=None, start=start_date, end=end_date) 
                #stock_data = stock_data.append(stock_data_latest)            
            except:                
                stock_data = pd.DataFrame([])            
                print('downloading-' + stock + ' for the lost data...before count:' + str(len(stock_data)))
                year = 1990            
                while year <= self.today_year:                
                    start_date = str(year) + '-01-01'                
                    end_date = str(year) + '-12-31'                
                    try:                    
                        stock_data_latest = ts.get_k_data(stock, autype='qfq', start=start_date, end=end_date)
                        stock_data = stock_data.append(stock_data_latest)                
                    except:                    
                        pass                
                    year = year + 1            
                    #stock_data['code'] = str(stock).zfill(6)            
                    #stock_data.index = stock_data.index.map(lambda x: strftime("%Y-%m-%d", x))            
                    stock_data.drop_duplicates(subset=['date'], keep='first', inplace=True)            
                    stock_data.sort_values(by='date', ascending=False, inplace=True)            
                    stock_data.to_csv(file_path + filename)            
                    print('downloading-' + stock + ' for the lost data...after count:' + str(len(stock_data)))
                    print('download_stock_D1_qfq successful ' + str(total))    
                    # TODO: this function has not done yet, need to do later when needed.    
    def download_stock_M1(self, start='2016-01-01', end='2016-10-01'):        
        dtype = {            
            'code': VARCHAR(6),            
            'date': VARCHAR(20),            
            'time': VARCHAR(20),            
            'price': DECIMAL(20,5),            
            'change': VARCHAR(10),            
            'volume': DECIMAL(20,5),            
            'amount': DECIMAL(20,5),            
            'type': VARCHAR(10)        
            }        
            #"""        
            # #download the stock info        
            #"""        
            stock_data_all = pd.DataFrame(columns=['code','date','time','price','change','volume','amount','type']) 
            print('downloading the stock daily info...')
            stock_data = ts.get_stock_basics()        
            stock_list = sorted(list(stock_data.index.values))        
            stock_term = ts.get_terminated()        
            stock_suspend = ts.get_suspended()        
            stock_term_suspend = stock_term.append(stock_suspend)        
            stock_term_suspend_list = sorted(list(stock_term_suspend.code.values))        
            stock_list_all = stock_list + stock_term_suspend_list        
            print(stock_list_all)        
            total = 0        
            start_date = datetime.strptime(start,'%Y-%m-%d')        
            end_date = datetime.strptime(end,'%Y-%m-%d')        
            for stock in stock_list:            
                date = start_date            
                print('Now downloading stock: ' + stock)            
                while end_date >= date >= start_date:                
                    date_str = date.date().isoformat()                
                    stock_data = ts.get_tick_data(code=stock,date=date_str,pause=1)                
                    if (stock_data is not None) and (stock_data.price is not None):                    
                        total = total + len(stock_data)                    
                        stock_data['code'] = stock                    
                        stock_data['date'] = date_str                    
                        stock_data_all = stock_data_all.append(stock_data)                
                    else:                    
                        warning_code = pd.DataFrame(columns={'return code': stock, 'description': 'download m1 failed:'})               
                        self.warning_list = self.warning_list.append(warning_code)                
                        date = date + timedelta(1)            
                        stock_data.to_sql(name=stock, con=self.engine_stock_m1, if_exists='replace',              
                            index=False,                              
                            index_label='date',                              
                            dtype=dtype                              
                            )        
                        print('download_stock_M1 successful ' + str(total))        
                        # ----------------------------------------------------------------------        
                        # directly get methods - Fundamental Data    
    def download_stock_basics(self):        
        """        
        code,代码        
        name,名称        
        industry,所属行业        
        area,地区        
        pe,市盈率        
        outstanding,流通股本        
        totals,总股本(万)        
        totalAssets,总资产(万)        
        liquidAssets,流动资产        
        fixedAssets,固定资产        
        reserved,公积金        
        reservedPerShare,每股公积金        
        eps,每股收益        
        bvps,每股净资        
        pb,市净率        
        timeToMarket,上市日期        
        """        
        dtype = {            
            'code': VARCHAR(6),            
            'name': VARCHAR(20),            
            'industry': VARCHAR(20),            
            'area': VARCHAR(20),            
            'pe': DECIMAL(20,5),            
            'outstanding': DECIMAL(20,5),            
            'totals': DECIMAL(20,5),            
            'totalAssets': DECIMAL(20,5),            
            'liquidAssets': DECIMAL(20,5),            
            'fixedAssets': DECIMAL(20,5),            
            'reserved': DECIMAL(20,5),            
            'reservedPerShare': DECIMAL(20,5),            
            'eps': DECIMAL(20,5),            
            'bvps': DECIMAL(20,5),            
            'pb': DECIMAL(20,5),            
            'timeToMarket': VARCHAR(20)        
        }        
        print('downloading the stock basic info...')        
        total = 0        
        stock_data = ts.get_stock_basics()        
        if stock_data is not None:            
            print('Now downloading stock basics, total records:' + str(len(stock_data)))            
            total = total + len(stock_data)            
            stock_data.to_sql(name='StockBasics', con=self.engine_stock_fundamentals, if_exists='replace',
                                                index=True,
                                                index_label='code',                                    
                                                dtype=dtype                                    
                                                )        
        else:            
            warning_code = pd.DataFrame({'return code': ['for all stocks'], 'description': ['stock basics download failed']})            
            self.warning_list = self.warning_list.append(warning_code)        
            #download the stocks which is terminated or suspended        
            #返回值说明：        
            #code：股票代码        
            #name：股票名称        
            #oDate:上市日期        
            #tDate:终止上市日期        
            #"""        
                dtype = {            
                    'seq': Integer,            
                    'code': VARCHAR(6),            
                    'name': VARCHAR(20),            
                    'oDate': VARCHAR(20),            
                    'tDate': VARCHAR(20)        
                }        
                total = 0        
                stock_term = ts.get_terminated()        
                if stock_term is not None:            
                    stock_suspend = ts.get_suspended()            
                    if stock_suspend is not None:                
                        stock_data = stock_term.append(stock_suspend)                
                    
                        stock_data.to_sql(name='StockTermSuspend', con=self.engine_stock_fundamentals, if_exists='replace',
                                                    index=False,                                  
                                                    dtype=dtype                                  
                                                    )            
                        else:                
                            warning_code = pd.DataFrame(columns={'return code': 1, 'description': 'stock suspend download failed'})
                            self.warning_list = self.warning_list.append(warning_code)        
                    else:            
                        warning_code = pd.DataFrame(columns={'return code': 1, 'description': 'stock term download failed'})            
                        self.warning_list = self.warning_list.append(warning_code)        
                        total = total + len(stock_data)        
                        print('download_stock_term/suspend successful total records:  ' + str(total))    
    def download_stock_basics_csv(self):        
        """        
        code,代码       
        name,名称        
        industry,所属行业        
        area,地区        
        pe,市盈率        
        outstanding,流通股本        
        totals,总股本(万)        
        totalAssets,总资产(万)        
        liquidAssets,流动资产        
        fixedAssets,固定资产        
        reserved,公积金        
        reservedPerShare,每股公积金        
        eps,每股收益        
        bvps,每股净资        
        pb,市净率        
        timeToMarket,上市日期        
        """        
        print('downloading the stock basic info...')        
        total = 0        
        stock_data = ts.get_stock_basics()        
        if stock_data is not None:            
            print('Now downloading stock basics, total records:' + str(len(stock_data)))            
            stock_data['order_book_id'] = stock_data.index.map(lambda x: x + '.XSHG' if x >= '600000' else x + '.XSHE')            
            filename = 'StockBasics'            
            stock_data.to_csv('/Users/yanghui/Documents/tushare_download/StockFundamentals/' + filename + '.csv',encoding='GBK')        
        else:            
            warning_code = pd.DataFrame({'return code': ['for all stocks'], 'description': ['stock basics download failed']})            
            self.warning_list = self.warning_list.append(warning_code)        
            #download the stocks which is terminated or suspended        
            #返回值说明：        
            #code：股票代码        
            #name：股票名称        
            #oDate:上市日期        
            #tDate:终止上市日期        
            #"""        
        dtype = {            
            'seq': Integer,            
            'code': VARCHAR(6),            
            'name': VARCHAR(20),            
            'oDate': VARCHAR(20),            
            'tDate': VARCHAR(20)        
            }        
        total = 0        
        stock_term = ts.get_terminated()        
        if stock_term is not None:            
            stock_suspend = ts.get_suspended()            
            if stock_suspend is not None:                
                stock_data = stock_term.append(stock_suspend)                
                stock_data.to_sql(name='StockTermSuspend', con=self.engine_stock_fundamentals, if_exists='replace',
                                                  index=False,                                  
                                                  dtype=dtype                                  
                                                  )            
            else:                
                warning_code = pd.DataFrame(columns={'return code': 1, 'description': 'stock suspend download failed'})                
                self.warning_list = self.warning_list.append(warning_code)        
        else:            
            warning_code = pd.DataFrame(columns={'return code': 1, 'description': 'stock term download failed'})
            self.warning_list = self.warning_list.append(warning_code)        
            total = total + len(stock_data)        
            print('download_stock_term/suspend successful total records:  ' + str(total))    
    def download_report_data(self,year_from=2013):        
        """        
        code,代码        
        name,名称        
        eps,每股收益        
        eps_yoy,每股收益同比(%)        
        bvps,每股净资产        
        roe,净资产收益率(%)        
        epcf,每股现金流量(元)        
        net_profits,净利润(万元)        
        profits_yoy,净利润同比(%)        
        distrib,分配方案        
        report_date,发布日期        
        """        
        dtype = {            
            'code': VARCHAR(6),            
            'name': VARCHAR(20),            
            'eps': DECIMAL(20, 5),            
            'eps_yoy': DECIMAL(20, 5),            
            'bvps': DECIMAL(20, 5),            
            'roe': DECIMAL(20, 5),            
            'epcf': DECIMAL(20, 5),            
            'net_profits': DECIMAL(20, 5),            
            'profits_yoy': DECIMAL(20, 5),            
            'distrib': VARCHAR(40),            
            'report_date': VARCHAR(20),            
            'year': Integer,            
            'quarter': Integer,        
        }        
        print('Now downloading stock report data...')        
        year = year_from        
        stock_data_all = pd.DataFrame(columns=['code','name','eps','eps_yoy','bvps','roe','epcf','net_profits','profits_yoy','distrib','report_date','year','quarter'])       
        while year_from <= year <= self.today.year:            
            for quarter in self.quarter_list:                
                stock_data = ts.get_report_data(year,quarter)                
                if stock_data is not None:                    
                    print('Total records for year-quarter ' + str(year) + '-' + str(quarter) +' : ' + str(len(stock_data)))                    stock_data['year'] = year                    
                    stock_data['quarter'] = quarter                    
                    stock_data_all = stock_data_all.append(stock_data,ignore_index=True)                
                else:                    
                    warning_code = pd.DataFrame({'return code': [str(year)+str(quarter)], 'description': ['stock report data download failed']})                    
                    self.warning_list = self.warning_list.append(warning_code)            
                    year = year + 1        
                    total_count = len(stock_data_all)        
                    stock_data_all.to_sql(name='StockReportData', con=self.engine_stock_fundamentals,
                                                  if_exists='append',                              
                                                  index=False,                             
                                                  dtype=dtype                              
                                                  )        
                    print('Download completed! Total records: ' + str(total_count))    
    def download_profit_data(self,year_from=2013):        
        """        
        code,代码        
        name,名称        
        roe,净资产收益率(%)        
        net_profit_ratio,净利率(%)        
        gross_profit_rate,毛利率(%)        
        net_profits,净利润(万元)        
        eps,每股收益       
        business_income,营业收入(百万元)        
        bips,每股主营业务收入(元)        
        """        
        dtype = {            
            'code': VARCHAR(6),            
            'name': VARCHAR(20),            
            'roe': DECIMAL(20, 5),            
            'net_profit_ratio': DECIMAL(20, 5),            
            'gross_profit_rate': DECIMAL(20, 5),            
            'net_profits': DECIMAL(20, 5),            
            'eps': DECIMAL(20, 5),            
            'business_income': DECIMAL(20, 5),            
            'bips': DECIMAL(20, 5),            
            'year': Integer,            
            'quarter': Integer        
        }        
        print('Now downloading stock profit data...')        
        stock_data_all = pd.DataFrame(columns=['code','name','roe','net_profit_ratio','gross_profit_rate','net_profits','eps','business_income','bips'])        year = year_from        while year_from <= year <= self.today.year:            
        for quarter in self.quarter_list:                
            stock_data = ts.get_profit_data(year,quarter)               
            if stock_data is not None:                    
                print('Total records for year-quarter ' + str(year) + '-' + str(quarter) +' : ' + str(len(stock_data)))                    
                stock_data['year'] = year                    
                stock_data['quarter'] = quarter                    
                stock_data_all = stock_data_all.append(stock_data,ignore_index=True)                
            else:                    
                warning_code = pd.DataFrame({'return code': [str(year)+str(quarter)], 'description': ['stock profit data download failed'] })                    
                self.warning_list = self.warning_list.append(warning_code)            
                year = year + 1        
                total_count = len(stock_data_all)        
                stock_data_all.to_sql(name='StockProfitData', con=self.engine_stock_fundamentals,
                                              if_exists='replace',                              
                                              index=False,                              
                                              dtype=dtype                              
                                              )        
                print('Download completed! Total records: ' + str(total_count))    
    def download_operation_data(self,year_from=2013):        
        """        
        code,代码        
        name,名称        
        arturnover,应收账款周转率(次)        
        arturndays,应收账款周转天数(天)        
        inventory_turnover,存货周转率(次)        
        inventory_days,存货周转天数(天)        
        currentasset_turnover,流动资产周转率(次)        
        currentasset_days,流动资产周转天数(天)        
        """        
        dtype = {            
            'code': VARCHAR(6),            
            'name': VARCHAR(20),            
            'roe': DECIMAL(20, 5),            
            'arturnover': DECIMAL(20, 5),            
            'arturndays': DECIMAL(20, 5),            
            'inventory_turnover': DECIMAL(20, 5),            
            'inventory_days': DECIMAL(20, 5),            
            'currentasset_turnover': DECIMAL(20, 5),            
            'currentasset_days': DECIMAL(20, 5),            
            'year': Integer,            
            'quarter': Integer        }       
        print('Now downloading stock operation data...')        
        year = year_from        
        stock_data_all = pd.DataFrame(columns=['code','name','roe','arturnover','arturndays',
                                                                'inventory_turnover','inventory_days',
                                                                'currentasset_turnover','currentasset_days'])
        while year_from <= year <= self.today.year:            
            for quarter in self.quarter_list:                
                stock_data = ts.get_operation_data(year,quarter)                
                if stock_data is not None:                    
                    print('Total records for year-quarter ' + str(year) + '-' + str(quarter) + ' : ' +
                                                  str(len(stock_data)))                    
                                                  stock_data['year'] = year                    
                                                  stock_data['quarter'] = quarter                    
                                                  stock_data_all = stock_data_all.append(stock_data,
                                                  ignore_index=True)                
                else:                    
                    warning_code = pd.DataFrame({'return code': [str(year)+str(quarter)], 'description': ['stock operatioon data download failed']})                    
                    self.warning_list = self.warning_list.append(warning_code)            
                    year = year + 1        
                    total_count = len(stock_data_all)        
                    stock_data_all.to_sql(name='StockOperationData', con=self.engine_stock_fundamentals,
                                                  if_exists='replace',                              
                                                  index=False,                              
                                                  dtype=dtype                              
                                                  )        
                    print('Download completed! Total records: ' + str(total_count))    
                    def download_growth_data(self,year_from=2013):        
                    """        
                    code,代码        
                    name,名称        
                    mbrg,主营业务收入增长率(%)        
                    nprg,净利润增长率(%)        
                    nav,净资产增长率        
                    targ,总资产增长率        
                    epsg,每股收益增长率        
                    seg,股东权益增长率        
                    """        
                    dtype = {            
                        'code': VARCHAR(6),            
                        'name': VARCHAR(20),            
                        'mbrg': DECIMAL(20, 5),            
                        'nprg': DECIMAL(20, 5),            
                        'nav': DECIMAL(20, 5),            
                        'targ': DECIMAL(20, 5),            
                        'epsg': DECIMAL(20, 5),            
                        'seg': DECIMAL(20, 5),            
                        'year': Integer,            
                        'quarter': Integer       
                    }        
                    print('Now downloading stock growth data...')        
                    year = year_from        stock_data_all = pd.DataFrame(columns=['code','name','mbrg','nprg','nav',                                                         'targ','epsg','seg'])        while year_from <= year <= self.today.year:            for quarter in self.quarter_list:                stock_data = ts.get_growth_data(year,quarter)                if stock_data is not None:                    print('Total records for year-quarter ' + str(year) + '-' + str(quarter) + ' : ' +                              str(len(stock_data)))                    stock_data['year'] = year                    stock_data['quarter'] = quarter                    stock_data_all = stock_data_all.append(stock_data,ignore_index=True)                else:                    warning_code = pd.DataFrame({'return code': [str(year)+str(quarter)], 'description': ['stock growth data download failed']})                    self.warning_list = self.warning_list.append(warning_code)            year = year + 1        total_count = len(stock_data_all)        stock_data_all.to_sql(name='StockGrowthData', con=self.engine_stock_fundamentals,                              if_exists='append',                              index=False,                              dtype=dtype                              )        print('Download completed! Total records: ' + str(total_count))    def download_debtpaying_data(self,year_from=2013):        """        code,代码        name,名称        currentratio,流动比率        quickratio,速动比率        cashratio,现金比率        icratio,利息支付倍数        sheqratio,股东权益比率        adratio,股东权益增长率        """        dtype = {            'code': VARCHAR(6),            'name': VARCHAR(20),            'currentratio': VARCHAR(20),            'quickratio': VARCHAR(20),            'cashratio': VARCHAR(20),            'icratio': VARCHAR(20),            'sheqratio': VARCHAR(20),            'adratio': VARCHAR(20),            'year': Integer,            'quarter': Integer        }        print('Now downloading stock debt paying data...')        year = year_from        stock_data_all = pd.DataFrame(columns=['code','name','currentratio','quickratio','cashratio',                                                         'icratio','sheqratio','adratio'])        while year_from <= year <= self.today.year:            for quarter in self.quarter_list:                stock_data = ts.get_debtpaying_data(year,quarter)                if stock_data is not None:                    print('Total records for year-quarter ' + str(year) + '-' + str(quarter) + ' : ' +                              str(len(stock_data)))                    stock_data['year'] = year                    stock_data['quarter'] = quarter                    stock_data_all = stock_data_all.append(stock_data,ignore_index=True)                else:                    warning_code = pd.DataFrame({'return code': [str(year)+str(quarter)], 'description': ['stock debt paying data download failed']})                    self.warning_list = self.warning_list.append(warning_code)            year = year + 1        total_count = len(stock_data_all)        stock_data_all.to_sql(name='StockDebtPayingData', con=self.engine_stock_fundamentals,                                if_exists='replace',                                index=False,                                dtype=dtype                                )        print('Download completed! Total records: ' + str(total_count))    def download_cashflow_data(self,year_from=2013):        """        code,代码        name,名称        cf_sales,经营现金净流量对销售收入比率        rateofreturn,资产的经营现金流量回报率        cf_nm,经营现金净流量与净利润的比率        cf_liabilities,经营现金净流量对负债比率        cashflowratio,现金流量比率        """        dtype = {            'code': VARCHAR(6),            'name': VARCHAR(20),            'cf_sales': DECIMAL(20, 5),            'rateofreturn': DECIMAL(20, 5),            'cf_nm': DECIMAL(20, 5),            'cf_liabilities': DECIMAL(20, 5),            'cashflowratio': DECIMAL(20, 5),            'year': Integer,            'quarter': Integer        }        print('Now downloading stock cash flow data...')        year = year_from        stock_data_all = pd.DataFrame(columns=['code','name','cf_sales','rateofreturn','cf_nm',                                                         'cf_liabilities','cashflowratio'])        while year_from <= year <= self.today.year:            for quarter in self.quarter_list:                stock_data = ts.get_cashflow_data(year,quarter)                if stock_data is not None:                    print('Total records for year-quarter ' + str(year) + '-' + str(quarter) + ' : ' +                              str(len(stock_data)))                    stock_data['year'] = year                    stock_data['quarter'] = quarter                    stock_data_all = stock_data_all.append(stock_data,ignore_index=True)                else:                    warning_code = pd.DataFrame(columns={'return code': year, 'description': 'stock cashflow paying data download failed' })                    self.warning_list = self.warning_list.append(warning_code)            year = year + 1        total_count = len(stock_data_all)        stock_data_all.to_sql(name='StockCashFlowData', con=self.engine_stock_fundamentals,                              if_exists='replace',                              index=False,                              dtype=dtype                              )        print('Download completed! Total records: ' + str(total_count))    def download_industry_classified(self):        """        code,代码        name,名称        c_name：行业名称        """        dtype = {            'code': VARCHAR(6),            'name': VARCHAR(20),            'c_name': VARCHAR(20)        }        print('Now downloading industry classified data...')        stock_data = ts.get_industry_classified()        if stock_data is not None:            stock_data.to_sql(name='StockIndustryClassified', con=self.engine_stock_fundamentals,                                          if_exists='replace',                                          index=False,                                          dtype=dtype                                          )        else:            warning_code = pd.DataFrame({'return code': 1, 'description': 'stock industry classified data download failed'})            self.warning_list = self.warning_list.append(warning_code)    def download_st_classified_CSV(self):        total = 0        print('downloading the st classified stock to csv...')        stock_data = ts.get_st_classified()        if stock_data is not None:            total = total + len(stock_data)            stock_data['order_book_id'] = stock_data['code'].map(lambda x: x + '.XSHG' if x >= '600000' else x + '.XSHE')            filename = 'ST_classified'            stock_data.to_csv('/Users/yanghui/Documents/tushare_download/StockFundamentals/' + filename + '.csv',encoding='GBK')        else:            warning_code = pd.DataFrame({'return code': 1, 'description': 'download st classified failed:'})            self.warning_list = self.warning_list.append(warning_code)        print('download_st_classified successful ' + str(total))    def download_news(self):        print('downloading the news to csv...')        stock_basics = ts.get_stock_basics()        stock_list = sorted(list(stock_basics.index.values))        print(stock_list)        total = 0        for stock in stock_list:            if stock not in ['000031','000065','000069','000150','000403','000409','000503','000505','000507','000510',                             '000524','000536','000537','000544','000546','000567','000601','000625','000637','000679',                             '000683','000690','000693','000718','000721','000723','000738','000783','000796','000801',                             '000809','000810','000836','000860','000882','000917','000925','000937','000952','000970',                             '000979','000987','000989','002007']:                print(stock)                stock_data = ts.get_notices(code=stock)            if stock_data is not None:                print('Now downloading stock: ' + stock + ', Total records:' + str(len(stock_data)))                total = total + len(stock_data)                stock_data['code'] = stock                stock_data['order_book_id'] = stock_data['code'].map(                    lambda x: x + '.XSHG' if x >= '600000' else x + '.XSHE')                if os.path.exists('/Users/yanghui/Documents/tushare_download/StockFundamentals/News.csv'):                    stock_data.to_csv('/Users/yanghui/Documents/tushare_download/StockFundamentals/News.csv', mode='a',                                      header=None,encoding='GBK')                else:                    stock_data.to_csv('/Users/yanghui/Documents/tushare_download/StockFundamentals/News.csv',encoding='GBK')            else:                warning_code = pd.DataFrame({'return code': 1, 'description': 'download news failed:'})                self.warning_list = self.warning_list.append(warning_code)            print('download_news successful for ' + stock + ': ' + str(total))    def download_index(self):        total = 0        print('downloading the stock index to csv...')        start_year = 1991        while start_year <= self.today_year:            start_date = str(start_year) + '-01-01'            end_date = str(start_year) + '-12-31'            stock_data = ts.get_h_data('399001', start=start_date, end=end_date,index=True)            stock_data['code'] = '399001'            if os.path.exists('/Users/yanghui/Documents/tushare_download/StockDaily/Index.csv'):                stock_data.to_csv('/Users/yanghui/Documents/tushare_download/StockDaily/Index.csv', mode='a',                                  header=None, encoding='GBK')            else:                stock_data.to_csv('/Users/yanghui/Documents/tushare_download/StockDaily/Index.csv', encoding='GBK')            stock_data = ts.get_h_data('000001', start=start_date, end=end_date, index=True)            stock_data['code'] = '000001'            if os.path.exists('/Users/yanghui/Documents/tushare_download/StockDaily/Index.csv'):                stock_data.to_csv('/Users/yanghui/Documents/tushare_download/StockDaily/Index.csv', mode='a',                                  header=None, encoding='GBK')            else:                stock_data.to_csv('/Users/yanghui/Documents/tushare_download/StockDaily/Index.csv', encoding='GBK')            start_year = start_year + 1        print('download_index successful ' + str(total))    def download_daily_tick(self,start='2016-06-01',end='2016-12-01'):        print('downloading the stock daily tick to csv...')        stock_basics = ts.get_stock_basics()        stock_list = sorted(list(stock_basics.index.values))        print(stock_list)        total = 0        """        load the trade calendar        """        engine_stock_fundamentals = create_engine("mysql+mysqldb://root:good@localhost:3306/TUSHARE_STOCK_FUNDAMENTALS",                                                  encoding='utf-8', echo=False)        connection = engine_stock_fundamentals.connect()        sql = "select * from StockTradeCal"        stock_trade_cal = pd.read_sql(sql, engine_stock_fundamentals)        connection.close()        trade_cal = stock_trade_cal        for stock in stock_list:            if stock >= '300153':                date = end                while date >= start:                    stock_data = ts.get_tick_data(stock, date=date, retry_count=3)                    if stock_data is not None:                        print(                        'Now downloading stock: ' + stock + ', Total records:' + str(len(stock_data)) + ' date:' + date)                        total = total + len(stock_data)                        stock_data['code'] = stock                        stock_data['date'] = date                        stock_data['order_book_id'] = stock_data['code'].map(                            lambda x: x + '.XSHG' if x >= '600000' else x + '.XSHE')                        filename = stock                        # stock_data.to_csv('/Users/yanghui/    Documents/tushare_download/StockDailyTick/' + filename + '.csv')                        if os.path.exists('/Users/yanghui/Documents/tushare_download/StockDailyTick/' + filename + '.csv'):                            stock_data.to_csv('/Users/yanghui/Documents/tushare_download/StockDailyTick/' + filename + '.csv',                                          mode='a', header=None, encoding='GBK')                        else:                            stock_data.to_csv('/Users/yanghui/Documents/tushare_download/StockDailyTick/' + filename + '.csv')                    else:                        warning_code = pd.DataFrame(                            columns={'return code': stock, 'description': 'download failed:' + stock})                        self.warning_list = self.warning_list.append(warning_code)                    prev_date_df = trade_cal[trade_cal.calendarDate == date]                    prev_date = prev_date_df.iloc[0]['prevTradeDate']                    date = prev_date        print('download_stock_daily_tick successful ' + str(total))
