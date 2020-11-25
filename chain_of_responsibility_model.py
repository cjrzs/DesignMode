"""
coding: utf8
@time: 2020/11/25 10:45
@author: cjr
@file: chain_of_responsibility_model.py
"""


from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handler(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handler(self, request) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handler(request)
        return None


class MonkeyHandler(AbstractHandler):

    def handler(self, request: Any) -> str:
        if request == 'banana':
            return f'Monkey: i will eat the {request}'
        else:
            return super().handler(request)


class SquirrelHandler(AbstractHandler):

    def handler(self, request: Any) -> str:
        if request == 'Nut':
            return f'Squirrel: i will eat the {request}'
        else:
            return super().handler(request)


class DogHandler(AbstractHandler):

    def handler(self, request: Any) -> str:
        if request == 'MeatBall':
            return f'Dog: i will eat the {request}'
        else:
            return super().handler(request)


def client_code(hanlder: Handler) -> None:
    for food in ['banana', 'Nut', 'MeatBall', 'Cup of coffee']:
        print(f'Client: Who wants a {food}?')
        result = hanlder.handler(food)
        if result:
            print(f'{result}', end='')
        else:
            print(f'{food} was left untouched.', end='')


if __name__ == '__main__':
    monkey = MonkeyHandler()
    dog = DogHandler()
    squirrel = SquirrelHandler()
    # handler = monkey.set_next(dog).set_next(squirrel)
    monkey.set_next(dog).set_next(squirrel)
    client_code(monkey)
