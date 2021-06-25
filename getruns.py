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
    print(url)

    data = requests.get(url).text
    data = json.loads(data)

    for run in data['data']:
        years = ['2021', '2020', '2019', '2018']
        


        try:
            date = run['date']

            if any(x in date for x in years):
                pass

            for video in run['videos']['links']:
                video = video['uri']
                if not 'you' in video:
                    pass
                print(video)
                with open('yt-speedrun-links.txt', 'a') as f:
                    f.write(video + "\n")

        except:
            pass
    num += 200

















