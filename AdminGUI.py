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

        self.read()
        #Creates the textframe where the tweets appear
        self.showText(True)


        #Creates the Accept button
        Accept = Button(self, font=("Helvetica",16), fg="Green2", background='white', text='Accept Tweet', command = self.accept)
        Accept.pack(side="left", expand=True, pady=20)

        #Creates the Reject button
        Reject = Button(self,font=("Helvetica",16), fg="red", background='white', text = 'Reject Tweet', command = self.reject)
        Reject.pack(side="right", expand=True, pady=20)


    def exit_window(self):
        """" Executes the code above """
        exit()

    def reject(self):
        print("rejected")
        self.showText(False)

    def accept(self):
        print("accepted")
        self.showText(False)

    def read(self):
        self.dict_tweetInfo = {}
        conn = sqlite3.connect("Database.db")
        c = conn.cursor()
        for row in c.execute(
                'SELECT tweet, tweetID FROM tweets WHERE status = "toBeProcessed"'):
            self.dict_tweetInfo[row[1]] = row[0]
        print(self.dict_tweetInfo)
        conn.commit()
        conn.close()

    def showText(self, init):
        for id, text in self.dict_tweetInfo.items():
            if init == True:
                self.textLabel = Label(self, bg="DeepSkyBlue2", fg="white" ,text=text, font=("Helvetica", 14)).pack(side=TOP)
            else:
                self.textLabel['text'] = text
            del self.dict_tweetInfo[id]
            break

root = Tk()
root.geometry('500x200') #Makes the window 500px by 200px
app = Window(root)
root.mainloop()
