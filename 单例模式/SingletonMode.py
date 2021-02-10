"""
coding: utf8
@time: 2021/2/10 18:29
@author: cjr
@file: SingletonMode.py
"""


# 装饰器实现单例
def singleton(cls):
    __instance = {}

    def inner():
        if cls not in __instance:
            __instance[cls] = cls()
        return __instance[cls]
    return inner


@singleton
class Cls:
    def __init__(self):
        pass


cls1 = Cls()
cls2 = Cls()
print(id(cls1) == id(cls2))


# new关键字实现单例
class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance


singleton1 = Singleton()
singleton2 = Singleton()
print(id(singleton1) == id(singleton2))


# 使用type创建单例
class Singleton2(type):
    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(Singleton2, cls).__call__(*args, **kwargs)
        return cls.__instance[cls]


class Cls5(metaclass=Singleton2):
    pass


cls3 = Cls5()
cls4 = Cls5()
print(id(cls3) == id(cls4))

from threading import Lock


class Singleton3:
    __instance = None
    __lock = Lock()

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:  # 在最外层加上一层额外的if判断，减少lock阻塞概率，提升性能。       
            # 临界区 Start       
            cls.__lock.acquire()
        try:
            if cls.__instance is None:
                cls.__instance = super().__new__(cls, *args, **kwargs)
        # 临界区内拦截所有异常重抛，避免死锁           
        except Exception as e:
            raise e
        finally:
            if cls.__lock.locked():
                cls.__lock.release()  # 临界区 End 
        return cls.__instance


class Cls6(Singleton3):
    pass


cls5 = Cls6()
cls6 = Cls6()
print(id(cls5) == id(cls6))


