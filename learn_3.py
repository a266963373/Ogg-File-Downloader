import requests as r
from bs4 import BeautifulSoup as b
import os.path as p
import re

request_url = 'https://leagueoflegends.fandom.com/wiki/Irelia/LoL/Audio'
response = r.get(request_url)
soup = b(response.content, 'html.parser')

folder_dir = r'D:\Codes\Python\lol voicelines\irelia'
audios = soup.find_all('audio', src=re.compile('Irelia_Original'))

for audio in audios:
    file_name = audio.string.split(':')[-1]
    file_path = p.join(folder_dir, file_name)

    with open(file_path, 'wb+') as f:
        f.write(r.get(audio['src']).content)
