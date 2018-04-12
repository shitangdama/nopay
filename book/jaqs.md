###阅读jaqs源码

ds = RemoteDataService()
ds.init_from_config(data_config)

在data文件中的dataservice文件


def init_from_config(self, props):
函数是初始化

props = {'start_date': 20170101, 'end_date': 20180330, 'universe': '000905.SH',
            'fields': ('turnover,float_mv,close_adj,pe,pb'),
            'freq': 1}
dv.init_from_config(props, ds)


这个函数最终要
dv.prepare_data()
看看主要做了什么