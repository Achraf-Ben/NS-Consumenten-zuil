from tkinter import *
import sqlite3

class Window(Frame):


    def __init__(self, master = None):                      #main window
        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):

        self.master.title('Admin GUI')

        self.pack(fill=BOTH, expand = 1)
        self.configure(bg = 'DeepSkyBlue2')

        frame = Frame(root)

        text = Label(self, bg="DeepSkyBlue2", fg="white" ,text="Wat vind jij van het hedendaags feminisme?", font=("Helvetica", 14)).pack(side=TOP)

        Accept = Button(self, font=("Helvetica",16), fg="Green2", background='white', text='Accept Tweet')

        Accept.pack(side="left", expand=True, pady=20)

        Reject = Button(self,font=("Helvetica",16), fg="red", background='white', text = 'Reject Tweet')

        Reject.pack(side="right", expand=True, pady=20)

        #frame.config(bg="white")
        #frame.pack(fill=BOTH, expand=True)


def exit_window(self):
        exit()

root = Tk()

root.configure(background="DeepSkyBlue2", padx=20, pady=50)
root.geometry('400x300')
app = Window(root)

root.mainloop()
