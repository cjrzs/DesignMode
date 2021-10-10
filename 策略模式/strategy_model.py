from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Context:
    """定义客户端接口"""

    def __init__(self, strategy: Strategy):
        """
        在Context中通过初始化函数来接收策略
        :param strategy:
        """
        self.__strategy = strategy

    @property
    def strategy(self):
        """
        维护具体的策略
        :return:
        """
        return self.__strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        """
        在策略模式中，应该支持动态切换策略
        :param strategy:
        :return:
        """
        self.__strategy = strategy

    def do_something(self):
        """
        执行不同的策略
        :return:
        """
        return self.__strategy.do_algorithm(['b', 'a', 'd', 'c'])


class Strategy(ABC):

    @abstractmethod
    def do_algorithm(self, data: List):
        """
        该策略的具体执行
        该方法必须重写  否则抛异常
        :param data: 处理的数据
        :return:
        """
        pass


class StrategyInstanceA(Strategy):
    """该策略将数据排序"""

    def do_algorithm(self, data: List):
        data.sort()
        return data


class StrategyInstanceB(Strategy):
    """该策略将数据倒序排序"""

    def do_algorithm(self, data: List):
        data.sort(reverse=True)
        return data


if __name__ == '__main__':
    # 使用策略A初始化 上下文
    context = Context(StrategyInstanceA())
    print(context.strategy)  # <__main__.StrategyInstanceA object at 0x000001CB017D4B50>
    print(context.do_something())  # ['a', 'b', 'c', 'd']

    # 将策略切换成 策略B
    context.strategy = StrategyInstanceB()
    print(context.strategy)  # <__main__.StrategyInstanceB object at 0x0000020369C55820>
    print(context.do_something())  # ['d', 'c', 'b', 'a']
