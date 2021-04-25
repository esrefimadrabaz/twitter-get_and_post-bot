import tweepy
import json

CONSUMER_KEY ="Blsd1QrCtGXfNH838RcGabeWS"
CONSUMER_SECRET = "6V3ZpSoM2X5IfmdATJmUZA7SnRuOLZ0OcNZZYYWtWixVJ3KjDX"
ACCESS_KEY = "845785453-CLAYzkXjTtFmgvyv437RBqryXR3FnAJ045SXFAnp"
ACCESS_SECRET = "YWjDnWJQ1Ye5bdyMA949FwEPQ1nOZCDgpiMlzIbEeUPLk"
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)



def listeyap():              # x is post count and z is the count of images in the post --------------- uses lists within lists
    my_dict = {}
    x = 0       
    for tweet in tweepy.Cursor(api.user_timeline, id=  'malmqk', tweet_mode="extended", include_rts=False).items():
        if not tweet.retweeted:       #remove if u want to get rt tweets in the page
            fav = tweet.favorite_count    
            if fav >= 0:       # favorite limit
                z = 0
                my_dict["post" + str(x)] = {}      #make the first list item for the first post (can probably cause the first post to be empty but works)
                if 'media' in tweet.entities:        #check if tweet has 'media' tag in it, then checks if its a video or image(s)
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
                    print(x)

    print("Downloaded " + str(x) + " tweets.")

    with open("C:/Users/Oguz/Desktop/tw2/bot_final/he/lists.txt", "w") as fp:  # dump my_dict as json
        json.dump(my_dict, fp)
    fp.close()
    print("It's ready.")


listeyap()
