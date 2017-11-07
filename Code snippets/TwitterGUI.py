import forecastio
from tkinter import *
from PIL import Image, ImageTk

import threading
import tweepy
import json
from queue import Queue


#Darsky / Forecastio
api_key = "dca7849ad2985d67e63bdce010c191ee"
# Utrecht
latitude = 52.0884851
longitude = 5.1180588
forecast = forecastio.load_forecast(api_key, latitude, longitude)
byHour = forecast.daily()
weerZin = byHour.summary
weerWoord = byHour.icon

# Tkinter Windows
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
        tekst = Label(self, text="Huidige weersomstandigheden in Utrecht:\n " + weerZin)
        tekst.pack()

        # Huidige weersomstandigheden - 1 woord
        tekst = Label(self, text=weerWoord)
        tekst.pack()

        # Show Tweets
        tweets = Label(self, text="Tweets")
        tweets.pack()

root = Tk() #Creates root window
root.geometry("1366x768") # Window size
app = Window(root) #Create the instance
root.mainloop() # Start mainloop to show it

# NS Kleur geel = #FFC917

""""
Bronnen:
https://pypi.python.org/pypi/python-forecastio/
https://pythonprogramming.net/python-3-tkinter-basics-tutorial/
https://pythonprogramming.net/tkinter-python-3-tutorial-adding-buttons/?completed=/python-3-tkinter-basics-tutorial/

https://github.com/geduldig/TwitterAPI
http://docs.python-requests.org/en/latest/user/quickstart/
"""
