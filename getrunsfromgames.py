import json
import requests
import time
import os
import sys
import random

file = sys.argv[1]

def getprox():
    proxies = ['u2.p.webshare.io:10000',
'u3.p.webshare.io:10001',
'u2.p.webshare.io:10002',
'u2.p.webshare.io:10003',
'u2.p.webshare.io:10004',
'e1.p.webshare.io:10005',
'u1.p.webshare.io:10006',
'u1.p.webshare.io:10007',
'u2.p.webshare.io:10008',
'e1.p.webshare.io:10009',
'u3.p.webshare.io:10010',
'u1.p.webshare.io:10011',
'u2.p.webshare.io:10012',
'u1.p.webshare.io:10013',
'u1.p.webshare.io:10014',
'e1.p.webshare.io:10015',
'e1.p.webshare.io:10016',
'u2.p.webshare.io:10017',
'u3.p.webshare.io:10018',
'u3.p.webshare.io:10019',
'e1.p.webshare.io:10020',
'u2.p.webshare.io:10021',
'u2.p.webshare.io:10022',
'u2.p.webshare.io:10023',
'u1.p.webshare.io:10024',
'u2.p.webshare.io:10025',
'e1.p.webshare.io:10026',
'u1.p.webshare.io:10027',
'u1.p.webshare.io:10028',
'u2.p.webshare.io:10029',
'u1.p.webshare.io:10030',
'e1.p.webshare.io:10031',
'u2.p.webshare.io:10032',
'e1.p.webshare.io:10033',
'u2.p.webshare.io:10034',
'u1.p.webshare.io:10035',
'u3.p.webshare.io:10036',
'e3.p.webshare.io:10037',
'u1.p.webshare.io:10038',
'u1.p.webshare.io:10039',
'u2.p.webshare.io:10040',
'u1.p.webshare.io:10041',
'e3.p.webshare.io:10042',
'u2.p.webshare.io:10043',
'u2.p.webshare.io:10044',
'u1.p.webshare.io:10045',
'e1.p.webshare.io:10046',
'u1.p.webshare.io:10047',
'u2.p.webshare.io:10048',
'u2.p.webshare.io:10049',
'u1.p.webshare.io:10050',
'u1.p.webshare.io:10051',
'u1.p.webshare.io:10052',
'u2.p.webshare.io:10053',
'u2.p.webshare.io:10054',
'u1.p.webshare.io:10055',
'e1.p.webshare.io:10056',
'u1.p.webshare.io:10057',
'u3.p.webshare.io:10058',
'u1.p.webshare.io:10059',
'e1.p.webshare.io:10060',
'u3.p.webshare.io:10061',
'u1.p.webshare.io:10062',
'u2.p.webshare.io:10063',
'e1.p.webshare.io:10064',
'u1.p.webshare.io:10065',
'u1.p.webshare.io:10066',
'u2.p.webshare.io:10067',
'u1.p.webshare.io:10068',
'u1.p.webshare.io:10069',
'u1.p.webshare.io:10070',
'u2.p.webshare.io:10071',
'u1.p.webshare.io:10072',
'u1.p.webshare.io:10073',
'u2.p.webshare.io:10074',
'u1.p.webshare.io:10075',
'u1.p.webshare.io:10076',
'e1.p.webshare.io:10077',
'u1.p.webshare.io:10078',
'e3.p.webshare.io:10079',
'e1.p.webshare.io:10080',
'u1.p.webshare.io:10081',
'u2.p.webshare.io:10082',
'u2.p.webshare.io:10083',
'u1.p.webshare.io:10084',
'u2.p.webshare.io:10085',
'u3.p.webshare.io:10086',
'u1.p.webshare.io:10087',
'u1.p.webshare.io:10088',
'u2.p.webshare.io:10089',
'e3.p.webshare.io:10090',
'u1.p.webshare.io:10091',
'u2.p.webshare.io:10092',
'u1.p.webshare.io:10093',
'u1.p.webshare.io:10094',
'u2.p.webshare.io:10095',
'u1.p.webshare.io:10096',
'u1.p.webshare.io:10097',
'e1.p.webshare.io:10098',
'u1.p.webshare.io:10099']

    proxy = random.choice(proxies)
    proxy = f'http://{proxy}'
    proxies = {
  "http": proxy,
  "https": proxy,
}
    return(proxies)
os.chdir(sys.path[0])

with open(f'{file}yt-speedrun-games.txt', 'r') as f:
    games = f.read()
    f.close()

games = games.split('\n')


for game in games:
    if game == "":
        pass
    offset = 0
    print(game)
    url = f"https://www.speedrun.com/api/v1/runs?game={game}&max=200"
    continue_game = True
    while continue_game:
        print(url)
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
        
    

















