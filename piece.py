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
sample_valid_moves = [[3, 2], [3, 4]]
sample_move_to_1 = [3, 2]
sample_move_to_2 = [3, 3]


class Piece:
    def __init__(self, team, king, position):
        self.team = team
        self.king = king
        self.position = position

    def move(self, game_board, valid_moves, move_to):
        valid_move = False
        for move in valid_moves:
            if move[0] == move_to[0] and move[1] == move_to[1]:
                valid_move = True
        if valid_move == False:
            raise ValueError("This move is not valid.")
        print("made it past the valid move check!")


sample_piece = Piece(2, False, [2, 3])

try:
    sample_piece.move(sample_board_1, sample_valid_moves, sample_move_to_1)
except ValueError:
    print("This move is not valid yo.")
