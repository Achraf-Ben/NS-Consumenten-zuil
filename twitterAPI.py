import tweepy
import datetime


class Twitter():

    accessToken = "927464600936828929-g8R4LsDaKbcXSxqW59khKZlTlJ1QM5T"
    accessTokenSecret = "iQVnaaMIkAdkbK2iZPaqeXiPiG8BJsN3FUisT5LhZ8aCy"
    consumerKey = "bnsvVR2jSVxSZXzLwL7mQHdhJ"
    ownerID = "27464600936828929"
    consumerKeySecret = "0S5AKn1EcS33tivGoZTTlu4kP02C7n9PG2uZ9dlTieqy7H5ybP"

    auth = tweepy.OAuthHandler(consumerKey, consumerKeySecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(auth)


    def updateTwitter(self, text):
        '''Stuurt via de parameter text een statusupdate op twitter'''
        self.api.update_status(text)


    def getTweets(self):
        '''Haalt alle tweets op en geeft een lijst van alle tweets die binnen 2 uur gestuurd zijn'''
        new_tweets = self.api.user_timeline(page_limit = 20)
        print(new_tweets)
        listTexts = []
        timezone = 3600
        #TODO: timeTweet naar 2 uur veranderen
        timeTweet = 300
        totalCOmpareTime = timezone + timeTweet
        for tweet in new_tweets:
            print(tweet.created_at)
            if (datetime.datetime.now() - tweet.created_at).total_seconds() < totalCOmpareTime:
                text = tweet.text
                date = tweet.created_at
                listTexts.append(text)
                print(text, date)
        return listTexts


