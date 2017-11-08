from tkinter import *
import sqlite3
import twitterAPI

class Window(Frame):

    def __init__(self, master = None):  #Creates main window
        """ Creates main window """
        self.twitterAPI_class = twitterAPI.Twitter()
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        """ Initializes the layout of the GUI """
        self.master.title('Admin GUI') #Gives a title to the window
        self.pack(fill=BOTH, expand = 1)
        self.configure(bg = 'DeepSkyBlue2') #Changes the background colour

        self.read(False)
        #Creates the textframe where the tweets appear

        self.textLabel = Label(self, bg="DeepSkyBlue2", fg="white" ,text=" ", font=("Helvetica", 14))
        self.textLabel.pack(side=TOP)
        self.showText()


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
        conn = sqlite3.connect("Database.db")
        c = conn.cursor()
        c.execute(
            'UPDATE tweets SET status = "REJECT" WHERE tweetId = ?', (self.tweetDBID,))
        conn.commit()
        conn.close()
        self.showText()

    def accept(self):
        import sqlite3
        try:
            # eerst een connectie porberen te maken met de database
            conn = sqlite3.connect("Database.db")
            c = conn.cursor()
            try:
                listText = self.twitterAPI_class.updateTwitter(self.tweetText)
                c.execute(
                    'DELETE FROM tweets WHERE tweetId = ?', (self.tweetDBID,))
                conn.commit()
                conn.close()
            except:
                print("er kan niet naar de twitterAPI gepost worden")
        except:
            print("er kan geen connectie met de database gemaakt worden")



        print("accepted")
        self.showText()

    def read(self, reload):
        self.dict_tweetInfo = {}
        conn = sqlite3.connect("Database.db")
        c = conn.cursor()
        for row in c.execute(
                'SELECT tweet, tweetID FROM tweets WHERE status = "toBeProcessed"'):
            self.dict_tweetInfo[row[1]] = row[0]
        print(self.dict_tweetInfo)
        conn.commit()
        conn.close()

        if reload == True:
            if self.dict_tweetInfo != {}:
                self.showText()

    def showText(self):
        if self.dict_tweetInfo != {}:
            for id, text in self.dict_tweetInfo.items():
                self.tweetDBID = id
                self.tweetText = text
                self.textLabel['text'] = text
                del self.dict_tweetInfo[self.tweetDBID]
                break
        else:
            self.textLabel['text'] = "Er zijn geen tweets meer die beoordeeld moeten worden"
            self.read(True)

root = Tk()
root.geometry('500x200') #Makes the window 500px by 200px
app = Window(root)
root.mainloop()
