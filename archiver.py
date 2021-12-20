import json
import os

DATA_FILE = 'data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        return data
    else:
        return None

def dump_data(data):
    if os.path.exists(DATA_FILE):
        data = load_data().append(data)
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

'''
legend = load_data()
for i in legend:
    print(i['url'])


url = 'https://bing.com'
title = 'Bing'
sub_urls = [
    'https://bing.com/image/',
    'https://bing.com/mail/',
    'https://bing.com/drive/'
    ]

json_data = [{
    'url': url,
    'title': title,
    'sub_urls': sub_urls
    }]

with open('data.json', 'r') as f:
    json_file = json.load(f)

json_file.append(json_data)

with open('data.json', 'w') as f:
    json.dump(json_file, f)

print('success')


def confirm():
    i = None
    while i == None:
        i = input('Enter YES or NO. (y/n): ')
        if i == 'y' or i == 'Y':
            confirmation = True
        elif i == 'n' or i == 'N':
            confirmation = False
        else:
            i = None

    return confirmation

if confirm():
    exit()
'''
