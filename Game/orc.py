from entity import Entity


class Orc(Entity):

    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        self.__self_berserk(berserk_factor)

    def __self_berserk(self, berserk_factor):
        if berserk_factor > 2 or berserk_factor < 1:
            raise ValueError
        else:
            self.berserk_factor = berserk_factor

    def take_healing(self, healing_points):
        if (self.is_alive()
                and healing_points <= self.MAX_HEALTH - self.get_health()):
            self.health += healing_points
            return True
        elif (self.is_alive()
                and healing_points > self.MAX_HEALTH - self.get_health()):
            self.health = self.MAX_HEALTH
            return True
        else:
            return False

    def attack(self):
        if self.weapon is False:
            return 0
        elif self.weapon is not False and self.weapon.critical_hit() is True:
            #print("crit %s" % (self.weapon.dmg * 2 * self.berserk_factor))
            return self.weapon.dmg * 2 * self.berserk_factor
        return self.weapon.dmg * self.berserk_factor
