import json

import requests

n = 0


def instadownloader(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "e676a60da7msh9f5922426b251bcp1b2dddjsn9a86dc98b41b",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    rest = json.loads(response.text)
    if 'error' in rest:
        return 'Error url'
    else:
        dict = {}
        if dict['type'] == 'video':
            dict['media'] = rest['media']
            return dict

        elif dict['type'] == 'image':
            dict['media'] = rest['media']
            return dict

        elif dict['type'] == 'carousel':
            dict['media'] = rest['media']
            return dict

        else:
            return "Bad"


xxx = instadownloader("https://www.instagram.com/reel/CqI3B8NjcaM/?igshid=MzRlODBiNWFlZA==")
print(xxx)
