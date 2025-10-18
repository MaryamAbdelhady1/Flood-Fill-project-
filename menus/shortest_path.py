from tkinter import *
from controls import *
from dfs import *
from bfs import *

class Algorithm_menu():
    def __init__(self , root):

        Label(root, text="Choose Algorithm : ", bg = "gray" , fg="black", font=('Arial Bold', 15)).place(x=200, y=140)
        Button(root, text = "DFS", bg = '#FFF8DC', fg = "black", font=('Arial Bold', 10), width=50, height=5 , command = lambda : ( root.destroy() , Controls('dfs') ) ).place( x=200, y=170)
        Button(root, text = "BFS", bg = '#FFF8DC' , fg = "black", font=('Arial Bold', 10), width=50, height=5 , command = lambda : ( root.destroy() , Controls('bfs') ) ).place( x=200, y=300)

        root.mainloop()








