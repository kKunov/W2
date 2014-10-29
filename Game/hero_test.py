import hero
import unittest


class HeroTests(unittest.TestCase):
    def setUp(self):
        self.born_hero = hero.Hero("Bron", 100, "DragonSlayer")

    def test_hero_init(self):
        self.assertEqual(self.born_hero.nickname, "DragonSlayer")

    def test_known_as(self):
        self.assertEqual(self.born_hero.known_as(), "Bron the DragonSlayer")

    def test_take_dmg(self):
        self.born_hero.take_dmg(50)
        self.assertEqual(self.born_hero.get_health(), 50)
        self.born_hero.take_dmg(62)
        self.assertEqual(self.born_hero.get_health(), 0)

    def test_get_healing(self):
        self.born_hero.health = 45
        self.assertTrue(self.born_hero.get_healing(35))
        self.assertEqual(self.born_hero.get_health(), 80)
        self.assertTrue(self.born_hero.get_healing(35))
        self.assertEqual(self.born_hero.get_health(), 100)
        self.born_hero.health = 0
        self.assertFalse(self.born_hero.get_healing(10))


if __name__ == '__main__':
    unittest.main()
