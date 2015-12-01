import unittest
from app.ship import Ship


class ShipSetupTests(unittest.TestCase):

    def setUp(self):
        self.ship = Ship('battleship', 4)
        self.ships = []
        self.ships.append(Ship('battleship', 4))
        self.ships.append(Ship('destroyer', 3))
        self.ships.append(Ship('submarine', 3))

    def test_ship_has_been_generated(self):
        self.assertNotEqual(self.ship, None)

    def test_ship_does_not_have_a_hit(self):
        self.assertEqual(self.ship.hits, 0)

    def test_ship_has_a_hit(self):
        self.ship.hits = 1
        self.assertEqual(self.ship.hits, 1)
