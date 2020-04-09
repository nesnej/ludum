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



white_pieces = {}
my_imgs = {}
for x in range(12):
    my_imgs[x] = ImageTk.PhotoImage(Image.open("nesnej/ludum/output-onlinepngtools.png"))
for x in range(12):
    white_pieces[x] = Button(root, image=my_imgs[x])


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


# Checkers piece image





mainloop()