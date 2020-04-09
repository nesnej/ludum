from tkinter import *

root = Tk()
root.title("Checkers")

redRow = {}
blackRow = {}

squares = range(0,32,2)
for x in squares:
    redRow[x] = Button(root, bg="red", padx=40, pady=35)
    redRow[x+1] = Button(root, bg="black", padx=40, pady=35)

for x in squares:
    blackRow[x] = Button(root, bg="black", padx=40, pady=35)
    blackRow[x+1] = Button(root, bg="red", padx=40, pady=35)


i = 0
k = 0
for j in range(0,7,2):
    for x in range(8):
        redRow[i].grid(row=j, column=x)
        i += 1
        print(i)


    for x in range(8):
        blackRow[k].grid(row=j+1,column=x)
        k += 1


#print(blackRow)
#print(redRow)
mainloop()