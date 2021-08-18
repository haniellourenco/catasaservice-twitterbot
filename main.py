import os
import time
from random import randint
import requests
import tweepy as tp

# twitter api:
consumer_key = 'kR6FxVmAx6k4i5uhPwIO0xuml'
consumer_secret = '0mSOxN90tPr759exMwExAccEFtEOlLVRwYY49VWJalFWFmHaBo'
access_token = '1367529588281204738-HDznOw5kyMTHC3vBcWJNfCclpjt4PO'
access_secret = 'hq5l7fonpmzOWnTTayBdqODcAn1zhZpeKjkceQrMWgoDD'

# logando na conta api twitter:
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

print('this is my twitter bot', flush=True)

url = "https://cataas.com/cat"

def tweet_image(url):
    filename = 'temp.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename)
        os.remove(filename)
    else:
        print("Unable to download image")


# DEV 1427738991890206732


while True:
    print('publicando imagem...')
    tweet_image(url)
    time.sleep(randint(600, 7200))
