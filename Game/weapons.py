import random


class Weapons:

    def __init__(self, name, dmg, critical_stricke_chance):
        self.name = name
        self.dmg = dmg
        self.__set_critical(critical_stricke_chance)

    def __set_critical(self, critical_stricke_chance):
        if critical_stricke_chance >= 0 and critical_stricke_chance <= 1:
            self.critical_stricke_chance = critical_stricke_chance
        else:
            raise ValueError

    def critical_hit(self):
        r = random.random()
        if r <= self.critical_stricke_chance:
            return True
        else:
            return False
