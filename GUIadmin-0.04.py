from tkinter import *
import sqlite3
from testjes import twitterAPI


class Window(Frame):
    def __init__(self, master = None):
        '''Creates main window.'''
        self.twitterAPI_class = twitterAPI.Twitter()
        Frame.__init__(self, master)
        self.master = master
        self.init_window()


    def init_window(self):
        '''Initialize the layout of the GUI and calls read() and adjust texts.'''
        self.master.title('NS Consumenten zuil - Admin') #Gives a title to the window
        self.pack(fill=BOTH, expand = 1)
        self.configure(bg = 'DeepSkyBlue2') #Changes the background colour

        #Creates the textframe where the tweets appear
        self.textLabel = Label(self, bg="DeepSkyBlue2", fg="white" ,text=" ", font=("Helvetica", 14))
        self.textLabel.pack(side=TOP, pady = 9)
        # Creates text where an error can appear
        self.errorLabel = Label(self, bg="DeepSkyBlue2", fg="white", text=" ", font=("Helvetica", 14))
        self.errorLabel.pack(side="bottom", fill=X, pady=10)

        #Creates the Accept button
        self.acceptButton = Button(self, font=("Helvetica",16), fg="Green2", background='white', text='Accept Tweet', command = self.accept)
        self.acceptButton.pack(side="left", expand=True, pady=0)

        #Creates the Reject button
        self.rejectButton = Button(self,font=("Helvetica",16), fg="red", background='white', text = 'Reject Tweet', command = self.reject)
        self.rejectButton.pack(side="right", expand=True, pady=0)
        self.read()


    def reject(self):
        '''Update database with status Reject, at position of id, and calls showtext() for new tweet.'''
        try:
            conn = sqlite3.connect("Database.db")
            c = conn.cursor()
            c.execute(
                'UPDATE tweets SET status = "REJECT" WHERE tweetId = ?', (self.tweetDBID,))
            conn.commit()
            conn.close()
            self.showText()
        except:
            self.errorLabel['text'] = "Er kan geen connectie met de database gemaakt worden"


    def accept(self):
        '''Update twitter with text and delete tweet from database at position of id, and calls showtext() for new tweet.'''
        try:
            # eerst een connectie porberen te maken met de database
            conn = sqlite3.connect("Database.db")
            c = conn.cursor()
            try:
                listText = self.twitterAPI_class.updateTwitter(self.tweetText)

            except:
                self.errorLabel['text'] = "Er kan niet naar de Twitter gepost worden"

            c.execute(
                'DELETE FROM tweets WHERE tweetId = ?', (self.tweetDBID,))
            conn.commit()
            conn.close()
        except:
            self.errorLabel['text'] = "Er kan geen connectie met de database gemaakt worden"

        print("accepted")
        self.showText()


    def read(self):
        '''Read from database all tweets and put these in a dictionary. then calls showText().'''
        self.dict_tweetInfo = {}
        try:
            conn = sqlite3.connect("Database.db")
            c = conn.cursor()
            for row in c.execute(
                    'SELECT tweet, tweetID FROM tweets WHERE status = "toBeProcessed"'):
                self.dict_tweetInfo[row[1]] = row[0]
            print(self.dict_tweetInfo)
            conn.commit()
            conn.close()

            if self.dict_tweetInfo != {}:
                self.showText()
            else:
                self.acceptButton['state'] = DISABLED
                self.rejectButton['state'] = DISABLED
        except:
            self.textLabel['text'] = "Er kan geen connectie met de database gemaakt worden"
            self.acceptButton['state'] = DISABLED
            self.rejectButton['state'] = DISABLED


    def showText(self):
        '''call first tweet in dictionary and put in textLabel, delete tweet from dictionary.'''
        if self.dict_tweetInfo != {}:
            for id, text in self.dict_tweetInfo.items():
                self.tweetDBID = id
                self.tweetText = text
                self.textLabel['text'] = text
                del self.dict_tweetInfo[self.tweetDBID]
                break
        else:
            self.textLabel['text'] = "Er zijn geen tweets die nog beoordeeld moeten worden"
            self.read()


root = Tk()
root.geometry('500x200') #Makes the window 500px by 200px
app = Window(root)
root.mainloop()
