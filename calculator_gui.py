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
        self._display_text = ""
        self._window = Tk()
        self._window.title("Calculator")

        #display
        self._display = Label(self.window, font=(self.DISPLAY_FONT), text="", anchor="e", justify="right", width=self.DISPLAY_WIDTH)

        #buttons
        self._btn1 = Button(self._window, text= "1", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.click("1"))
        self._btn2 = Button(self._window, text= "2", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.click("2"))
        self._btn3 = Button(self._window, text= "3", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.click("3"))
        self._btn4 = Button(self._window, text= "4", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.click("4"))
        self._btn5 = Button(self._window, text= "5", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.click("5"))
        self._btn6 = Button(self._window, text= "6", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.click("6"))
        self._btn7 = Button(self._window, text= "7", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.click("7"))
        self._btn8 = Button(self._window, text= "8", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.click("8"))
        self._btn9 = Button(self._window, text= "9", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.click("9"))
        self._btn0 = Button(self._window, text= "0", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.click("0"))

        self._btn_del = Button(self._window, text= "DEL", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.click("DEL"))
        self._btn_delAll = Button(self._window, text= "AC", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.click("AC"))
        self._btn_dot = Button(self._window, text= ".", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.click("."))
        self._btn_equal = Button(self._window, text= "=", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.click("="))
        self._btn_sum = Button(self._window, text= "+", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.click("+"))
        self._btn_sub = Button(self._window, text= "-", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.click("-"))
        self._btn_div = Button(self._window, text= "/", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.click("/"))
        self._btn_mult = Button(self._window, text= "*", width = self.BTN_WIDTH, height = self.BTN_HEIGHT, borderwidth = self.BTN_BORDERWIDTH, relief = self.BTN_RELIEF, command = lambda: self.click("*"))

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
    
    @property
    def display_text(self):
        return self._display_text
    
    @display_text.setter
    def display_text(self, new_text):
        self._display_text = new_text
        self.refresh_display()
    
    def refresh_display(self):
        self.display.config(text = self.display_text)

    def add_to_display_text(self, text):
        self.display_text = self.display_text + text
    
    def _delete_all(self):
        self.display_text = ""
    
    def _delete_last_char(self):
        self.display_text = self.display_text[:-1]

    def click(self, pressed_button):
        txt = self.display_text

        if self.display_text == self.MESSAGE_ERROR:
            self._delete_all()

        splitted_expression = self.split_expression(self.display_text)
        number1 = splitted_expression[0]
        number2 = splitted_expression[1]
        operator = splitted_expression[2]

        if pressed_button == "=":
            if  number1 is None or operator is None:
                pass
            else:
                self.display_text = str(self.solve(number1,number2,operator))

        if pressed_button in ["1","2","3","4","5","6","7","8","9","0"]:
            self.add_to_display_text(pressed_button)

        if pressed_button == "DEL":
            self._delete_last_char()

        if pressed_button == "AC":
            self._delete_all()

        if pressed_button == "." and txt != "":
            #solo puede escribirse un punto si el ultimo char es un numero
            #también se controla que no haya otro punto en el numero que se esta escribiendo
            if number2 is None:
                if "." in self.display_text or self.display_text == "-":
                    pass
                else:
                    self.add_to_display_text(pressed_button)
            else:
                #hay num2
                number2_in_display_text = self.display_text.replace(str(number1)+operator, "", 1)
                if "." in number2_in_display_text or number2_in_display_text == "" or self.display_text == "-":
                    pass
                else:
                    self.add_to_display_text(pressed_button)



        if pressed_button in ["+","*","/"] and self.display_text != "":
            if "." in self.display_text[-1]: # si el ultimo char es un punto, se borra
                self._delete_last_char()
            #En ambos if, se evalúa si number1 es None, si lo es, entonces no llego una expression
            if number1 is not None and operator is None:
                self.add_to_display_text(pressed_button) 
            elif number1 is not None and number2 is not None:
                #hay numero 2 y operador, tratamos de resolver la expresión, y txt se convierte en el resultado + el operador
                try:
                    self.display_text = str(self.solve(number1, number2, operator)) + pressed_button             
                except:
                    self.display_text = self.M_ERROR
            elif number1 is not None and number2 is None and operator is not None:
                pass
            else:
                self.display_text = self.M_ERROR
        
        if pressed_button =="-":
            if self.display_text == "": 
                self.add_to_display_text(pressed_button)
            else:
                if number1 is not None and operator is None: 
                    self.add_to_display_text(pressed_button)
                elif number1 is not None and operator is not None:
                    number2_in_display_text = self.display_text.replace(str(number1)+str(operator), "", 1)
                    if number2_in_display_text == "":
                        self.add_to_display_text(pressed_button)
                elif number1 is not None and number2 is not None and operator is not None:
                    try:
                        self.display_text = str(self.solve(number1,number2,operator)) + pressed_button             
                    except:
                        self.display_text = self.M_ERROR
                else:
                    self.display_text = self.M_ERROR


c = Calculator_gui()
