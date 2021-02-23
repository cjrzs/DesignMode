"""
coding: utf8
@time: 2020/12/27 20:23
@author: cjr
@file: builderpat.py
"""
import time

from enum import Enum


PizzaProgress = Enum('PizzaProgress', 'queued preparation baking ready')
PizzaDough = Enum('PizzaDough', 'thin thick')
PizzaSauce = Enum('PizzaSauce', 'tomato creme_fraiche')
PizzaTopping = Enum('PizzaTopping', 'mozzarella double_mozzarella bacon ham mushrooms red_onion oregano')
STEP_DELAY = 3


class Pizza:

    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self, dough):
        self.dough = dough
        print(f'preparing the {self.dough.name} dough of your {self} ...')
        time.sleep(STEP_DELAY)
        print(f'done with the {self.dough.name} dough')


class MargaritaBuilder:

    def __init__(self):
        self.pizza = Pizza('margarita')
        self.Progress = PizzaProgress.

