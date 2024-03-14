from calculator import Calculator
from tkinter import *

class Calculator_gui(Calculator):

    def __init__(self):
        Calculator.__init__(self)
        self._window = Tk()
        self._window.title("Calculator")

        #display
        self._display = Label(self.window, font=("Calibri 20"), text="hola", anchor="e", justify="right", width="16")

        #buttons
        self._btn1 = Button(self._window, text= "1", width = 5, height = 2, borderwidth=5, relief="raised")
        self._btn2 = Button(self._window, text= "2", width = 5, height = 2, borderwidth=5, relief="raised")
        self._btn3 = Button(self._window, text= "3", width = 5, height = 2, borderwidth=5, relief="raised")
        self._btn4 = Button(self._window, text= "4", width = 5, height = 2, borderwidth=5, relief="raised")
        self._btn5 = Button(self._window, text= "5", width = 5, height = 2, borderwidth=5, relief="raised")
        self._btn6 = Button(self._window, text= "6", width = 5, height = 2, borderwidth=5, relief="raised")
        self._btn7 = Button(self._window, text= "7", width = 5, height = 2, borderwidth=5, relief="raised")
        self._btn8 = Button(self._window, text= "8", width = 5, height = 2, borderwidth=5, relief="raised")
        self._btn9 = Button(self._window, text= "9", width = 5, height = 2, borderwidth=5, relief="raised")
        self._btn0 = Button(self._window, text= "0", width = 5, height = 2, borderwidth=5, relief="raised")

        self._btn_del = Button(self._window, text= "DEL", width = 5, height = 2, borderwidth=5, relief="raised")
        self._btn_delAll = Button(self._window, text= "AC", width = 5, height = 2, borderwidth=5, relief="raised")
        self._btn_dot = Button(self._window, text= ".", width = 5, height = 2, borderwidth=5, relief="raised")
        self._btn_equal = Button(self._window, text= "=", width = 5, height = 2, borderwidth=5, relief="raised")
        self._btn_sum = Button(self._window, text= "+", width = 5, height = 2, borderwidth=5, relief="raised")
        self._btn_sub = Button(self._window, text= "-", width = 5, height = 2, borderwidth=5, relief="raised")
        self._btn_div = Button(self._window, text= "/", width = 5, height = 2, borderwidth=5, relief="raised")
        self._btn_mult = Button(self._window, text= "*", width = 5, height = 2, borderwidth=5, relief="raised")

        self.btns_grid()
        self.display_grid()
        self._window.mainloop()

    def display_grid(self):
        self._display.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5, sticky="e")

    def btns_grid(self):
        #row
        self._btn_delAll.grid(row = 2, column = 0, padx = 5, pady = 5)
        self._btn_del.grid(row = 2, column = 1, columnspan = 2, padx = 5, pady = 5)
        self._btn_equal.grid(row = 2, column = 3, padx = 5, pady = 5)

        #row2
        self._btn7.grid(row = 3, column = 0, padx = 5, pady = 5)
        self._btn8.grid(row = 3, column = 1, padx = 5, pady = 5)
        self._btn9.grid(row = 3, column = 2, padx = 5, pady = 5)
        self._btn_sum.grid(row = 3, column = 3, padx = 5, pady = 5)

        #row3
        self._btn4.grid(row = 4, column = 0, padx = 5, pady = 5)
        self._btn5.grid(row = 4, column = 1, padx = 5, pady = 5)
        self._btn6.grid(row = 4, column = 2, padx = 5, pady = 5)
        self._btn_sub.grid(row = 4, column = 3, padx = 5, pady = 5)

        #row4
        self._btn1.grid(row = 5, column = 0, padx = 5, pady = 5)
        self._btn2.grid(row = 5, column = 1, padx = 5, pady = 5)
        self._btn3.grid(row = 5, column = 2, padx = 5, pady = 5)
        self._btn_div.grid(row = 5, column = 3, padx = 5, pady = 5)

        #row5
        self._btn_dot.grid(row = 6, column = 0, padx = 5, pady = 5)
        self._btn0.grid(row = 6, column = 1, padx = 5, pady = 5)
        self._btn_mult.grid(row = 6, column = 3, padx = 5, pady = 5)

    @property
    def window(self):
        return self._window

    @property
    def display(self):
        return self._display
    

c = Calculator_gui()