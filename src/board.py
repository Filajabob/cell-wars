from cell import Cell
from faction import Faction, NoFaction
import utils


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

    def beside(self, x=None, y=None, faction=NoFaction(), *, coords=None):
        if not (x or y):
            x = coords[0]
            y = coords[1]

        above_owned = self.search_for_cell(x, y + 1).owner.num == faction.num
        below_owned = self.search_for_cell(x, y - 1).owner.num == faction.num
        left_owned = self.search_for_cell(x - 1, y).owner.num == faction.num
        right_owned = self.search_for_cell(x + 1, y).owner.num == faction.num

        return above_owned or below_owned or left_owned or right_owned

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
        pretty_board = "\t"

        for x in range(self.width):
            pretty_board += f" {x + 1}  "

        pretty_board += f'X\n'

        for y in range(self.height):
            pretty_board += f' {utils.Colors.CYAN}{y + 1}\t'

            for x in range(self.width):
                pretty_board += f"{utils.rgb(*self.search_for_cell(x, y).owner.rgb)}" \
                                f"[{self.compact_dimensional()[x][y]}]" \
                                f"{utils.Colors.CYAN} "

            pretty_board += f'{utils.Colors.CYAN}\n'

        pretty_board += " Y"

        return pretty_board

    def transfer_cell(self, cell_coords: tuple, target_faction: Faction = NoFaction()):
        cell = self.search_for_cell(coords=cell_coords)
        cell.owner = target_faction
