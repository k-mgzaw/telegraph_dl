from bs4 import BeautifulSoup as bs

def extract(request_data):
    SITE = 'https://telegra.ph'
    
    bso = bs(request_data.content, features='html.parser')

    # title
    title = bso.find('h1').string

    # download urls
    download_urls = [''.join(SITE + tag['src']) for tag in bso.find_all('img')]

    data_extracted = {
        'title': title,
        'download_urls': download_urls
        }

    return data_extracted
