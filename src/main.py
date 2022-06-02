import argparse
import random

from game_logic import capture
from board import Board
from faction import Faction, NoFaction

import utils
from utils.constants import set_var

# Check to enable or disable colors based on sys args
parser = argparse.ArgumentParser()
parser.add_argument('-c', "--colors", help="Whether to enable colors.", action=argparse.BooleanOptionalAction)
args = parser.parse_args()

set_var("COLORS_ENABLED", args.colors)

width = int(input("How wide should the board be? "))
height = int(input("How high should the board be? "))

print("Creating board...")
board = Board(width, height)

amount_of_factions = int(input("How many factions should there be? "))
factions = []

for i in range(1, amount_of_factions + 1):
    faction_name = input(f"Name of faction {i}: ")
    factions.append(Faction(faction_name, i, 20,
                            (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))))

print("Populating board...")

for faction in factions:
    coords = (random.randint(2, width - 1), random.randint(2, height - 1))
    starting_cell = board.search_for_cell(coords=coords)

    while starting_cell.owner is NoFaction():
        coords = (random.randint(2, width - 1), random.randint(2, height - 1))
        starting_cell = board.search_for_cell(coords=coords)

    board.transfer_cell(coords, faction)

print("Let's start!")

for faction in factions:
    print(f"{utils.rgb(*faction.rgb)}{faction.num}: {faction.name}")

print(board.pretty())

while True:
    for faction in factions:
        print(f"{utils.Colors.WHITE}It's {faction.name}'s turn!")
        x = int(input("X: "))
        y = int(input("Y: "))

        capture((x, y), faction, board)

        print(board.pretty())
