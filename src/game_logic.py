def capture(coords, faction, board):
    """
    Returns True if capture was successful, returns None if not
    """

    if faction.power <= 0:
        print(f"{faction.name} does not have enough power!")
        return

    if not board.beside(faction=faction, coords=coords):
        print(f"{faction.name} does not have cells touching that cell!")
        return

    if not board.cell_exists(coords=coords):
        print(f"The cell at {coords} does not exist!")
        return

    board.transfer_cell(coords, faction)
    faction.power -= 1

    return True

