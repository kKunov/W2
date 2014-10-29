import unittest
import dungeon
import orc
import hero
import weapons


class TestDungeon(unittest.TestCase):
    def setUp(self):
        self.map_1 = dungeon.Dungeon("map1.txt")
        self.orc = orc.Orc("The Devil", 100, 1.2)
        self.hero = hero.Hero("Goshko", 100, "strahliveca")
        self.weapon1 = weapons.Weapons("Small Axe", 20, 0.2)
        self.orc.equip_weapon(self.weapon1)
        self.hero.equip_weapon(self.weapon1)

    def test_init(self):
        self.assertEqual(self.map_1.file_path, "map1.txt")

    def test_print_map(self):
        self.assertTrue(self.map_1.print_map())

    def test_spawn(self):
        self.assertTrue(self.map_1.spawn("Shady", self.hero))
        self.assertFalse(self.map_1.spawn("Shady", self.hero))
        self.assertTrue(self.map_1.spawn("Gandalf_sexy!", self.orc))
        self.assertFalse(self.map_1.spawn("Shady", self.hero))
        self.assertFalse(self.map_1.spawn("Shady", self.orc))


if __name__ == '__main__':
    unittest.main()
