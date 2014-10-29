import unittest
import entity
import weapons


class TestEntity(unittest.TestCase):
    def setUp(self):
        self.new_entity = entity.Entity("Gosho", 100)
        self.weapon = weapons.Weapons("Axe", 10, 0.6)

    def test_init(self):
        self.assertEqual("Gosho", self.new_entity.name)
        self.assertEqual(100, self.new_entity.health)

    def test_get_health(self):
        self.assertEqual(self.new_entity.get_health(), 100)

    def test_is_alive(self):
        self.assertTrue(self.new_entity.is_alive())
        self.new_entity.health = 0
        self.assertFalse(self.new_entity.is_alive())

    def test_has_weapon_and_equip_weapon(self):
        self.assertFalse(self.new_entity.has_weapon())
        self.new_entity.equip_weapon(self.weapon)
        self.assertEqual(self.new_entity.weapon, self.weapon)
        self.assertTrue(self.new_entity.has_weapon())
        new_weapon = weapons.Weapons("Sword", 20, 0.7)
        self.new_entity.equip_weapon(new_weapon)
        self.assertEqual(self.new_entity.weapon, new_weapon)

    def test_attack(self):
        self.assertEqual(self.new_entity.attack(), 0)
        self.new_entity.equip_weapon(weapons.Weapons("Small Axe", 10, 0))
        self.assertEqual(self.new_entity.attack(), 10)
        self.new_entity.equip_weapon(weapons.Weapons("Small Sword", 10, 1))
        self.assertEqual(self.new_entity.attack(), 20)


if __name__ == '__main__':
    unittest.main()
