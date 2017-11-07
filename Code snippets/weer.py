import forecastio
from tkinter import *
from PIL import Image, ImageTk

api_key = "dca7849ad2985d67e63bdce010c191ee"
# Utrecht
latitude = 52.0884851
longitude = 5.1180588

forecast = forecastio.load_forecast(api_key, latitude, longitude)
byHour = forecast.daily()
weerZin = byHour.summary
weerWoord = byHour.icon

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        '''Creation of init_window'''
        self.master.title("NS - Twitter & Weer") #Titel of the master widget
        self.pack(fill=BOTH, expand=1)  # Allow full space of root

        # Menu
        #menu = Menu(self.master)
        #self.master.config(menu=menu)
        #file = Menu(menu)
        #file.add_command(label="Sluiten", command=self.client_exit)
        #menu.add_cascade(label="Opties", menu=file)
        #edit = Menu(menu)
        #edit.add_command(label="Show NS Logo", command=self.nsLogo)
        #menu.add_cascade(label="Edit", menu=edit)

        load = Image.open("ns_logo.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

        intro = Label(self, text="Welkom bij de NS Twitter Zuil. \n")
        intro.pack()

        tekst = Label(self, text=weerZin)
        tekst.pack()

        tekst = Label(self, text=weerWoord)
        tekst.pack()

    def client_exit(self):
        '''Close init_window'''
        exit()

    def nsLogo(self):
        load = Image.open("ns_logo.png")
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def introTekst(self):
        tekst = Label(self, text="Welkom bij de NS Twitter Zuil. \n Tweets: ")
        tekst.pack()

    def weerZin(self):
        tekst = Label(self, text=weerZin)
        tekst.pack()

    def weerWoord(self):
        tekst = Label(self, text=weerWoord)
        tekst.pack()


root = Tk() #Creates root window
root.geometry("1366x768") # Window size
app = Window(root) #Create the instance
root.mainloop() # Start mainloop to show it

#bg
""""
Bronnen:
https://pypi.python.org/pypi/python-forecastio/
https://pythonprogramming.net/python-3-tkinter-basics-tutorial/
https://pythonprogramming.net/tkinter-python-3-tutorial-adding-buttons/?completed=/python-3-tkinter-basics-tutorial/
"""
