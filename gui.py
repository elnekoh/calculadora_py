from tkinter import *

window = Tk()
window.title("Calculator")

    

#display
display = Label(window, font=("Calibri 20"), text="", anchor="e", justify="right", width="16")
display.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5, sticky="e")

#buttons btn = Button(window, text= "", width = 5, height = 2)
btn1 = Button(window, text= "1", width = 5, height = 2, borderwidth=5, relief="raised")
btn2 = Button(window, text= "2", width = 5, height = 2, borderwidth=5, relief="raised")
btn3 = Button(window, text= "3", width = 5, height = 2, borderwidth=5, relief="raised")
btn4 = Button(window, text= "4", width = 5, height = 2, borderwidth=5, relief="raised")
btn5 = Button(window, text= "5", width = 5, height = 2, borderwidth=5, relief="raised")
btn6 = Button(window, text= "6", width = 5, height = 2, borderwidth=5, relief="raised")
btn7 = Button(window, text= "7", width = 5, height = 2, borderwidth=5, relief="raised")
btn8 = Button(window, text= "8", width = 5, height = 2, borderwidth=5, relief="raised")
btn9 = Button(window, text= "9", width = 5, height = 2, borderwidth=5, relief="raised")
btn0 = Button(window, text= "0", width = 5, height = 2, borderwidth=5, relief="raised")

btn_del = Button(window, text= "DEL", width = 5, height = 2, borderwidth=5, relief="raised")
btn_delAll = Button(window, text= "AC", width = 5, height = 2, borderwidth=5, relief="raised")
btn_dot = Button(window, text= ".", width = 5, height = 2, borderwidth=5, relief="raised")
btn_equal = Button(window, text= "=", width = 5, height = 2, borderwidth=5, relief="raised")
btn_sum = Button(window, text= "+", width = 5, height = 2, borderwidth=5, relief="raised")
btn_sub = Button(window, text= "-", width = 5, height = 2, borderwidth=5, relief="raised")
btn_div = Button(window, text= "/", width = 5, height = 2, borderwidth=5, relief="raised")
btn_mult = Button(window, text= "*", width = 5, height = 2, borderwidth=5, relief="raised")

#btn.grid(row = , column = , padx = 5, pady = 5)
#row1
btn_delAll.grid(row = 2, column = 0, padx = 5, pady = 5)
btn_del.grid(row = 2, column = 1, columnspan = 2, padx = 5, pady = 5)
btn_equal.grid(row = 2, column = 3, padx = 5, pady = 5)

#row2
btn7.grid(row = 3, column = 0, padx = 5, pady = 5)
btn8.grid(row = 3, column = 1, padx = 5, pady = 5)
btn9.grid(row = 3, column = 2, padx = 5, pady = 5)
btn_sum.grid(row = 3, column = 3, padx = 5, pady = 5)

#row3
btn4.grid(row = 4, column = 0, padx = 5, pady = 5)
btn5.grid(row = 4, column = 1, padx = 5, pady = 5)
btn6.grid(row = 4, column = 2, padx = 5, pady = 5)
btn_sub.grid(row = 4, column = 3, padx = 5, pady = 5)

#row4
btn1.grid(row = 5, column = 0, padx = 5, pady = 5)
btn2.grid(row = 5, column = 1, padx = 5, pady = 5)
btn3.grid(row = 5, column = 2, padx = 5, pady = 5)
btn_div.grid(row = 5, column = 3, padx = 5, pady = 5)

#row5
btn_dot.grid(row = 6, column = 0, padx = 5, pady = 5)
btn0.grid(row = 6, column = 1, padx = 5, pady = 5)
btn_mult.grid(row = 6, column = 3, padx = 5, pady = 5)


window.mainloop()