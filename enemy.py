from random import randint

class Enemy:
    def __init__(self) -> None:
        self.hp = randint(70, 130)
        self.damage = randint(6, 13)