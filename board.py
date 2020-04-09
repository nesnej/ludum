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
    redRow[x] = Button(root, bg="red", padx=40, pady=35)
    redRow[x+1] = Button(root, bg="black", padx=40, pady=35)

for x in squares:
    blackRow[x] = Button(root, bg="black", padx=40, pady=35)
    blackRow[x+1] = Button(root, bg="red", padx=40, pady=35)


#creatinig the white pieces
white_pieces = {}
my_w_imgs = {}
for x in range(12):
    my_w_imgs[x] = ImageTk.PhotoImage(Image.open("nesnej/ludum/output2-onlinepngtools.png"))
for x in range(12):
    white_pieces[x] = Button(root, image=my_w_imgs[x])
print(white_pieces)

#creating the black pieces

black_pieces = {}
my_b_imgs ={}
for x in range(12):
    my_b_imgs[x] = ImageTk.PhotoImage(Image.open("nesnej/ludum/output-onlinepngtools.png"))
for x in range(12):
    black_pieces[x] = Button(root, image=my_b_imgs[x])
print(black_pieces)


#Placing the white pieces onto the board
row_c = 0 
column_c = 1
for key, value in white_pieces.items():
    value.grid(row=row_c, column=column_c)
    if column_c == 7:
        row_c += 1
        column_c = 0
    elif column_c == 6:
        row_c += 1
        column_c = 1
    else:
        column_c += 2

#Placing the Black pieces onto the board
bot_row = 5
bot_column = 0
for key, value in black_pieces.items():
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
#white_pieces[x].grid(row=y, column=z)



mainloop()