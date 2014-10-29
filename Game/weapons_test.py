import unittest
import weapons


class TestWeapons(unittest.TestCase):
    def setUp(self):
        self.axe = weapons.Weapons("Bad Axe", 3, 0.5)

    def test_init(self):
        self.assertEqual(self.axe.name, "Bad Axe")
        self.assertEqual(self.axe.dmg, 3)
        self.assertEqual(self.axe.critical_stricke_chance, 0.5)
        with self.assertRaises(ValueError):
            weapons.Weapons("", 4, 3)

    def test_critical_hit(self):
        has_crit = 0
        hasnt_crit = 0
        for n in range(1000):
            if self.axe.critical_hit():
                has_crit = True
            else:
                hasnt_crit = True
        self.assertTrue(has_crit, hasnt_crit)


if __name__ == '__main__':
    unittest.main()
