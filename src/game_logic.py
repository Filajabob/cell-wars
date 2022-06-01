def capture(coords, faction, board):
    if faction.power <= 0:
        print(f"{faction.name} does not have enough power!")

    if not board.search_for_cell(coords)

    board.transfer_cell(coords, faction)

