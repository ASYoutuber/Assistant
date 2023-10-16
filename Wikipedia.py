from tkinter import *
import wikipedia

def Wikipedia():
    window = Tk()

    title = Label(window, text = "Welcome to Wikipedia!", bg = "cyan", fg = "white", font = ("Times New Roman", 40), width = 45)
    lbl = Label(window, text = "Enter the topic you need to search for!", bg = "cyan", fg = "white", font = ("Times New Roman", 20), width = 32)
    txt = Entry(window, width = 25)
    btn = Button(window, text = "Submit", font = ("Times New Roman", 20), width = 25, command = lambda: Search(txt, result))
    result = Message(window)

    title.grid(row = 0, column = 2)
    lbl.grid(row = 1, column = 2)
    txt.grid(row = 2, column = 2)
    btn.grid(row = 3, column = 2)
    result.grid(row = 4, column = 2)

    window.geometry("900x700")
    window.title("Wikipedia")
    window.mainloop()

def Search(txt, result):
    try:
        search = wikipedia.summary(txt.get())
        result.configure(text = search, bg = "cyan", fg = "white", font = ("Times New Roman", 20))
    except wikipedia.DisambiguationError:
        result.configure(text = "Too many results available please be specific!", bg = "cyan", fg = "white", font = ("Times New Roman", 20))