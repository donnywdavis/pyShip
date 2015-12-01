from random import randint


def get_ship_positions(ship):
    """
    Calculate the positions that a ship will occupy on the board

    :param ship: The ship object to calculate positions for
    :return: A list with the positions for the ship
    """

    start = (randint(2, (11 - ship.length)), randint(2, 11))
    if start[1] + ship.length > 11:
        positions = tuple([(x, start[1]) for x in range(start[0], (ship.length + start[0]))])
    else:
        positions = tuple([(start[0], y) for y in range(start[1], (ship.length + start[1]))])

    return positions


def load_ships(number_of_ships):
    """
    Build a list of ships that the player will use

    :param number_of_ships: The number of ships to load
    :return: A list of ship objects for the player
    """
    ships_list = (
        ('battleship', 4),
        ('carrier', 6),
        ('submarine', 3),
        ('destroyer', 3),
        ('cruiser', 2)
    )
    ships = []
    used_positions = []

    for i in range(number_of_ships):
        ship = Ship(ships_list[i][0], ships_list[i][1])
        positions = tuple()
        while set(used_positions).intersection(positions) or positions == tuple():
            positions = get_ship_positions(ship)
        used_positions.append(positions)
        ship.positions = positions
        ships.append(ship)

    return ships


class Ship(object):

    def __init__(self, name, length):
        """
        Initialize a ship object

        :param name: The name of the ship
        :param length: The length of the ship
        """

        self.name = name
        self.length = length
        self.positions = tuple()
        self.hits = 0

    def __str__(self):
        return self.name

    def hit(self, x, y):
        """
        Check if the ship is hit

        :param x: The x coordinate for the ship
        :param y: The y coordinate for the ship
        :return: Boolean if the ship is hit
        """

        if set(self.positions).intersection(((x, y),)):
            self.hits += 1
            return True
        else:
            return False

    def sunk(self):
        """
        Check if the ship is sunk

        :return: Boolean if the ship has been sunk
        """

        return True if self.hits == self.length else False
