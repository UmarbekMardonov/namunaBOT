import json
import requests


def youtube(link):
    url = "https://ytstream-download-youtube-videos.p.rapidapi.com/dl"

    querystring = {"id": link}

    headers = {
        "X-RapidAPI-Key": "e676a60da7msh9f5922426b251bcp1b2dddjsn9a86dc98b41b",
        "X-RapidAPI-Host": "ytstream-download-youtube-videos.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    rest = json.loads(response.text)
    if rest['thumbnail']:
        photo = rest['thumbnail'][3]
    elif rest['formats'][2]:
        video720 = rest['formats'][2]
    elif rest['formats'][1]:
        video360 = rest['formats'][1]
    elif rest['formats'][0]:
        video144 = rest['formats'][0]


#youtube("6sJKTljo_G8")
youtube("hIT3gUlf9zY")
