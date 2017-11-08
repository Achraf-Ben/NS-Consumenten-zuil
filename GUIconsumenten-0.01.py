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
        self.translateErrorEnglish = False

        #Below: Layout
        self.staticText = Label(self.master, text = 'Vul hier uw Tweet in:', background = '#FFC917', font = ('Helvetica', 16), pady = 2, padx = 15)
        self.inputConsument = Entry(self.master, background = '#005CA0', foreground = '#FFFFFF', font = ('Helvetica', 12), width = 60)
        self.sendTweetButton = Button(self.master, text = 'Klik hier om uw Tweet te versturen.', command=self.sendTweet, background = '#005CA0', foreground = '#FFFFFF')
        blankSpace1 = Label(self.master, background = '#FFC917', pady = 2, padx = 15)
        self.foutmelding = Label(self.master, text = '', background = '#FFC917', font = ('Helvetica', 12), pady = 2, padx = 15)
        self.nederlands = Button(self.master, text = 'Nederlands', command = self.translateDutch, background = '#005CA0', foreground = '#FFFFFF', padx = 15)
        self.english = Button(self.master, text = 'English', command = self.translateEnglish, background = '#005CA0', foreground = '#FFFFFF', padx = 15)
        blankSpace2 = Label(self.master, background='#FFC917')
        blankSpace3 = Label(self.master, background = '#FFC917')
        blankSpace4 = Label(self.master, background = '#FFC917')

        #Below: Grid positioning
        self.staticText.grid(row = 0, column = 1, sticky = W + E)
        self.inputConsument.grid(row = 1, column = 1)
        self.sendTweetButton.grid(row = 3, column = 1, sticky = W + E)
        blankSpace1.grid(row = 2, column = 1, sticky = W + E)
        self.foutmelding.grid(row = 4, column = 1, sticky = W + E)
        self.nederlands.grid(row = 5, column = 1, sticky = W)
        self.english.grid(row = 5, column = 1, sticky = E)
        blankSpace2.grid(row = 2, column=0, padx = 10)
        blankSpace3.grid(row = 2, column = 3, padx = 10)
        blankSpace4.grid(row = 6, column = 1, pady = 1)


    def sendTweet(self):
        'Sends tweet from GUI to Database'
        text = self.inputConsument.get()
        if len(text) <=0 and self.translateErrorEnglish == False:
            print('foutmelding!')
            self.foutmelding ['text'] = 'Het bericht mag niet leeg zijn. Probeer opnieuw.'

        elif len(text) <=0 and self.translateErrorEnglish == True:
            print('foutmelding!')
            self.foutmelding ['text'] = 'You cannot send an empty message. Please try again.'

        elif len(text) > 140 and self.translateErrorEnglish == False:
            print('foutmelding!')
            self.foutmelding ['text'] = 'Tweets kunnen maximaal 140 karakters bevatten. Probeer opnieuw.'

        elif len(text) > 140 and self.translateErrorEnglish == True:
            print('foutmelding!')
            self.foutmelding ['text'] = 'Tweets can only contain a maximum of 140 characters. Please try again.'

        else:
            try:
                conn = sqlite3.connect("Database.db")
                c = conn.cursor()
                c.execute('INSERT INTO tweets(tweet, status) VALUES(?, "toBeProcessed")', (text,))
                conn.commit()
                conn.close()
                if self.translateErrorEnglish == False:
                    self.foutmelding['text'] = 'Het bericht is verstuurd!'
                else:
                    self.foutmelding['text'] = 'The message has been sent!'
                self.inputConsument.delete(0, 'end')
            except:
                if self.translateErrorEnglish == False:
                    databaseError = 'Kan geen verbinding maken met de Database. Probeer het later nog eens.'
                else:
                    databaseError = 'Unable to connect to Database. Please try again later.'
                print(databaseError)
                self.foutmelding ['text'] = databaseError


    def translateDutch(self):
        'Changes the application language to Dutch'
        self.translateErrorEnglish = False
        self.staticText ['text'] = 'Vul hier uw Tweet in.'
        self.sendTweetButton ['text'] = 'Klik hier om uw Tweet te versturen.'


    def translateEnglish(self):
        'Changes the application language to English'
        self.translateErrorEnglish = True
        self.staticText ['text'] = 'Enter your Tweet here.'
        self.sendTweetButton ['text'] = 'Click here to send your Tweet.'


root = Tk()
root.configure(background = '#FFC917')

app = Window(root)

root.mainloop()
