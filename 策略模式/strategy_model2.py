"""
在python中函数是一等公民，
因此我们可以基于函数实现策略模式
"""


class Context:
    """定义客户端接口"""

    def __init__(self, strategy=None):
        """
        在Context中通过初始化函数来接收策略
        :param strategy:
        """
        self.__strategy = strategy
        self.data = ['b', 'a', 'd', 'c']

    @property
    def strategy(self):
        """
        维护具体的策略
        :return:
        """
        return self.__strategy

    @strategy.setter
    def strategy(self, strategy):
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
        if not self.__strategy:
            return None
        return self.__strategy(self)


def strategy_instance_a(context: Context) -> Context:
    """
    该策略将数据排序
    :param context:
    :return:
    """
    context.data.sort()
    return context


def strategy_instance_b(context: Context) -> Context:
    """
    该策略将数据倒序排序
    :param context:
    :return:
    """
    context.data.sort(reverse=True)
    return context


if __name__ == '__main__':
    # 使用策略A初始化上下文
    c = Context(strategy_instance_a)
    print(c.strategy)  # <function strategy_instance_a...>
    print(c.do_something().data)  # ['a', 'b', 'c', 'd']

    # 切换到策略B
    c.strategy = strategy_instance_b
    print(c.strategy)  # <function strategy_instance_b...>
    print(c.do_something().data)  # ['d', 'c', 'b', 'a']

    # 进一步使用策略
    # 比如我们想找到所有的策略 如下所示
    strategy_instances = [item for item in globals() if item.startswith('strategy_instance_')]
    print(strategy_instances)  # ['strategy_instance_a', 'strategy_instance_b']



