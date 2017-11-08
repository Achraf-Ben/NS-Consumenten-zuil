import forecastio
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import time
import datetime
import twitterAPI

def weersvoorspelling():
    '''Returns weather forecast using the Darsky API'''
    api_key = "dca7849ad2985d67e63bdce010c191ee"
    # Utrecht
    latitude = 52.0884851
    longitude = 5.1180588
    try:
        forecast = forecastio.load_forecast(api_key, latitude, longitude)
        byHour = forecast.daily()
        weerZin = byHour.summary
        return weerZin
    except:
        APIerror = "Cant connect to the DarkSky API please try again"
        return APIerror

# Tkinter Window
class Window(Frame):
    twitterAPI_class = twitterAPI.Twitter()
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        '''Creation of init_window'''
        self.master.title("NS - Twitter & Weer") #Titel of the master widget
        self.pack(fill=BOTH, expand=1)  # Allow full space of root
        self.configure(background="DeepSkyBlue2")

        # NS Logo
        load = Image.open("ns_logo.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render, bg="DeepSkyBlue2")
        img.image = render
        img.place(x=0, y=0)

        # Intro tekst
        intro = Label(self, text="Welkom bij de NS Twitter Zuil. \n", bg="DeepSkyBlue2", height=2, padx=15, pady = 14, font=("Helvetica", 16), fg="white")
        intro.pack()

        # Show Tweets
        listText = self.twitterAPI_class.getTweets()
        if listText != []:
            self.label = Label(self, text='Meest recente tweets:', height=2, padx=15, font=("Helvetica", 16),
                               fg="white")
            self.label.configure(background='DeepSkyBlue2')
            self.label.pack()

            for text in listText:
                self.label = Label(self, text=text, height=2, padx=15,
                                   font=("Helvetica", 14), fg="white")
                self.label.configure(background='DeepSkyBlue2')
                self.label.pack()
        else:
            # Huidige weersomstandigheden
            tekst = Label(self, text="Huidige weersomstandigheden in Utrecht:\n " + weersvoorspelling(),
                          bg="DeepSkyBlue2", height=2, padx=15, font=("Helvetica", 16), fg="white")
            tekst.pack()


root = Tk() #Creates root window
root.geometry("1200x600") # Window size
root.configure(background='DeepSkyBlue2')
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
