####重构
#####对整个量化文件进行重构
将回测拆分开来
- data_api:主要处理数据的获取
- data_view:主要处理因子分析
- data_handle:主要处理原始数据变成会测数据


strategy中有一个event的策略类主要是作为manager类保存event和部分数据



在backtest内部有个循环，不停的调用stratrgy中的判断函数，
calculate_signals函数
可以扩展这个函数分割成aop
有个centext是历史数据

也就是说backtest类是喂数据，管理strategy和pm

关于bar的设计

这里将bar设计成一个工具类
暂时不设计择时
这里这里最好设计成一个通用的dataview
