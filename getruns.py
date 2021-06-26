import json
import requests
import time
import os
import sys



os.chdir(sys.path[0])
url = "https://www.speedrun.com/api/v1/runs?max=200"
while True:

    time.sleep(0.6)
    
    print(url)

    data = requests.get(url).text
    data = json.loads(data)
    try:
        url = data['pagination']['links'][1]['uri']
    except:
        url = data['pagination']['links'][0]['uri']
        print("THIS SHOULD ONLY HAPPEN ON FIRST PAGE\n\n\n\n\n\n\n")
    for run in data['data']:
        try:
            for video in run['videos']['links']:
                video = video['uri']
                print(video)
                with open('yt-speedrun-links.txt', 'a') as f:
                    f.write(video + "\n")

        except:
            pass
    

















