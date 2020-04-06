from piece import Piece
x = "x"
o = "o"
sample_board_1 = [
    [x, 2, x, 2, x, 2, x, 2],
    [2, x, 2, x, 2, x, 2, x],
    [x, 2, x, 2, x, 2, x, 2],
    [o, x, o, x, o, x, o, x],
    [x, o, x, o, x, o, x, o],
    [1, x, 1, x, 1, x, 1, x],
    [x, 1, x, 1, x, 1, x, 1],
    [1, x, 1, x, 1, x, 1, x],

]
sample_piece = Piece(2, False, [2, 3])
sample_valid_moves = [[3, 2], [3, 4]]
sample_move_to_1 = [3, 2]
sample_move_to_2 = [3, 3]


def move(game_board, valid_moves, piece, move_to):
