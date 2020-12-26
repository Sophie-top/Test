import random

class Humanoid():
    def __init__(self):
        self.name = "Безымянный"
        self.surname = "Бесфамильный"
        self.level = 1
        self.HP = 100

    def print_stats(self):
        print(self.name)
        print(self.surname)
        print(self.level)
        print(self.HP)

    def change_stats(self, HP_damage):
        self.HP -= HP_damage


class Player(Humanoid):
    def __init__(self, name, surname, level, HP):
        super().__init__()
        self.name = name
        self.surname = surname
        self.level = level
        self.HP = HP

class Enemy(Humanoid):
    def __init__(self, level, ):
        super().__init__()
        self.name = random.choise(("Грэг", "Жран", "Грыз", "Аргх"))
        self.surname = random.choise(("Одноглазый", "Дерзкий", "Зловонный", "Алчный"))
        self.level = level
        self.HP = 100
