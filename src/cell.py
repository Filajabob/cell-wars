from faction import Faction, NoFaction


class Cell:
    def __init__(self, num: int, coords: tuple, owner: Faction=NoFaction()):
        self.num = num
        self.coords = coords
        self.owner = owner
