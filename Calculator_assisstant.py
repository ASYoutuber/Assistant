from tkinter import *
from Weather_app import Weather_app
from Translator import Translator_app
from Calculator import Calculator_app
from Wikipedia import Wikipedia
from Currency_converter import Currency_Convert_app
from Reminders import Remind

window = Tk()

title = Label(window, text = "Calculator Assistant", bg = "white", fg = "black", font = ("Times New Roman", 40), width = 45)
btn = Button(window, text = "Calculator", bg = "white", fg = "black", font = ("Times New Roman", 20), width = 25, command = Calculator_app)
btn2 = Button(window, text = "Weather app", bg = "white", fg = "black", font = ("Times New Roman", 20), width = 25, command = Weather_app)
btn3 = Button(window, text = "Translator", bg = "white", fg = "black", font = ("Times New Roman", 20), width = 25, command = Translator_app)
btn4 = Button(window, text = "Currency Converter", bg = "white", fg = "black", font = ("Times New Roman", 20), width = 25, command = Currency_Convert_app)
btn5 = Button(window, text = "Wikipedia", bg = "white", fg = "black", font = ("Times New Roman", 20), width = 25, command = Wikipedia)
btn6 = Button(window, text = "Reminders", bg = "white", fg = "black", font = ("Times New Roman", 20), width = 25, command = Remind)

title.grid(row = 0, column = 2)
btn.grid(row = 1, column = 2)
btn2.grid(row = 2, column = 2)
btn3.grid(row = 3, column = 2)
btn4.grid(row = 4, column = 2)
btn5.grid(row = 5, column = 2)
btn6.grid(row = 6, column = 2)

window.geometry("900x600")
window.title("Calculator assistant")
window.configure(bg = "black")
window.mainloop()