from abc import ABC, abstractmethod
import random
class Unit(ABC):
    _name = None
    _strength = 0
    _health = 0
    _doubleattack = 0
    _defence = 0

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
    _defence = 20
    def _attack(self, opponent):
        dmg = self._strength
        if self._cheak_double_attack():
            dmg = dmg * 2
        opponent.health -= dmg
        self.health += dmg * 0.1


class Knight(Unit):
    _doubleattack = 0.4
    _defence = 40

    def _attack(self, opponent):
        dmg = self._strength
        if self._cheak_double_attack():
            dmg = dmg * 2
        opponent.health -= (dmg * 1.2 - opponent._defence)


class Monk(Unit):
    _doubleattack = 0.7
    _defence = 30
    def _attack(self, opponent):
        dmg = self._strength
        if self._cheak_double_attack():
            dmg = dmg * 2
        opponent.health -= dmg - opponent._defence
        self._health = round(self._health * 1.1)


class Rogue(Unit):
    _doubleattack = 0.4
    _defence = 25
    def _attack(self, opponent):
        dmg = self._strength
        if self._cheak_double_attack():
            dmg = dmg * 2
        opponent.health -= dmg - opponent._defence

k1 = Knight(name="Artur", strength=100, health=500)
v1 = Vampire(name="Drac", strength=100, health=500)
r1 = Rogue(name="Krok", strength=70, health=1000)
m1 = Monk(name="Panda Kunfu", strength=90, health=500)


class Battle():
    _opponent1 = None
    _opponent2 = None
    _units = None

    def __init__(self, opp1, opp2):
        if isinstance(opp1, Unit) and isinstance(opp2, Unit):
            self._opponent1 = opp1
            self._opponent2 = opp2
            self._units = (self._opponent1, self._opponent2)

    def _battle(self):
        random_unit = random.choice(self._units)
        if random_unit == self._opponent1:
            while True:
                if not self._opponent1._health == 0 or not self._opponent2._health == 0:
                    self._opponent1._attack(self._opponent2)
                    print(self._opponent2._health, self._opponent2.__class__.__name__)
                    if self._opponent2._health == 0:
                        return f"У бойца класса {self._opponent2.__class__.__name__} осталось {self._opponent2._health} "\
                               f" жизней и он потерпел порожение"

                    self._opponent2._attack(self._opponent1)
                    print(self._opponent1._health, self._opponent1.__class__.__name__)
                    if self._opponent1.health == 0:
                        return f"У бойца класса {self._opponent1.__class__.__name__} осталось {self._opponent1._health} "\
                               f" жизней и он потерпел порожение"
        else:
            while True:
                if not self._opponent1._health == 0 or not self._opponent2._health == 0:
                    self._opponent2._attack(self._opponent1)
                    print(self._opponent1._health, self._opponent1.__class__.__name__)
                    if self._opponent1.health == 0:
                        return f"У бойца класса {self._opponent1.__class__.__name__} осталось {self._opponent1._health} "\
                               f" жизней и он потерпел порожение"
                    self._opponent1._attack(self._opponent2)
                    print(self._opponent2._health, self._opponent2.__class__.__name__)
                    if self._opponent2._health == 0:
                        return f"У бойца класса {self._opponent2.__class__.__name__} осталось {self._opponent2._health} "\
                               f" жизней и он потерпел порожение"

battle1 = Battle(k1, r1)
print(battle1._battle())



