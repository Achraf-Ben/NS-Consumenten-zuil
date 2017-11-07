import forecastio
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import time
import datetime

def weersvoorspelling():
    '''Returns weather forecast using the Darsky API'''
    api_key = "dca7849ad2985d67e63bdce010c191ee"
    # Utrecht
    latitude = 52.0884851
    longitude = 5.1180588
    forecast = forecastio.load_forecast(api_key, latitude, longitude)
    byHour = forecast.daily()
    weerZin = byHour.summary
    return weerZin

# Tkinter Window
class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        '''Creation of init_window'''
        self.master.title("NS - Twitter & Weer") #Titel of the master widget
        self.pack(fill=BOTH, expand=1)  # Allow full space of root

        # NS Logo
        load = Image.open("ns_logo.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

        # Intro tekst
        intro = Label(self, text="Welkom bij de NS Twitter Zuil. \n")
        intro.pack()

        # Huidige weersomstandigheden
        tekst = Label(self, text="Huidige weersomstandigheden in Utrecht:\n " + weersvoorspelling())
        tekst.pack()

        # Show Tweets
        self.label = Label(self, text='Meest recente tweets:', height=2, padx=15, font=("Helvetica", 16), fg="white")
        self.label.configure(background='DeepSkyBlue2')
        self.label.pack()


root = Tk() #Creates root window
root.geometry("1366x768") # Window size
app = Window(root) #Create the instance
root.mainloop() # Start mainloop to show it

# NS Kleur geel = #FFC917

""""
Bronnen:
https://pypi.python.org/pypi/python-forecastio/
http://tweepy.readthedocs.io/en/v3.5.0/api.html
https://pythonprogramming.net/python-3-tkinter-basics-tutorial/
https://pythonprogramming.net/tkinter-python-3-tutorial-adding-buttons/?completed=/python-3-tkinter-basics-tutorial/
https://pythonprogramming.net/tkinter-adding-text-images/
https://pythonprogramming.net/twitter-api-streaming-tweets-python-tutorial/?completed=/mysql-live-database-example-streaming-data/
https://stackoverflow.com/questions/36590476/taking-data-from-a-database-and-putting-into-a-table-in-a-gui
"""
