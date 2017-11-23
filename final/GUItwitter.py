import forecastio
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import time
import datetime
import twitterAPI
import threading


def weersvoorspelling():
    '''Return weather forecast using the Darsky API.'''
    api_key = "XXXXXXXXXXXXXXXXXXXXXXXX"
    # Utrecht
    latitude = 52.0884851
    longitude = 5.1180588
    try:
        forecast = forecastio.load_forecast(api_key, latitude, longitude)
        byHour = forecast.daily()
        weerZin = byHour.summary
        return weerZin
    except:
        APIerror = "Can't connect to the DarkSky API, please try again."
        return APIerror
    

# Tkinter Window
class Window(Frame):
    twitterAPI_class = twitterAPI.Twitter()
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        

    def init_window(self):
        '''Create init_window.'''
        self.master.title("NS Consumenten zuil - Twitter & Weer") # Title of the master widget
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
        self.labelIntro = Label(self, text=' ', height=2, padx=15, font=("Helvetica", 18), fg="white")
        self.labelIntro.configure(background='DeepSkyBlue2')
        self.labelIntro.pack()

        self.label = Label(self, text=" ", padx=15, font=("Helvetica", 14), fg="white", wraplength=1000)
        self.label.configure(background='DeepSkyBlue2' )
        self.label.pack(fill=BOTH)

        threadUpdateTime = threading.Thread(target=self.reloadTweets)
        threadUpdateTime.start()
        

    def reloadTweets(self):
        while True:
            listText = self.twitterAPI_class.getTweets()
            if listText != []:
                self.labelIntro['text'] = 'Meest recente tweets:'
                textTotal = "\n"
                for text in listText:
                    textTotal += text + "\n\n\n"
                self.label['text'] = textTotal
            else:
                # Huidige weersomstandigheden
                self.labelIntro['text'] = "Huidige weersomstandigheden in Utrecht:"
                self.label['text'] = weersvoorspelling()
                self.label.pack()

            time.sleep(5)
            

root = Tk() # Create root window
root.geometry("1200x600") # Window size
root.configure(background='DeepSkyBlue2')
app = Window(root) # Create the instance
root.mainloop() # Start mainloop
