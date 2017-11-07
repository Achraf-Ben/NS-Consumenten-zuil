from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
#todo: change from..
from testjes import twitterAPI

class GUI(Frame):
    twitterAPI_class = twitterAPI.Twitter()

    def __init__(self, root=None):
        Frame.__init__(self, root)
        self.root = root
        self.initialisizeGUI()


    def initialisizeGUI(self):



        self.label = Label(master=self.root, text='Meest recente tweets:', height=2, padx=15, font=("Helvetica", 16), fg="white")
        self.label.configure(background='DeepSkyBlue2')
        self.label.pack()

        listText = self.twitterAPI_class.getTweets()
        if listText != []:

            for text in listText:
                self.label = Label(master=self.root, text=text, height=2, padx=15,
                                   font=("Helvetica", 14), fg="white")
                self.label.configure(background='DeepSkyBlue2')
                self.label.pack()
        else:
            print("lijst is leeg1")




root = Tk()


app = GUI(root)



root.mainloop()