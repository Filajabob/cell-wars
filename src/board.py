from cell import Cell
from faction import Faction, NoFaction
import utils


class Board:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.cells = []

        i = 0

        for x in range(1, self.width + 1):
            for y in range(1, self.height + 1):
                self.cells.append(Cell(i, (x, y)))
                i += 1

    def search_for_cell(self, x: int = None, y: int = None, *, coords: tuple = None, ignore_errors=False):
        if not coords:
            coords = (x, y)

        for cell in self.cells:
            if cell.coords == coords:
                return cell
        else:
            if not ignore_errors:
                raise KeyError(f"Failed to find cell at {coords}")
            else:
                return

    def owned(self, coords, faction):
        return self.search_for_cell(coords=coords).num == faction.num

    def beside(self, x=None, y=None, faction=NoFaction(), *, coords=None):
        if not (x or y):
            x = coords[0]
            y = coords[1]

        try:
            above_owned = self.search_for_cell(x, y + 1, ignore_errors=True).owner.num == faction.num
            # 'NoneType' object has no attribute 'owner' means the cell was not found and we should ignore it
        except:
            above_owned = False

        try:
            below_owned = self.search_for_cell(x, y - 1, ignore_errors=True).owner.num == faction.num
        except:
            below_owned = False

        try:
            left_owned = self.search_for_cell(x - 1, y, ignore_errors=True).owner.num == faction.num
        except:
            left_owned = False

        try:
            right_owned = self.search_for_cell(x + 1, y, ignore_errors=True).owner.num == faction.num
        except:
            right_owned = False

        return above_owned or below_owned or left_owned or right_owned

    def compact_dimensional(self):
        i = 0
        result = []

        for x in range(1, self.width + 1):
            result.append([])  # Create a new axis

            for y in range(1, self.height + 1):
                result[x - 1].append(self.search_for_cell(x, y).owner.num)
                i += 1

        return result

    def pretty(self):
        pretty_board = "\t"

        for x in range(self.width):
            pretty_board += f" {x + 1}  "

        pretty_board += f'X\n'

        for y in range(1, self.height + 1):
            pretty_board += f' {utils.Colors.CYAN}{y}\t'

            for x in range(1, self.width + 1):
                pretty_board += f"{utils.rgb(*self.search_for_cell(x, y).owner.rgb)}" \
                                f"[{self.compact_dimensional()[x - 1][y - 1]}]" \
                                f"{utils.Colors.CYAN} "

            pretty_board += f'{utils.Colors.CYAN}\n'

        pretty_board += " Y"

        return pretty_board

    def transfer_cell(self, cell_coords: tuple, target_faction: Faction = NoFaction()):
        cell = self.search_for_cell(coords=cell_coords)
        cell.owner = target_faction

    def faction_exists(self, faction):
        faction_num = faction.num
        cells_owners_nums = [cell.owner.num for cell in self.cells]

        return faction_num in cells_owners_nums

    def cell_exists(self, x=None, y=None, *, coords=None, num=None):
        if x and y:
            coords = (x, y)
        elif num:
            for cell in self.cells:
                if cell.num == num:
                    return True
            else:
                return False

        return self.search_for_cell(coords=coords, ignore_errors=True) is not None
