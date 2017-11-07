from tkinter import *
import sqlite3

class Window(Frame):


    def __init__(self, master = None):  #Creates main window
        """ Creates main window """
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        """ Initializes the layout of the GUI """
        self.master.title('Admin GUI') #Gives a title to the window
        self.pack(fill=BOTH, expand = 1)
        self.configure(bg = 'DeepSkyBlue2') #Changes the background colour

        #Creates the textframe where the tweets appear
        text = Label(self, bg="DeepSkyBlue2", fg="white" ,text="Sample Tweet", font=("Helvetica", 14)).pack(side=TOP)

        #Creates the Accept button
        Accept = Button(self, font=("Helvetica",16), fg="Green2", background='white', text='Accept Tweet')
        Accept.pack(side="left", expand=True, pady=20)

        #Creates the Reject button
        Reject = Button(self,font=("Helvetica",16), fg="red", background='white', text = 'Reject Tweet')
        Reject.pack(side="right", expand=True, pady=20)


def exit_window(self):
    """" Executes the code above """
    exit()

root = Tk()
root.geometry('500x200') #Makes the window 500px by 200px
app = Window(root)

root.mainloop()
