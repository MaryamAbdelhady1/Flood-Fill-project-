from tkinter import *
from controls import *
from shortest_path import *

root = Tk()
class Start_menu():
    def __init__(self ):
        root.title("Start")
        root.geometry("800x600")
        root.resizable(False, False)
        # root.config(bg = '#4B0082' )
        root.config(bg = '#D8BFD8' )

        Button(root , text = "Calculate shortest path" , bg = '#FFF8DC' , fg = "black" , font = ('Arial Bold' , 10) , width = 50 , height = 5 , command = lambda : Algorithm_menu(root)).place(x = 200 , y = 170 )
        Button(root , text = "Calculate minimum weight path" , bg = '#FFF8DC' , fg = "black" , font = ('Arial Bold' , 10) , width = 50 , height = 5 , command = lambda : (root.destroy() , Controls('dijkstra') ) ).place(x = 200, y = 300 )

        root.mainloop()






