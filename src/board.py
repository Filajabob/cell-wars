from cell import Cell
from faction import Faction, NoFaction


class Board:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.cells = []

        i = 0

        for x in range(self.width):
            for y in range(self.height):
                self.cells.append(Cell(i, (x, y)))
                i += 1

    def search_for_cell(self, x: int = None, y: int = None, *, coords: tuple = None):
        if not coords:
            coords = (x, y)

        for cell in self.cells:
            if cell.coords == coords:
                return cell
        else:
            raise KeyError(f"Failed to find cell at {coords}")

    def owned(self, coords, faction):
        return self.search_for_cell(coords=coords).num == faction.num

    def compact_dimensional(self):
        i = 0
        result = []

        for x in range(self.width):
            result.append([])  # Create a new axis

            for y in range(self.height):
                result[x].append(self.search_for_cell(x, y).owner.num)
                i += 1

        return result

    def pretty(self):
        pretty_board = ""

        for x in range(self.width):
            for y in range(self.height):
                pretty_board += f"[{self.compact_dimensional()[x][y]}] "

            pretty_board += '\n'

        return pretty_board

    def transfer_cell(self, cell_coords: tuple, target_faction: Faction = NoFaction()):
        cell = self.search_for_cell(coords=cell_coords)
        cell.owner = target_faction
