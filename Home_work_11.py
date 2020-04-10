

from abc import ABC, abstractmethod
import random
class Unit(ABC):
    _name = None
    _strength = 0
    _health = 0
    _doubleattack = 0

    def _cheak_name(self, name):
        return name

    def __init__(self, name, strength, health):
        self._name = self._cheak_name(name)
        self._strength = strength
        self.health = health

    def _cheak_double_attack(self):
        crit = random.random()
        if self._doubleattack >= crit:
            return True

    @abstractmethod
    def _attack(self, opponent):
        pass

    def attack(self, opponent):
        if not isinstance(opponent, Unit):
            raise Exception
        if opponent._health == 0:
            raise Exception(f'Здоровье противника = "{opponent.health}"')


        if isinstance(opponent, Rogue):
            r = random.randint(1, 10)
            if r == 2:
                opponent.health = opponent.health
            else:
                return self._attack(opponent)
        else:
            return self._attack(opponent)


    @property
    def health(self):
        return self._health


    @health.setter
    def health(self, val):
        if not isinstance(val, (int, float)):
            raise Exception

        self._health = val if val > 0 else 0


class Vampire(Unit):
    _doubleattack = 0.5
    def _attack(self, opponent):
        dmg = self._strength
        if self._cheak_double_attack():
            dmg = dmg * 2
        opponent.health -= dmg
        self.health += dmg * 0.1


class Knight(Unit):
    _doubleattack = 0.4

    def _attack(self, opponent):
        dmg = self._strength
        if self._cheak_double_attack():
            dmg = dmg * 2
        opponent.health -= dmg * 1.2


class Monk(Unit):
    _doubleattack = 0.7
    def _attack(self, opponent):
        dmg = self._strength
        if self._cheak_double_attack():
            dmg = dmg * 2
        opponent.health -= dmg
        self._health = round(self._health * 1.1)


class Rogue(Unit):
    _doubleattack = 0.4
    def _attack(self, opponent):
        dmg = self._strength
        if self._cheak_double_attack():
            dmg = dmg * 2
        opponent.health -= dmg

k1 = Knight(name="Artur", strength=100, health=500)
v1 = Vampire(name="Drac", strength=100, health=500)
r1 = Rogue(name="Krok", strength=70, health=500)
m1 = Monk(name="Panda Kunfu", strength=90, health=500)

print(r1._health)
k1.attack(r1)
print(r1._health)
k1.attack(r1)
print(r1._health)
k1.attack(r1)
print(r1._health)
k1.attack(r1)
print(r1._health)
k1.attack(r1)
print(r1._health)
k1.attack(r1)
print(r1._health)
k1.attack(r1)
print(r1._health)
k1.attack(r1)
print(r1._health)