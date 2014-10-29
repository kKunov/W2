class Entity:

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.MAX_HEALTH = 100
        self.weapon = False

    def get_health(self):
        return self.health

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def take_dmg(self, dmg):
        if dmg > self.get_health():
            self.health = 0
        else:
            self.health -= dmg

    def has_weapon(self):
        if self.weapon is not False:
            return True
        else:
            return False

    def equip_weapon(self, weapon):
        if self.weapon is False:
            self.weapon = weapon
        else:
            self.weapon = False
            self.weapon = weapon

    def attack(self):
        if self.weapon is False:
            return 0
        elif (self.weapon is not False
              and self.weapon.critical_hit()):
            #print("crit %s" % (self.weapon.dmg * 2))
            return self.weapon.dmg * 2
        return self.weapon.dmg
