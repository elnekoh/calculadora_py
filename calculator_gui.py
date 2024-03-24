from calculator import Calculator
from tkinter import *
from icecream import *

class Calculator_gui(Calculator):
    
    #constantes
    #btns
    BTN_WIDTH = 5
    BTN_HEIGHT = 2
    BTN_BORDERWIDTH = 5
    BTN_RELIEF = "raise"
    BTN_PADX = 5
    BTN_PADY= 5

    #display
    DISPLAY_WIDTH = 16
    DISPLAY_PADX = 5
    DISPLAY_PADY = 5
    DISPLAY_FONT = "Calibri 20"

    def __init__(self):
        Calculator.__init__(self)
        self._window = Tk()
        self._window.title("Calculator")

        #display
        self._display = Label(self.window, font=(self.DISPLAY_FONT), text="", anchor="e", justify="right", width=self.DISPLAY_WIDTH)

        #buttons
        self._btn1 = Button(self._window, text= "1", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.btn_click("1"))
        self._btn2 = Button(self._window, text= "2", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.btn_click("2"))
        self._btn3 = Button(self._window, text= "3", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.btn_click("3"))
        self._btn4 = Button(self._window, text= "4", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.btn_click("4"))
        self._btn5 = Button(self._window, text= "5", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.btn_click("5"))
        self._btn6 = Button(self._window, text= "6", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.btn_click("6"))
        self._btn7 = Button(self._window, text= "7", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.btn_click("7"))
        self._btn8 = Button(self._window, text= "8", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.btn_click("8"))
        self._btn9 = Button(self._window, text= "9", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.btn_click("9"))
        self._btn0 = Button(self._window, text= "0", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.btn_click("0"))

        self._btn_del = Button(self._window, text= "DEL", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.btn_click("DEL"))
        self._btn_delAll = Button(self._window, text= "AC", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.btn_click("AC"))
        self._btn_dot = Button(self._window, text= ".", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.btn_click("."))
        self._btn_equal = Button(self._window, text= "=", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.btn_click("="))
        self._btn_sum = Button(self._window, text= "+", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.btn_click("+"))
        self._btn_sub = Button(self._window, text= "-", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.btn_click("-"))
        self._btn_div = Button(self._window, text= "/", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.btn_click("/"))
        self._btn_mult = Button(self._window, text= "*", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.btn_click("*"))

        self.btns_grid()
        self.display_grid()
        self._window.mainloop()

    def display_grid(self):
        self._display.grid(row = 0, column = 0, columnspan = 4, padx = self.DISPLAY_PADX, pady = self.DISPLAY_PADY, sticky="e")

    def btns_grid(self):
        #row
        self._btn_delAll.grid(row = 2, column = 0, padx = self.BTN_PADX, pady = self.BTN_PADY)
        self._btn_del.grid(row = 2, column = 1, columnspan = 2, padx = self.BTN_PADX, pady = self.BTN_PADY)
        self._btn_equal.grid(row = 2, column = 3, padx = self.BTN_PADX, pady = self.BTN_PADY)

        #row2
        self._btn7.grid(row = 3, column = 0, padx = self.BTN_PADX, pady = self.BTN_PADY)
        self._btn8.grid(row = 3, column = 1, padx = self.BTN_PADX, pady = self.BTN_PADY)
        self._btn9.grid(row = 3, column = 2, padx = self.BTN_PADX, pady = self.BTN_PADY)
        self._btn_sum.grid(row = 3, column = 3, padx = self.BTN_PADX, pady = self.BTN_PADY)

        #row3
        self._btn4.grid(row = 4, column = 0, padx = self.BTN_PADX, pady = self.BTN_PADY)
        self._btn5.grid(row = 4, column = 1, padx = self.BTN_PADX, pady = self.BTN_PADY)
        self._btn6.grid(row = 4, column = 2, padx = self.BTN_PADX, pady = self.BTN_PADY)
        self._btn_sub.grid(row = 4, column = 3, padx = self.BTN_PADX, pady = self.BTN_PADY)

        #row4
        self._btn1.grid(row = 5, column = 0, padx = self.BTN_PADX, pady = self.BTN_PADY)
        self._btn2.grid(row = 5, column = 1, padx = self.BTN_PADX, pady = self.BTN_PADY)
        self._btn3.grid(row = 5, column = 2, padx = self.BTN_PADX, pady = self.BTN_PADY)
        self._btn_div.grid(row = 5, column = 3, padx = self.BTN_PADX, pady = self.BTN_PADY)

        #row5
        self._btn_dot.grid(row = 6, column = 0, padx = self.BTN_PADX, pady = self.BTN_PADY)
        self._btn0.grid(row = 6, column = 1, padx = self.BTN_PADX, pady = self.BTN_PADY)
        self._btn_mult.grid(row = 6, column = 3, padx = self.BTN_PADX, pady = self.BTN_PADY)

    @property
    def window(self):
        return self._window

    @property
    def display(self):
        return self._display
    
    def btn_click(self, btn):
        #se obtiene siempre el texto del display
        txt = self.display.cget("text")
        #si el texto es un error, al tocar un boton se borra
        if txt == self.M_ERROR:
            txt = ""

        if btn == "=":
            #esto deberia ser otro metodo!!!
            split = self.split_expression(txt)
            ic(split)
            if split[1] is None or split[2] is None:
                pass
            else:
                txt = str(self.solve(split[0],split[1],split[2]))
                self.display.config(text=txt)

        if btn in ["1","2","3","4","5","6","7","8","9","0"]:
            self.display.config(text=txt+btn)

        if btn == "DEL":
            self.display.config(text=txt[:-1])

        if btn == "AC":
            self.display.config(text="")

        if btn == "." and txt != "":
            #solo puede escribirse un punto si el ultimo char es un numero
            #tambien se controla que no haya otro punto en el numero que se esta escribiendo
            split = self.split_expression(txt)
            if split[1] is None:
                #no hay num2
                if "." in txt or txt == "-":
                    pass
                else:
                    self.display.config(text=txt+btn)
            else:
                #hay num2
                second_number = txt.replace(str(split[0]), "", 1)
                if "." in second_number or txt == "-":
                    pass
                else:
                    self.display.config(text=txt+btn)



        if btn in ["+","*","/"] and txt != "":
            if "." in txt[-1]: # si el ultimo char es un punto, se borra
                txt = txt[:-1]
            split = self.split_expression(txt)
            #En ambos if, se evalua si split[0] es None, si lo es, entonces no llego una expression
            if split[0] is not None and split[2] is None:
                #si split[2] es None, entonces solo esta el numero 1 en la expresion
                txt = txt + btn 
            elif split[0] is not None and split[1] is not None:
                #hay numero 2 y operador, tratamos de resolver la expresion, y txt se convierte en el resultado + el operador
                try:
                    txt = str(self.solve(split[0],split[1],split[2]))+btn             
                except:
                    txt = self.M_ERROR
            else:
                txt = self.M_ERROR #ante cualquier situacion no esperada, se muestra un error
            self.display.config(text=txt) 
        
        if btn =="-":
            if txt == "": 
                txt = "-"
            else:
                #si el texto no esta vacio, se controla si el ultimo char es un operador
                split = self.split_expression(txt)
                if split[0] is not None and split[2] is None: #si exite numero 1, y el operador no, a txt se me agrega btn
                    txt = txt + btn
                else:
                    #pero si el operador si existe, entonces controlamos si el numero 2 esta vacio
                    #si esta vacio, entonces se agrega el simbolo negativo
                    txt_split2 = txt.replace(str(split[0])+str(split[2]), "", 1)
                    if txt_split2 == "":
                        txt = txt + btn
                            
            self.display.config(text = txt)


c = Calculator_gui()
