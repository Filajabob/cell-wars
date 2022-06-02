import argparse

from game_logic import capture
from board import Board
from faction import Faction
from utils.constants import set_var

# Check to enable or disable colors based on sys args
parser = argparse.ArgumentParser()
parser.add_argument('-c', "--colors", help="Whether to enable colors.", action=argparse.BooleanOptionalAction)
args = parser.parse_args()

set_var("COLORS_ENABLED", args.colors)

board = Board(10, 20)

america = Faction("America", 1, 10, (255, 0, 0))
board.transfer_cell((0, 1), america)
capture((1, 1), america, board)

print(board.pretty())
