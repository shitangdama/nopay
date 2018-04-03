from abc import abstractmethod

# 虚拟类
class DataService(object):
    # 先编写离线
    def register_context(self, context):
        self.ctx = context
    
    @abstractmethod
    def quote(self, symbol, fields=""):
        pass

    @abstractmethod
    def bar_quote(self, symbol, start_time=200000, end_time=160000,
                  trade_date=0, freq="1M", fields="", data_format="", **kwargs):
        pass
        
    @abstractmethod
    def daily(self, symbol, start_date, end_date, fields="", adjust_mode=None):
        pass
    
    @abstractmethod
    def bar(self, symbol, start_time=200000, end_time=160000, trade_date=None, freq='1M', fields=""):
        pass
    
    @abstractmethod
    def query(self, view, filter, fields):
        pass


# 关于单例模式
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class RemoteDataService(DataService):
    __metaclass__ = Singleton
    def init_from_config(self, props):
        """
        
        Parameters
        ----------
        props : dict
            Configurations used for initialization.

        Example
        -------
        {"remote.data.address": "tcp://Address:Port",
            "remote.data.username": "your username",
            "remote.data.password": "your password"}

            """
        def get_from_list_of_dict(l, key, default=None):
            res = None
            for dic in l:
                res = dic.get(key, None)
                if res is not None:
                    break
            if res is None:
                res = default
            return res

        props_default = dict()  # jutil.read_json(jutil.join_relative_path('etc/data_config.json'))
        dic_list = [props, props_default]

        address = get_from_list_of_dict(dic_list, "remote.data.address", "")
        username = get_from_list_of_dict(dic_list, "remote.data.username", "")
        password = get_from_list_of_dict(dic_list, "remote.data.password", "")
        time_out = get_from_list_of_dict(dic_list, "timeout", 60)

        print(address)

        print("\nBegin: DataApi login {}@{}".format(username, address))
        INDENT = ' ' * 4

        # 
        # 这个函数是判断当前状态
        # if self.data_api_loginned:
        #     if (address == "") or (username == "") or (password == ""):
        #         raise InitializeError("no address, username or password available!")
        #     elif ((address == self._address) and (time_out == self._timeout)
        #         and (username == self._username) and (password == self._password)):
        #         print(INDENT + "Already login as {:s}, skip init_from_config".format(username))
        #         return '0,'  # do not login with the same props again
        #     else:
        #         self.data_api.close()
        #         self.data_api = None

        # self._address = address
        # self._username = username
        # self._password = password
        # self._timeout = time_out

        # data_api = DataApi(self._address, use_jrpc=False)
        # data_api.set_timeout(timeout=self._timeout)
        # r, err_msg = data_api.login(username=self._username, password=self._password)
        # if not r:
        #     print(INDENT + "login failed: err_msg = '{}'\n".format(err_msg))
        # else:
        #     self.data_api = data_api
        #     print(INDENT + "login success \n")

        # return err_msg