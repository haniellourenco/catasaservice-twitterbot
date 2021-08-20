import os
import time
import pytz
from datetime import datetime
from random import randint
import requests
import tweepy as tp
from keys import *



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
    tz_SP = pytz.timezone('America/Sao_Paulo')
    datetime_SP = datetime.now(tz_SP)
    tweet_image(url)
    print('publicando imagem... horário: ' + datetime_SP.strftime("%H:%M:%S"))
    time.sleep(randint(600, 3600))
