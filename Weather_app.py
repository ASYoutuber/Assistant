from tkinter import *
import json
import requests

def Weather_app():
  window = Tk()

  title = Label(window, text = "Welcome to the Weather App!", bg = "cyan", fg = "white", font = ("Arial", 40), width = 45)
  lbl = Label(window, text = "Enter the name of a city!", bg = "cyan", fg = "white", font = ("Times New Roman", 20))
  txt = Entry(window, width = 30, font = ("Arial", 20))
  btn = Button(window, text = "Submit", bg = "cyan", fg = "black", command = lambda: weather(txt, result, description))
  result = Label(window, text = "", fg = "black", width = 50, height = 10)
  space = Label(window)
  description = Label(window, text = "", fg = "White")

  title.grid(row = 0, column = 2)
  lbl.grid(row = 1, column = 2)
  txt.grid(row = 2, column = 2)
  btn.grid(row = 3, column = 2)
  result.grid(row = 4, column = 2)
  space.grid(row = 5, column = 2)
  description.grid(row = 6, column = 2)

  window.geometry("900x600")
  window.title("Weather App")
  window.mainloop()

def weather(txt, result, description):
  location = txt.get()
  api = "http://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=cf68af6b1720ee2d0fb9db397e7632d2"
  response = requests.get(api)
  city = response.json()
  x = city["main"]
  current_temperature = round(x["temp"] - 273, 2)
  feels_like = round(x["feels_like"] - 273, 2)
  min_temp = round(x["temp_min"] - 273, 2)
  max_temp = round(x["temp_max"] - 273, 2)
  humidity = round(x["humidity"], 2)
  result.configure(text = "Minimum temperature: " + str(min_temp) + "\nMaximum Temprature: " + str(max_temp) + "\nCurrent Temprature: " + str(current_temperature) + "\nFeels Like: " + str(feels_like) + "\nHumidity: " + str(humidity), font = ("Times New Roman", 25))
  if (current_temperature > 25):
    result.configure(bg = "yellow")
    description.configure(text = "It appears to be hot", bg = "yellow")
  else:
    result.configure(bg = "light blue")
    description.configure(text = "It appears to be cold", bg = "light blue")