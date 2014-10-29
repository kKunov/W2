import unittest
import orc
import weapons


class TestOrc(unittest.TestCase):
    def setUp(self):
        self.born_orc = orc.Orc("The Devil", 100, 1.3)

    def test_orc_init(self):
        self.assertEqual(self.born_orc.berserk_factor, 1.3)
        with self.assertRaises(ValueError):
            orc.Orc("New Devil", 100, 2.3)

    def test_take_dmg(self):
        self.born_orc.take_dmg(20)
        self.assertEqual(self.born_orc.get_health(), 80)
        self.born_orc.take_dmg(82)
        self.assertEqual(self.born_orc.get_health(), 0)

    def test_take_healing(self):
        self.born_orc.health = 20
        self.assertTrue(self.born_orc.take_healing(30))
        self.assertEqual(self.born_orc.get_health(), 50)
        self.assertTrue(self.born_orc.take_healing(80))
        self.assertEqual(self.born_orc.get_health(), self.born_orc.MAX_HEALTH)
        self.born_orc.health = 0
        self.assertFalse(self.born_orc.take_healing(23))

    def test_attack(self):
        self.assertEqual(self.born_orc.attack(), 0)
        self.born_orc.equip_weapon(weapons.Weapons("Small Axe", 10, 0))
        self.assertEqual(self.born_orc.attack(), 13)
        self.born_orc.equip_weapon(weapons.Weapons("Small Sword", 10, 1))
        self.assertEqual(self.born_orc.attack(), 26)


if __name__ == '__main__':
    unittest.main()
