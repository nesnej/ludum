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
    [x, 2, x, 2, x, 2, x, 2],  # 0
    [2, x, 2, x, 2, x, 2, x],  # 1
    [x, 2, x, 2, x, 2, x, 2],  # 2
    [o, x, 1, x, o, x, o, x],  # 3
    [x, o, x, o, x, o, x, o],  # 4
    [1, x, 1, x, 1, x, 1, x],  # 5
    [x, 1, x, o, x, 1, x, 1],  # 6
    [1, x, 1, x, 1, x, 1, x],  # 7s
]
sample_board_3 = [
    [x, 2, x, 2, x, 2, x, 2],  # 0
    [2, x, 2, x, 2, x, 2, x],  # 1
    [x, 2, x, 1, x, 2, x, 2],  # 2
    [o, x, o, x, o, x, o, x],  # 3
    [x, 1, x, o, x, o, x, o],  # 4
    [o, x, 1, x, 1, x, 1, x],  # 5
    [x, 1, x, o, x, 1, x, 1],  # 6
    [1, x, 1, x, 1, x, 1, x],  # 7s
]
piece_4_valid_moves = [[[3, 2], [5, 0]]]
piece_4_move_to = [[3, 2], [5, 0]]


sample_valid_moves = [[[3, 2]], [[3, 4]]]
sample_move_to_1 = [[3, 2]]
sample_move_to_2 = [[3, 3]]

sample_valid_moves_2 = [[[3, 4]], [[4, 1], [6, 3]]]
sample_good_move_1 = [[4, 1], [6, 3]]

sample_valid_moves_3 = [[[4, 1]]]
sample_bad_move_1 = [[1, 1]]
sample_good_move_4 = [[4, 1]]


class Piece:
    def __init__(self, team, king, position):
        self.team = team
        self.king = king
        self.position = position

    def move(self, game_board, valid_move_paths, move_path):
        total_move_path_parts = len(move_path)
        final_destination = move_path[total_move_path_parts - 1]
        starting_position = self.position
        self.position = final_destination
        row_index = 0
        column_index = 1

        # first entry is where to move the piece, other entry are space to set to 'o'
        game_board_manipulations = [final_destination, starting_position]

        is_valid_move_path = is_move_path_valid(valid_move_paths, move_path)

        if is_valid_move_path == False:
            raise ValueError("This move is not valid.")

        print("this is a valid move!")

        # Remove enemy pieces that were jumped over from the game board
        if final_destination[row_index] >= starting_position[row_index] + 2:
            # This piece jumped at least one piece
            for jump in range(total_move_path_parts):
                if jump == 0:
                    # It's the first move
                    previous_move = starting_position
                else:
                    previous_move = move_path[jump - 1]
                current_move = move_path[jump]
                look_back_index = 1
                piece_to_remove = []
                # last jump we look back one column and one row
                if self.team == 2 and self.king == False:
                    if previous_move[column_index] > current_move[column_index]:
                        # The piece jumped to the left
                        piece_to_remove = [
                            current_move[0] -
                            1, current_move[1]+1
                        ]
                    elif previous_move[column_index] < current_move[column_index]:
                        # The piece jumped to the right
                        piece_to_remove = [
                            current_move[row_index] -
                            1, current_move[column_index] - 1
                        ]
                elif self.team == 1 and self.king == False:
                    if previous_move[column_index] > current_move[column_index]:
                        # This piece jumped to the left
                        piece_to_remove = [
                            current_move[0] +
                            1, current_move[1]+1
                        ]
                    elif previous_move[column_index] < current_move[column_index]:
                        # This piece jumped to the right
                        piece_to_remove = [
                            current_move[row_index] -
                            1, current_move[column_index] - 1
                        ]
                # Remove the piece
                game_board_manipulations.append(piece_to_remove)
        print(game_board_manipulations)
        return game_board_manipulations


def is_move_path_valid(valid_move_paths, move_path):
    rowIndex = 0
    columnIndex = 1
    total_move_path_parts = len(move_path)
    is_valid_move = False
    for valid_move_path in valid_move_paths:
        number_of_move_parts_checked = 0
        for move_part in valid_move_path:
            if number_of_move_parts_checked > total_move_path_parts:
                is_valid_move = True
                break
            if move_part[rowIndex] != move_path[number_of_move_parts_checked][rowIndex] or move_part[columnIndex] != move_path[number_of_move_parts_checked][columnIndex]:
                break
            number_of_move_parts_checked += 1
            # This is for when move_path is of length 1
            if total_move_path_parts == 1:
                is_valid_move = True
                break
            if number_of_move_parts_checked == total_move_path_parts:
                # We've check all the parts of the move and we haven't had an invalid entry so it a good move.
                is_valid_move = True
                break
        if is_valid_move == True:
            break
        return is_valid_move


sample_piece = Piece(2, False, [2, 3])
try:
    sample_piece.move(sample_board_1, sample_valid_moves, sample_move_to_1)
except ValueError:
    print("This move is not valid yo.")
sample_piece3 = Piece(1, False, [5, 0])
try:
    sample_piece3.move(sample_board_2, sample_valid_moves_3,
                       sample_bad_move_1)
except ValueError:
    print("This move is not valid yo.")
try:
    sample_piece3.move(sample_board_2, sample_valid_moves_3,
                       sample_good_move_4)
except ValueError:
    print("This move is not valid yo.")
sample_piece_4 = Piece(2, False, [1, 4])
try:
    sample_piece_4.move(sample_board_3, piece_4_valid_moves, piece_4_move_to)
except ValueError:
    print("This move is not valid yo.")
