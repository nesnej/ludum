from tkinter import *
from PIL import ImageTk, Image
from piece import Piece
from validmoves import valid_moves2
# from tkinter.ttk import *


root = Tk()
root.title("Checkers")
x = 'x'
o = 'o'
game_board = [
    [x, 2, x, 2, x, 2, x, 2],
    [2, x, 2, x, 2, x, 2, x],
    [x, 2, x, 2, x, 2, x, 2],
    [o, x, o, x, o, x, o, x],
    [x, o, x, o, x, o, x, o],
    [1, x, 1, x, 1, x, 1, x],
    [x, 1, x, 1, x, 1, x, 1],
    [1, x, 1, x, 1, x, 1, x],
]

redRow = {}
blackRow = {}

# Created Squares and added them to dictionary
squares = range(0, 32, 2)
for x in squares:
    redRow[x] = Button(root, state=DISABLED, bg="red", padx=40, pady=35)
    redRow[x+1] = Button(root, bg="black", padx=40, pady=35)

for x in squares:
    blackRow[x] = Button(root, bg="black", padx=40, pady=35)
    blackRow[x+1] = Button(root, state=DISABLED, bg="red", padx=40, pady=35)

gvalid_moves = []
piece_wanting_to_move = Piece(0, False, [0, 0])
gbutton = Button(root)


def runMove(square):
    global game_board
    global gvalid_moves
    print(game_board)
    print("VALID MOVES", gvalid_moves)

    row = square.grid_info()["row"]
    col = square.grid_info()["column"]

    move_path = []
    for move in gvalid_moves:
        if move[len(move)-1] == [int(row), int(col)]:
            move_path = move

    print(move_path)

    game_board_manipulations = piece_wanting_to_move.move(
        game_board, gvalid_moves, move_path)

    gbutton.grid(
        row=game_board_manipulations[0][0], column=game_board_manipulations[0][1])

    i = 0
    for manip in game_board_manipulations:
        if i == 0:
            game_board[manip[0]][manip[1]] = piece_wanting_to_move.team
        else:
            game_board[manip[0]][manip[1]] = o
        i += 1


def save_global_piece(valid_moves):
    global game_board
    global gvalid_moves
    gvalid_moves = valid_moves
    print(gvalid_moves)
    print(piece_wanting_to_move)


def getLocation(button):
    global gbutton
    global game_board
    gbutton = button
    row = button.grid_info()["row"]
    print(row)
    col = button.grid_info()["column"]
    print(col)
    color = button.cget("bg")
    team = 0
    if color == "pink":
        team = 2
    elif color == "purple":
        team = 1
    print(team)

    global piece_wanting_to_move
    piece = Piece(team, False, [int(row), int(col)])
    print("PIECE POSITION", piece.position)
    piece_wanting_to_move = piece
    return piece


    # creatinig the white pieces
black_pieces = {}
my_w_imgs = {}
for x in range(12):
    my_w_imgs[x] = ImageTk.PhotoImage(Image.open(
        "nesnej/ludum/output2-onlinepngtools.png"))
for x in range(12):
    black_pieces[x] = Button(
        root, bg='pink', image=my_w_imgs[x])
# print(black_pieces)

# creating the black pieces

white_p1 = {}
my_b_imgs = {}
for x in range(12):
    my_b_imgs[x] = ImageTk.PhotoImage(Image.open(
        "nesnej/ludum/output-onlinepngtools.png"))
for x in range(12):
    white_p1[x] = Button(root, bg='purple', image=my_b_imgs[x])
# print(white_p1)


# Placing the black pieces onto the board

row_c = 0
column_c = 1
black_piece_location = []
for key, value in black_pieces.items():
    black_piece_location.append([row_c, column_c])
    value.grid(row=row_c, column=column_c)
    def remember(piece):
        global game_board
        value.config(command=lambda: save_global_piece(valid_moves2(
            game_board, getLocation(piece))))
    remember(value)

    if column_c == 7:
        row_c += 1
        column_c = 0
    elif column_c == 6:
        row_c += 1
        column_c = 1
    else:
        column_c += 2

# Placing the white pieces onto the board
bot_row = 5
bot_column = 0
white_piece_location = []
for key, value in white_p1.items():
    white_piece_location.append([bot_row, bot_column])
    value.grid(row=bot_row, column=bot_column)
    if bot_column == 6:
        bot_row += 1
        bot_column = 1
    elif bot_column == 7:
        bot_row += 1
        bot_column = 0
    else:
        bot_column += 2


# From dictionary put those squares onto window
i = 0
k = 0
for j in range(0, 7, 2):
    for x in range(8):
        redRow[i].grid(row=j, column=x)

        i += 1

    for x in range(8):
        blackRow[k].grid(row=j+1, column=x)

        def remember2(square):
            square.config(command=lambda: runMove(square))
        remember2(blackRow[k])
        k += 1


# To move location of piece simply use this line below but change the x to the piece you want to move, y the row where you want it, and z the column where you want it
# black_pieces[1].grid(row=3, column=2)


board = []
rows = []

for x in range(4):
    rows = []
    for x in range(8):
        rows.append(redRow[x])
    board.append(rows)
    rows = []
    for x in range(8):
        rows.append(blackRow[x])
    board.append(rows)

pieces = []

# for

"""

"""


simple_board = []
for row in board:
    simple_row = []
    for square in row:
        simple_color = square.cget('bg')

        if simple_color == 'black':
            simple_row.append('o')
        elif simple_color == 'red':
            simple_row.append('x')
    simple_board.append(simple_row)
# print(simple_board)
for piece in black_piece_location:
    simple_board[piece[0]][piece[1]] = '2'
for piece in white_piece_location:
    simple_board[piece[0]][piece[1]] = '1'

print(simple_board)
mainloop()
