from tkinter import *
from PIL import ImageTk,Image
#from tkinter.ttk import *


root = Tk()
root.title("Checkers")

redRow = {}
blackRow = {}

# Created Squares and added them to dictionary
squares = range(0,32,2)
for x in squares:
    redRow[x] = Button(root, state=DISABLED, bg="red", padx=40, pady=35)
    redRow[x+1] = Button(root, bg="black", padx=40, pady=35)

for x in squares:
    blackRow[x] = Button(root, bg="black", padx=40, pady=35)
    blackRow[x+1] = Button(root, state=DISABLED, bg="red", padx=40, pady=35)




#creatinig the white pieces
black_pieces = {}
my_w_imgs = {}
for x in range(12):
    my_w_imgs[x] = ImageTk.PhotoImage(Image.open("nesnej/ludum/output2-onlinepngtools.png"))
for x in range(12):
    black_pieces[x] = Button(root, bg='pink', image=my_w_imgs[x])
#print(black_pieces)

#creating the black pieces

white_p1 = {}
my_b_imgs ={}
for x in range(12):
    my_b_imgs[x] = ImageTk.PhotoImage(Image.open("nesnej/ludum/output-onlinepngtools.png"))
for x in range(12):
    white_p1[x] = Button(root, bg='purple', image=my_b_imgs[x])
#print(white_p1)


#Placing the black pieces onto the board
row_c = 0 
column_c = 1
black_piece_location = []
for key, value in black_pieces.items():
    black_piece_location.append([row_c, column_c])
    value.grid(row=row_c, column=column_c)
    if column_c == 7:
        row_c += 1
        column_c = 0
    elif column_c == 6:
        row_c += 1
        column_c = 1
    else:
        column_c += 2

#Placing the white pieces onto the board
bot_row = 5
bot_column = 0
white_piece_location = []
for key, value in white_p1.items():
    white_piece_location.append([bot_row, bot_column])
    value.grid(row=bot_row, column=bot_column)
    if bot_column == 6:
        bot_row += 1
        bot_column = 1
    elif bot_column== 7:
        bot_row += 1
        bot_column = 0
    else:
        bot_column += 2


# From dictionary put those squares onto window
i = 0
k = 0
for j in range(0,7,2):
    for x in range(8):
        redRow[i].grid(row=j, column=x)
        i += 1
        
    for x in range(8):
        blackRow[k].grid(row=j+1,column=x)
        k += 1


#To move location of piece simply use this line below but change the x to the piece you want to move, y the row where you want it, and z the column where you want it
#black_pieces[1].grid(row=3, column=2)


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

#for 

"""
game_board = [
    [x,2,x,2,x,2,x,2],
    [2,x,2,x,2,x,o,x],
    [x,2,x,2,x,2,x,2],
    [o,x,o,x,o,x,1,x],
    [x,o,x,2,x,o,x,o],
    [1,x,1,x,1,x,1,x],
    [x,o,x,1,x,1,x,o],
    [1,x,1,x,1,x,1,x],

]
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
#print(simple_board)
for piece in black_piece_location:
    simple_board[piece[0]][piece[1]] = '2'
for piece in white_piece_location:
    simple_board[piece[0]][piece[1]] = '1'

print(simple_board)
mainloop()