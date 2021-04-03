import tweepy
import json

CONSUMER_KEY = "WMd6R5kcDIlgkmuEIxCPEfGNj"
CONSUMER_SECRET = "xvEaJN4vIZY9BMK3Fsb4ySerarccCg3EHxI2mL5Lz2y4qxXGJ5"
ACCESS_KEY = "1170016028509790208-4avcGboqAv9yXum6qZQan0eD0VVTjs"
ACCESS_SECRET = "GTcD2RwtCkq2tDWgIT6ybJXFMsFgsgeAdnRa18io28fob"
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)



def listeyap():
    my_dict = {}
    x = 0
    for tweet in tweepy.Cursor(api.user_timeline, id=  'TooSatisfied', tweet_mode="extended", include_rts=False).items():
        if not tweet.retweeted:
            fav = tweet.favorite_count
            if fav >= 1000:
                z = 0
                my_dict["post" + str(x)] = {}
                if 'media' in tweet.entities:
                    for image in tweet.extended_entities['media']:
                        tip = image['type']
                        if tip == 'video':
                            link = image['expanded_url']
                            my_dict["post" + str(x)]["resim" + str(z)] = link
                            z = z + 1
                        else:
                            link = image['media_url']
                            my_dict["post" + str(x)]["resim" + str(z)] = link
                            z = z + 1
                x = x + 1

    print("Downloaded " + str(x) + " tweets.")

    with open("C:/Users/Oguz/Desktop/tw2/bot_final/he/lists.txt", "w") as fp:  # dump my_dict as json
        json.dump(my_dict, fp)
    fp.close()
    print("It's ready.")


listeyap()

"""x = {"2" : "bum"}
x.update({"y" : {"1" : "hey", "2" : "bum"}})
print(x["y"])
uzun = len(x["y"])
print(uzun)"""