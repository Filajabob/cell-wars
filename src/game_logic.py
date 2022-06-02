def capture(coords, faction, board):
    if faction.power <= 0:
        print(f"{faction.name} does not have enough power!")
        return

    if not board.beside(faction=faction, coords=coords):
        print(f"{faction.name} does not have cells touching that cell!")
        return

    board.transfer_cell(coords, faction)
    faction.power -= 1

