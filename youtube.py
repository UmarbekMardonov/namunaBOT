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
    print(rest)


#youtube("6sJKTljo_G8")
youtube("hIT3gUlf9zY")
