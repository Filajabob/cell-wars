from board import Board
from faction import Faction

playing_board = Board(10, 10)
americans = Faction("Americans", 1, 1)

print(playing_board.pretty())

playing_board.transfer_cell((1, 2), americans)

print(playing_board.pretty())
