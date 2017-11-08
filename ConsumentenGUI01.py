from tkinter import *
import sqlite3


#005CA0 = NS_Blauw
#FFFFFF = NS_Wit
#FFC917 = NS_Geel
#000000 = NS_Zwart


class Window(Frame):  # Creates window

    def __init__(self, master=None):  # Main window
        'Main application window for ConsumentenGUI'
        Frame.__init__(self, master)
        self.master.title('NS-Consumenten zuil')

        #Below: Standard layout + Text
        staticText = Label(self.master, text = 'Vul hier uw Tweet in:', background = '#FFC917', font = ('Helvetica', 16), pady = 2, padx = 15)

        self.inputConsument = Entry(self.master, background = '#005CA0', foreground = '#FFFFFF', font = ('Helvetica', 12), width = 140)
        sendTweetButton = Button(self.master, text = 'Klik hier om uw Tweet te versturen.', command=self.sendTweet)


        staticText.grid(row = 0, column = 0, sticky = W)
        self.inputConsument.grid(row = 1, column = 0, columnspan = 2)
        sendTweetButton.grid(row = 2, column = 0, columnspan = 2, sticky = W)


        # todo: get text input from Entry and sent to DB
    def sendTweet(self):
        'Sends tweet from GUI to Database'
        text = self.inputConsument.get()
        if len(text) <=0:
            print('foutmelding!')
            foutmelding = Label(self.master, text='Het bericht mag niet leeg zijn. Probeer opnieuw.', background = '#FFC917', font = ('Helvetica', 16))
            foutmelding.grid(row=3, column=0, sticky = W)
        elif len(text) > 140:
            print('foutmelding!')
            foutmelding = Label(self.master, text='Tweets kunnen maximaal 140 karakters bevatten. Probeer opnieuw.', background = '#FFC917', font = ('Helvetica', 16))
            foutmelding.grid(row=3, column=0, sticky = W)
        else:
            conn = sqlite3.connect("Database.db")
            c = conn.cursor()
            c.execute('INSERT INTO tweets(tweet, status) VALUES(?, "toBeProcessed")', (text,))
            conn.commit()
            conn.close()
            melding = Label(self.master, text='Het bericht is verstuurd!',
                                background='#FFC917', font=('Helvetica', 16))
            melding.grid(row=3, column=0, sticky=W)
            self.inputConsument.delete(0, 'end')

root = Tk()
root.configure(background = '#FFC917')

app = Window(root)

root.mainloop()