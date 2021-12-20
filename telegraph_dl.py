import os
from datetime import datetime
import requests

# ============
# custom files
# ============
from extractor import extract
from archiver import load_data, dump_data
from downloader import download

url = input('Enter URL: ')
req = requests.get(url)
data_extracted = extract(req)

# create directory for downloaded files
download_dir = data_extracted['title']
if not os.path.exists(download_dir):
    os.mkdir(download_dir)
else:
    print('Directory "{}" already exists.'.format(download_dir))
    input('Press any key to exit.')
    quit()

# json data
json_data = [{
    'url': url,
    'time_saved': datetime.now().isoformat(timespec='seconds'),
    'title': data_extracted['title'],
    'download_urls': data_extracted['download_urls']
}]
dump_data(json_data)

# download urls 
for download_url in data_extracted['download_urls']:
    download(download_url, download_dir)
