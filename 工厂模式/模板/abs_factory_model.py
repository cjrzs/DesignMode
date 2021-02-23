"""
coding: utf8
@time: 2021/2/21 18:43
@author: cjr
@file: abs_factory_model.py
"""
# 在该例子下我们看到系列1和系列2，分别有A，B两款产品
# 系列1的产品是A1，B1， 系列2的产品是A2，B2

from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """
    一个必须的抽象工厂方法，返回一系列的产品
    """
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    """
    工厂方法，生产具体的产品实例
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    """
    工厂方法，生产另外一系列的产品实例
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


class AbstractProductA(ABC):
    """
    产品A有一个基本的接口，该产品的作用或者介绍等
    """

    @abstractmethod
    def useful_function_a(self) -> str:
        pass


"""
下面是产品实例
"""


class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A1."


class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A2."


class AbstractProductB(ABC):
    """
    另外一个产品，可以和同样系列的产品产生互动
    """
    @abstractmethod
    def useful_function_b(self) -> None:
        """
        产品B也可以做一些事
        """
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        """
        产品b可以和a产生互动，因为他们都是一系列的产品
        """
        pass


"""
生产产品B的实例
"""


class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B1."

    """
    产品B1可以和产品A1产生活动
    """

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"


class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B2."

    def another_useful_function_b(self, collaborator: AbstractProductA):
        """
        产品B2可以和产品A2产生互动
        """
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the ({result})"


def client_code(factory: AbstractFactory) -> None:

    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())
