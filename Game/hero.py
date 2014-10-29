from entity import Entity


class Hero(Entity):

    def __init__(self, name, health, nickname):
        super().__init__(name, health)
        self.nickname = nickname
        self.max_health = 100

    def known_as(self):
        return "{} the {}".format(self.name, self.nickname)

    def get_healing(self, healing_points):
        if self.is_alive() and healing_points <= self.max_health - self.get_health():
            self.health += healing_points
            return True
        elif self.is_alive() and healing_points > self.max_health - self.get_health():
            self.health = self.max_health
            return True
        else:
            return False
