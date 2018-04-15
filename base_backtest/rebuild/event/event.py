# 这里重写event，原版event复用性太差
# 使用一个event核心，不在分开

from enum import Enum
# 默认的value
from collections import defaultdict

class Event(object):
    # 这个地方要不要使用kwargs
    def __init__(self, event_type, **kwargs):
        self.event_type = event_type
        self.__dict__ = kwargs


    def __str__(self):
        return str(self.__dict__)
        
    def __repr__(self):
        return ' '.join('{}:{}'.format(k, v) for k, v in self.__dict__.items())


class EventBus(object):
    def __init__(self):
        # 定义一个监听器
        self._listeners = defaultdict(list)
# 最好严格判断下类型
    def register(self, event_type, event):
        self._listeners[event_type].append(event)

    def prepend_register(self, event_type, event):
        self._listeners[event_type].insert(0, event)
    
    #  def romoveObserver(self, observer): self.__observers.remove(observer)

    def notify(self, event_type):
        for event in self._listeners[event_type]:
            print(event)


if __name__ == "__main__":
    event_manager = EventBus()
    event_1 = Event("market", name="01")
    event_2 = Event("market", name="02")
    event_3 = Event("market", name="03")
    # event_4 = Event("strategy", name="04")
    # event_5 = Event("strategy", name="05")
    # event_6 = Event("strategy", name="06")
    # event_7 = Event("portfolio", name="07")
    # event_8 = Event("portfolio", name="08")
    # event_9 = Event("portfolio", name="09")
    event_manager.register("market", event_1)
    event_manager.register("market", event_2)
    event_manager.register("market", event_3)
    # event_manager.register(event_4)
    # event_manager.register(event_5)
    # event_manager.register(event_6)
    # event_manager.register(event_7)
    # event_manager.register(event_8)
    # event_manager.register(event_9)

    event_manager.notify("market")