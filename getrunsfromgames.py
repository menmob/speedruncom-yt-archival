import json
import requests
import time
import os
import sys
import random



def getprox():
    proxies = ['45.136.172.159:9673',
'64.43.90.219:6734',
'5.157.131.47:8307',
'23.229.126.165:7694',
'45.72.55.101:7138',
'45.137.40.29:8582',
'5.154.253.189:8447',
'45.130.60.159:9686',
'45.131.212.164:6213',
'193.151.160.7:8094']

    proxy = random.choice(proxies)
    proxy = f'http://{proxy}'
    proxies = {
  "http": proxy,
  "https": proxy,
}
    return(proxies)
os.chdir(sys.path[0])

with open('yt-speedrun-games.txt', 'r') as f:
    games = f.read()
    f.close()

games = games.split('\n')


for game in games:
    offset = 0
    print(game)
    url = f"https://www.speedrun.com/api/v1/runs?game={game}&max=200"
    continue_game = True
    while continue_game:
        print(url)
        time.sleep(0.1)
        data = requests.get(url, proxies=getprox()).text
        data = json.loads(data)
        offset += 200
        if len(data['data']) < 1:
            continue_game = False
        url = f"https://www.speedrun.com/api/v1/runs?game={game}&max=200&offset={offset}"

        for run in data['data']:
            try:
                for video in run['videos']['links']:
                    video = video['uri']
                    print(video)
                    with open('yt-speedrun-links-new.txt', 'a') as f:
                        f.write(video + "\n")

            except:
                pass
        
    

















