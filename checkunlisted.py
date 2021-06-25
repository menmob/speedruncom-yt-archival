import requests
import re
import time

num = 0
numu = 0

with open('yt-speedrun-links.txt', 'r') as f:
    urls = f.read()

urls = urls.split('\n')


for url in urls:
    url = f'https://www.youtube.com/watch?v={url}'
    time.sleep(0.5)
    num +=1
    print(f"Checked {num} urls - {url}. {numu} unlisted so far.")
    try:
        data = requests.get(url).text
    except:
        print(f'{url} - FAILED')
        pass
    if 'ytd-badge-supported-renderer">Unlisted' in data:
        with open('yt-speedrun-links-unlisted.txt', 'a') as f:
            f.write(url + "\n")
            numu += 1
            