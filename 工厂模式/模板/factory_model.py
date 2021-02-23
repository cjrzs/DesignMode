"""
coding: utf8
@time: 2021/2/21 17:04
@author: cjr
@file: factory_model.py
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    """
    创建者基类，声明了一个工厂方法，该方法将返回一个产品的实体对象。
    子类需提供其实现，来创建不同的对象。
    """

    @abstractmethod
    def factory_method(self):
        # 此处如果不将创建工厂的方法设置成抽象也可，
        # 转而提供一个默认的方法，也就是提供一个默认对象。
        pass

    def some_operation(self) -> str:
        """
        除了创建一个名字之外，还要设置一些核心的业务逻辑。
        它依赖于factory_method返回的实体对象。
        子类也可以通过重写该方法，创建拥有不同行为的产品。
        """
        # Call the factory method to create a Product object.
        product = self.factory_method()

        # Now, use the product.
        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result


# 两个实际的创建者，创建不同的产品实例
class ConcreteCreator1(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


# 拥有实际行为的产品
class Product(ABC):
    def operation(self):
        pass


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


def client_code(creator: Creator) -> None:
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == '__main__':
    client_code(ConcreteCreator1())
    client_code(ConcreteCreator2())

