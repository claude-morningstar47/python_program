from tkinter import *


def callback(r, c, player):
    b[r][c].configure(text=player)
    player = 'O' if player == 'X' else 'O'


root = Tk()
b = [
    [Button(font=('Verdana', 56), width=3, bg='yellow', command=lambda r=i, c=j: callback(r, c, player)) for j in range(3)] for i in range(3)
]
for row in b:
    for col in row:
        col.grid(row=b.index(row), column=row.index(col))

player = 'X'
mainloop()
