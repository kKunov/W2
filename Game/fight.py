import random


class Fight():

    def __init__(self, hero, orc):
        self.hero = hero
        self.orc = orc

    def coinflip(self):
        if random.random() <= 0.5:
            return True
        else:
            return False

    def simulate_figrh(self):
        turn = 0
        if self.coinflip():
            turn += 1
        while self.hero.is_alive() and self.orc.is_alive():
            if turn % 2 == 1:
                self.orc.take_dmg(self.hero.attack())
                #print("Orc HP: %s" % self.orc.get_health())
            else:
                self.hero.take_dmg(self.orc.attack())
                #print("Hero HP: %s" % self.hero.get_health())
            turn += 1
        if self.hero.is_alive():
            #print("The Hero Wins!")
            return "hero"
        else:
            #print("The Orc Wins!")
            return "orc"
