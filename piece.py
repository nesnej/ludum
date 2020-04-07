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
sample_board_2 = [
    [x, 2, x, 2, x, 2, x, 2],
    [2, x, 2, x, 2, x, 2, x],
    [x, 2, x, 2, x, 2, x, 2],
    [o, x, 1, x, o, x, o, x],
    [x, o, x, o, x, o, x, o],
    [1, x, 1, x, 1, x, 1, x],
    [x, 1, x, o, x, 1, x, 1],
    [1, x, 1, x, 1, x, 1, x],

]
sample_valid_moves = [[[3, 2]], [[3, 4]]]
sample_move_to_1 = [[3, 2]]
sample_move_to_2 = [[3, 3]]

sample_valid_moves_2 = [[[3, 4]], [[4, 1], [6, 3]]]
sample_good_move_1 = [[4, 1], [6, 3]]


class Piece:
    def __init__(self, team, king, position):
        self.team = team
        self.king = king
        self.position = position

    def move(self, game_board, valid_moves, move_to):
        rowIndex = 0
        columnIndex = 1
        moveToLength = len(move_to)

        valid_move = False
        for move in valid_moves:
            number_of_move_parts_checked = 0
            for move_part in move:
                if number_of_move_parts_checked > moveToLength:
                    valid_move = True
                    break
                if move_part[rowIndex] != move_to[number_of_move_parts_checked][rowIndex] or move_part[columnIndex] != move_to[number_of_move_parts_checked][columnIndex]:
                    break
                number_of_move_parts_checked += 1
                # This is for when move_to is of length 1
                if moveToLength == 1:
                    valid_move = True
                    break
                if number_of_move_parts_checked == moveToLength:
                    # We've check all the parts of the move and we haven't had an invalid entry so it a good move.
                    valid_move = True
                    break
            if valid_move == True:
                break

        if valid_move == False:
            raise ValueError("This move is not valid.")
        print("this is a valid move!")
        # perform the move one step at a time, removing piece if they get jumped


# sample_piece = Piece(2, False, [2, 3])
# try:
#     sample_piece.move(sample_board_1, sample_valid_moves, sample_move_to_1)
# except ValueError:
#     print("This move is not valid yo.")

sample_piece2 = Piece(2, False, [2, 3])
try:
    sample_piece2.move(sample_board_2, sample_valid_moves_2,
                       sample_good_move_1)
except ValueError:
    print("This move is not valid yo.")
