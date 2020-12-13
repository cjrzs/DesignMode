"""
coding: utf8
@time: 2020/12/13 22:01
@author: cjr
@file: abstract_factory.py
"""


"""
抽象工厂方法是许多工厂方法的集合，每一个工厂方法负责生产一种不同的对象
"""


class Frog:
    """
    青蛙
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f'{self} the Frog encounters {obstacle} and {act}!'
        print(msg)


class Bug:
    """
    虫子
    """
    def __str__(self):
        return 'A Bug'

    def action(self):
        return 'eats it'


class FrogWorld:
    """
    青蛙游戏，工厂方法
    """
    def __init__(self, name):
        print(self)
        self.name = name

    def __str__(self):
        return '\n\n\t---- Frog World ----'

    def make_character(self):
        return Frog(self.name)

    @staticmethod
    def make_obstacle():
        return Bug()


class Wizard:
    """
    巫师
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f'{self} the Wizard battles {obstacle} and {act}!'
        print(msg)


class Ork:
    """
    兽人
    """
    def __str__(self):
        return 'an evil ork'

    def action(self):
        return 'kills it'


class WizardWorld:
    """
    巫师游戏的工厂方法
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '\n\n\t ---- Wizard World ----'

    def make_character(self):
        return Wizard(self.name)

    @staticmethod
    def make_obstacle():
        return Ork()


class GameEnvironment:
    """
    由两个工厂方法组成抽象工厂
    """
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def vail_date_age(name):
    try:
        age = input(f'Welcome {name}, How old are you?')
        age = int(age)
    except ValueError as e:
        print(f'The age is vail date, please try again')
        return False, age
    return True, age


def main():
    name = input('Hello, what is you name?')
    valid_input = False
    while not valid_input:
        valid_input, age = vail_date_age(name)
    game = WizardWorld if age > 18 else FrogWorld
    environment = GameEnvironment(game(name))
    environment.play()


if __name__ == '__main__':
    main()
