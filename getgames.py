import json
import requests
import time
import os
import sys



os.chdir(sys.path[0])
url = "https://www.speedrun.com/api/v1/games?max=250"
while True:

    time.sleep(0.6)
    
    print(url)

    data = requests.get(url).text
    data = json.loads(data)
    try:
        url = data['pagination']['links'][1]['uri']
    except:
        url = data['pagination']['links'][0]['uri']
    for game in data['data']:
        try:
            id = game['id']
            print(id)
            with open('yt-speedrun-games.txt', 'a') as f:
                f.write(id + "\n")

        except:
            pass
    

















