import tweepy
import json
import os
import requests
import youtube_dl
import time

CONSUMER_KEY ="9JYejRYfJRNHuoV2nC4z8T227"
CONSUMER_SECRET = "Wxua1fgTfexMd6mI27r91UQHPTx8rq7Q2B84lKdW1OGxeTFUha"
ACCESS_KEY = "2700009857-4qEG8lpxft1LopUCjGcpUh7yOv8qrzxE6Cptf7E"
ACCESS_SECRET = "mGWvKbMfJXYyvaE4OiqtgnTXE78AkKtkDfl21RCZt996a"
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

path = "/home/smawlz/vxsuals/fotolar/"



def indir(link,y):  # x = kaç tane
    try:
        resim = requests.get(str(link), allow_redirects=True)
        extension = link.split('.')[-1]
        print(link)
        if extension == 'jpg' or extension == 'png':
            open(path + str(y)+ "." + extension , 'wb').write(resim.content)
        else:
            ydl_opts2 = {
                'format': 'bestvideo+bestaudio/best',  #set video titl as opt
                'outtmpl' : path + "0" + '.%(ext)s',
                }
            with youtube_dl.YoutubeDL(ydl_opts2) as ydl: #download
                ydl.download([link])
            print("video downloaded")
            pass
    except:
        pass

def kontrol():
    for i in range (0, 4 , 1):
        try:
            os.remove(path + str(i) + ".png")
        except:
            pass
        try:
            os.remove(path + str(i) + ".jpg")
        except:
            pass
        try:
            os.remove(path + str(i) + ".mp4")
        except:
            pass


def upload(z , link):
    fotolar = []
    for i in range (0, z, 1):
        extension = link.split('.')[-1]
        if extension == 'jpg' or extension == 'png':
            res = api.media_upload(path + str(i) + "." + extension)
        else:
            res = api.media_upload(path + str(i) + ".mp4", media_category='TWEET_VIDEO')
            while (res.processing_info['state'] == 'pending'):
               time.sleep(res.processing_info['check_after_secs'])
               res = api.get_media_upload_status(res.media_id_string)
        fotolar.append(res.media_id_string)
    api.update_status(status = "", media_ids = fotolar)


def final():
    with open("/home/smawlz/vxsuals/lists.txt", "r") as fp:
        new_dict = json.load(fp)
    fp.close()
    with open("/home/smawlz/vxsuals/sayi.txt", "r") as fp:
        sayi = fp.read()  # sayi = kaçıncı post oldugu
    fp.close()
    adet = len(new_dict["post" + str(sayi)])   # postta kaç foto oldugu
    check = len(new_dict) # toplam kaç post oldugu

    print(str(check) + " posttan " + str((int(sayi) + 1)) + "." + " posttayız, bu postta " + str(adet) + " foto var.")
    if int(sayi) < 0:
        print("Fotolar bitti")
        return

    kontrol()

    for i in range(0, adet, 1):
        #print(i)
        #print(new_dict["post" + str(sayi)]["resim"+ str(i)])
        indir(new_dict["post" + str(sayi)]["resim"+ str(i)], i)


    upload(adet, new_dict["post" + str(sayi)]["resim"+ str(i)])
    with open("/home/smawlz/vxsuals/sayi.txt", "w") as fp:
        fp.write(str(int(sayi) - 1 ))
    fp.close()
    print("Yüklendi.")





final()