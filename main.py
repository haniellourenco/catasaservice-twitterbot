import os
import time
import pytz
from datetime import datetime
from random import randint
import requests
import json
import tweepy as tp
#from keys import *

consumer_key = 'sFg0Fe0iVKcYEiPiCO4Ix6p6j'
consumer_secret = 'vby53rwKvJzDJ0srCSSE7Zggev4cZsGW5LxQBxEZZeZ2a41umY'
access_token = '1367529588281204738-ZDdM4yA4xfgzVqhl693VzCiHwOOACS'
access_secret = 'ZR2EyZO8GsB0rSNnzYCDaoTkEYSzPGKThOp1E5Yf4ky6j'

# logando na conta api twitter:
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

print('this is my twitter bot', flush=True)

# url = "https://cataas.com/cat"
links = ['https://cataas.com/cat',
         'https://thatcopy.pw/catapi/rest/', 'https://aws.random.cat/meow']


def tweet_image():
    escolhido = randint(0, 2)

    if escolhido == 0:
        url = 'https://cataas.com/cat'
        print('Escolhi o 0')
    if escolhido == 1:
        res = requests.get(links[1])
        data = json.loads(res.text)
        url = data.get("url")
        print('Escolhi o 1')
        # data = json.dumps(data)
    if escolhido == 2:
        res = requests.get(links[2])
        data = json.loads(res.text)
        url = data.get("file")
        print("Escolhi o 2")

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


while True:
    tz_SP = pytz.timezone('America/Sao_Paulo')
    datetime_SP = datetime.now(tz_SP)
    tweet_image()
    print('publicando imagem... horário: ' + datetime_SP.strftime("%H:%M:%S"))
    time.sleep(randint(600, 3600))
