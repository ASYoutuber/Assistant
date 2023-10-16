from tkinter import *
from tkinter import messagebox
import pickle
def Remind():
    window = Tk()

    title = Label(window, text = "Welcome to Reminders!", bg = "blue", fg = "white", font = ("Times New Roman", 40), width = 45)
    list_ = Listbox(window, width = 25)

    txt = Entry(window, width = 25)
    btn = Button(window, text = "Add task", bg = "light blue", fg = "black", font = ("Times New Roman", 20), width = 25, command = lambda: Add_task(txt, list_))

    btn1 = Button(window, text = "Remove task", bg = "blue", fg = "black", font = ("Times New Roman", 20), width = 25, command = lambda: Remove_task(list_))

    btn2 = Button(window, text = "Load task", bg = "light blue", fg = "black", font = ("Times New Roman", 20), width = 25, command = lambda: Load_task(list_))

    btn3 = Button(window, text = "Save task", bg = "blue", fg = "black", font = ("Times New Roman", 20), width = 25, command = lambda: Save_task(list_))

    title.grid(row = 0, column = 2)
    list_.grid(row = 1, column = 2)
    txt.grid(row = 2, column = 2)
    btn.grid(row = 3, column = 2)
    btn1.grid(row = 4, column = 2)
    btn2.grid(row = 6, column = 2)
    btn3.grid(row = 5, column = 2)
    
    window.geometry("900x600")
    window.title("Reminders")
    window.mainloop()

def Add_task(txt, list_):
    if (len(txt.get()) > 0):
        list_.insert(END, txt.get())
        txt.delete(0, END)
    else:
        messagebox.showwarning(title = "Warning", message = "You must type a task before entering!")

def Remove_task(list_):
    try:
        index = list_.curselection()[0]
        list_.delete(index)
    except:
        messagebox.showwarning(title = "Warning", message = "You must select a task before deleting!")

def Save_task(list_):
    saved_reminders = open("Saved_reminders.dat", "wb")
    list_r = list_.get(0, list_.size())
    pickle.dump(list_r, saved_reminders)
    saved_reminders.close()

def Load_task(list_):
    saved_reminders = open("Saved_reminders.dat", "rb")
    tasks = pickle.load(saved_reminders)
    list_.delete(0, END)
    for i in tasks:
        list_.insert(END, i)
    saved_reminders.close()