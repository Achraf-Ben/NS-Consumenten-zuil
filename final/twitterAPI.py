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
        '''send de tweet met de bijbehorende tekst.'''
        self.api.update_status(text)


    def getTweets(self):
        '''haalt de tweets op die binnen 2 uur zijn gepost en stuurt een lijst van de tweets terug.'''
        try:
            new_tweets = self.api.user_timeline(page_limit = 20)
            listTexts = []
            #houd rekening met de tijdzone
            timezone = 3600
            # tweets die binnen 2 uur gepost zijn mogen worden opgenomen in de lijst
            timeTweet = 7200
            totalCOmpareTime = timezone + timeTweet

            numCount = 0
            for tweet in new_tweets:
                if (datetime.datetime.now() - tweet.created_at).total_seconds() < totalCOmpareTime:
                    numCount = numCount + 1
                    text = tweet.text
                    date = tweet.created_at
                    listTexts.append(text)
                    if numCount >= 4:
                        break
                else:
                    # de tweets zijn op volgorde van datum, dus de rest van de tweets zijn ouder en hoeven ook niet bekeken te worden
                    break
            return listTexts
        except:
            error = []
            return error


