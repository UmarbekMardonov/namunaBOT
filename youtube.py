import json

import requests


def youtube(link):
    if link[:27] == 'https://youtube.com/shorts/':
        link = link[27:38]
    if link[:17] == 'https://youtu.be/':
        link = link[17:28]
    url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details"

    querystring = {"videoId": link}

    headers = {
        "X-RapidAPI-Key": "3d579d87b6msh8e40272f2bd1036p1b3e47jsnc7a47101736b",
        "X-RapidAPI-Host": "youtube-media-downloader.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    rest = json.loads(response.text)
    dict = {}
    if rest['audios']:
        dict['audio'] = rest['audios']['items'][0]['url']
    dict['title'] = rest['title']
    dict['desc'] = rest['channel']['name']
    dict['mediaAvatar'] = rest['thumbnails'][4]['url']
    dict['360video'] = rest['videos']['items'][0]['url']
    dict['360videoSize'] = rest['videos']['items'][0]['sizeText']
    dict['720video'] = rest['videos']['items'][1]['url']
    dict['720videoSize'] = rest['videos']['items'][1]['sizeText']
    dict['1080video'] = rest['videos']['items'][2]['url']
    dict['1080videoSize'] = rest['videos']['items'][2]['sizeText']
    return dict
# youtube('https://youtube.com/shorts/7hh_mOJT6gM?si=Kyo15lhUR6CwWtq_')
# youtube('https://youtu.be/Gs6AjGQu4DU?si=9b4DEWjTA63s4UIf')
