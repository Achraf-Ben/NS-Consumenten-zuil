import tweepy
import json
from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import *
from queue import Queue
import threading
import configparser
import sys

CONSOLE_TEMPLATE = '{}: {}\n'
TWEET_TEXT_TEMPLATE = '{:150}'

# This is the listener, resposible for receiving data
class MyStreamListner(tweepy.StreamListener):
    def __init__(self, gui):
        super().__init__()
        self.gui = gui

    def on_data(self, data):
        decoded = json.loads(data)
        tweet_text = '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        self.gui.tweet_q.put(tweet_text)
        self.gui.window.event_generate('<<new_tweet>>', when='tail')
        print(tweet_text)
        return True

    def on_error(self, status):
        print(status)

class TwitterGui:
    def __init__(self, window, tweet_q):
        self.tweet_q = tweet_q
        self.display_q = Queue()
        self.window = window
        self.output_tweet_text = StringVar()
        self.current_tweet = None
        self.tweet_input = StringVar()
        self.console_frame = Frame(window)
        self.console_frame.grid(row=3, column=0, columnspan=3)
        self.tweet_console = ScrolledText(self.console_frame, wrap=WORD, width=170, height=40)
        self.tweet_console.pack()
        self.output_label = Label(window, textvariable=self.output_tweet_text)
        self.output_label.grid(row=0, column=2, rowspan=2)
        self.output_label.config(wraplength=600)
        Button(window, text="Quit", command=self.quit).grid(row=2, column=0)
        Entry(window, textvariable=self.tweet_input).grid(row=0, column=0)
        Button(window, text='send', command=self.send_fake_tweet).grid(row=1, column=0)
        self.scroll()
        self.number = 0
        self.live_tweets = {}

    def next_number(self):
        self.number += 1
        return self.number

    def on_new_tweet(self, *args):
        if not self.tweet_q.empty():
            new_tweet_data = self.tweet_q.get()
            self.add_tweet(new_tweet_data)

    def add_tweet(self, tweet_text):
        new_tweet = Tweet(tweet_text, self.next_number())
        self.display_q.put(new_tweet)
        self.live_tweets[new_tweet.number] = new_tweet
        self.update_console()

    def remove_tweet(self, tweet_num):
        pass

    def update_console(self):
        console_text = ''
        for tweet_num in sorted(self.live_tweets.keys()):
            tweet = self.live_tweets[tweet_num]
            console_text += CONSOLE_TEMPLATE.format(tweet.number, tweet.text)
        self.tweet_console.delete('1.0', END)
        self.tweet_console.insert(INSERT, console_text)

    def scroll(self):
        if not self.display_q.empty():
            if self.current_tweet: self.display_q.put(self.current_tweet)
            self.current_tweet = self.display_q.get()
            self.output_tweet_text.set(self.current_tweet.text)
        self.window.after(5000, self.scroll)


    def send_fake_tweet(self):
        text = self.tweet_input.get()
        self.add_tweet(text)

    def quit(self):
        self.window.destroy()

class Tweet:
    def __init__(self, text, number):
        self.text =  TWEET_TEXT_TEMPLATE.format(text)
        self.number = number
        self.is_live = True

def read_conf(settings_location):
    """Read the given setting file
    and return the configparser
    """
    settings = configparser.ConfigParser()
    settings.optionxform = str
    settings.read(settings_location)
    return settings


def twitterstream(gui):
    consumer_key = "bnsvVR2jSVxSZXzLwL7mQHdhJ"
    consumer_secret = "0S5AKn1EcS33tivGoZTTlu4kP02C7n9PG2uZ9dlTieqy7H5ybP"
    access_token = "927464600936828929-g8R4LsDaKbcXSxqW59khKZlTlJ1QM5T"
    access_token_secret = "iQVnaaMIkAdkbK2iZPaqeXiPiG8BJsN3FUisT5LhZ8aCy"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    twitterstream = MyStreamListner(gui)
    stream = tweepy.Stream(auth, twitterstream)

    stream.filter(track=['utrecht'])


if __name__ == '__main__':
    window = Tk()
    tweet_q = Queue()
    gui = TwitterGui(window, tweet_q)
    window.bind('<<new_tweet>>', gui.on_new_tweet)
    t1 = threading.Thread(target=twitterstream, args=(gui,))
    t1.setDaemon(True)
    gui.stream_thread = t1
    t1.start()
    window.mainloop()
