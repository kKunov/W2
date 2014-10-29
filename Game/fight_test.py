import unittest
import fight
import hero
import orc
import weapons


class TestFight(unittest.TestCase):
    def setUp(self):
        self.test_weapon_1 = weapons.Weapons("Sword", 10, 0.5)
        self.test_weapon_2 = weapons.Weapons("Axe", 10, 0.5)
        self.test_hero = hero.Hero("Goshko", 100, "Aways sceried guy")
        self.test_hero.equip_weapon(self.test_weapon_1)
        self.test_orc = orc.Orc("The Devil", 100, 1)
        self.test_orc.equip_weapon(self.test_weapon_2)
        self.test_fight = fight.Fight(self.test_hero, self.test_orc)

    def test_init(self):
        self.assertEqual(self.test_fight.hero.name, self.test_hero.name)
        self.assertEqual(self.test_fight.hero.health, self.test_hero.health)
        self.assertEqual(self.test_fight.hero.nickname, self.test_hero.nickname)
        self.assertEqual(self.test_fight.orc.name, self.test_orc.name)
        self.assertEqual(self.test_fight.orc.health, self.test_orc.health)
        self.assertEqual(self.test_fight.orc.berserk_factor, self.test_orc.berserk_factor)

    def test_coinflip(self):
        hero_first = 0
        orc_first = 0
        for n in range(1000):
            if self.test_fight.coinflip():
                hero_first = True
            else:
                orc_first = True
        self.assertTrue(hero_first, orc_first)

    def test_simulate_fight(self):
        hero_win = 0
        orc_win = 0
        for n in range(1000):
            if self.test_fight.simulate_figrh() == "hero":
                hero_win = True
            else:
                orc_win = True
            self.test_fight.hero.health = 100
            self.test_fight.orc.health = 100
        self.assertTrue(orc_win)
        self.assertTrue(hero_win)


if __name__ == '__main__':
    unittest.main()
