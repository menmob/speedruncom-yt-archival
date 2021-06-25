import json
import requests
import time
import os
import sys
num = 0


os.chdir(sys.path[0])
while True:
    time.sleep(0.6)
    url = f"https://www.speedrun.com/api/v1/runs?max=200&offset={num}"


    data = requests.get(url).text
    data = json.loads(data)

    for run in data['data']:
        try:
            for video in run['videos']['links']:
                video = video['uri']
                if not 'you' in video:
                    pass
                print(video)
                with open('yt-speedrun-links.txt', 'a') as f:
                    f.write(video)

        except:
            pass
    num += 200
    print(num)

















