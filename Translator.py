from tkinter import *
from googletrans import Translator, LANGUAGES
from tkinter import ttk

def Translator_app():
  window = Tk()

  title = Label(window, text = "Welcome to the Translator!", bg = "cyan", fg = "white", font = ("Times New Roman", 40), width = 45)
  lbl = Label(window, text = "Enter a sentence to be translated!", bg = "cyan", fg = "white", font = ("Times New Roman", 20), width = 30)
  txt = Entry(window, width = 20)
  x = list(LANGUAGES.values())
  dest = ttk.Combobox(window, values = x, width = 20, font = ("Times New Roman", 20))
  lbl2 = Label(window, text = "Answer will appear here!", bg = "white", fg = "black", font = ("Times New Roman", 20), width = 20)
  btn = Button(window, text = "Submit", bg = "white", fg = "black", command = lambda: Translate(txt, dest, lbl2))

  title.grid(row = 0, column = 2)
  lbl.grid(row = 1, column = 2)
  txt.grid(row = 2, column = 2)
  dest.grid(row = 3, column = 2)
  lbl2.grid(row = 4, column = 2)
  btn.grid(row = 5, column = 2)

  window.geometry("900x600")
  window.title("Translator")
  window.mainloop()

def Translate(txt, dest, lbl2):
  translator = Translator()
  translated = translator.translate(txt.get(), dest.get())
  lbl2.configure(text = translated.text)