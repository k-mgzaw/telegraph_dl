import os

import requests

HEADER = {'User-Agent': 'Mozilla/5.0 (X11; CrOS armv7l 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.98 Safari/537.36'}

def download(url, destination=''): # default destination is current directory
    filename = os.path.join(destination, url.split('/')[-1]) 
    with requests.get(url, headers=HEADER, stream=True) as r:
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=2048):
                f.write(chunk)

