import math
import re
import aiohttp
from aiohttp import ClientSession
from bs4 import BeautifulSoup
import random
import json


def hisobot():
    count = 0
    return count




def random_ip():
    ips = ['46.227.123.', '37.110.212.', '46.255.69.', '62.209.128.', '37.110.214.', '31.135.209.', '37.110.213.',
           '37.110.216.', '62.209.127.']
    prefix = random.choice(ips)
    return prefix + str(random.randint(1, 255))


class Downloads():
    async def instagram_1(link):
        result = []
        RES = {}
        data = {'q': link, 'vt': 'home'}
        headers = {
            'origin': 'https://saveinsta.app',
            'referer': 'https://saveinsta.app/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
            'X-Forwarded-For': random_ip(),
            'X-Client-IP': random_ip(),
            'X-Real-IP': random_ip(),
            'X-Forwarded-Host': 'saveinsta.app'
        }
        base_url = 'https://v3.saveinsta.app/api/ajaxSearch'
        async with ClientSession() as session:
            async with session.post(base_url, data=data, headers=headers) as response:
                jsonn = json.loads(await response.text())
                if jsonn['status'] == 'ok':
                    data = jsonn['data']
                    soup = BeautifulSoup(data, 'html.parser')
                    for i in soup.find_all('div', class_='download-items__btn'):
                        url = i.find('a')['href']
                        result.append({'url': url})
                    RES = {'ok': True, 'status_code': 200, 'result': result}
                else:
                    RES = {'ok': False, 'status_code': 400, 'result': 'Error'}
        return RES

    async def instagram_2(url):
        headers = {
            'authority': 'instagrab.app',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': '_ga=GA1.1.661703434.1685185653; _ga_FKM4JVNKDN=GS1.1.1690351182.7.0.1690351182.0.0.0',
            'origin': 'https://instagrab.app',
            'referer': 'https://instagrab.app/',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': 'Windows',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'page': url,
            'ftype': 'all',
            'ajax': '1',
        }

        async with aiohttp.ClientSession() as session:
            async with session.post("https://instagrab.app/", headers=headers, data=data) as response:
                try:
                    if response.status == 200:
                        matches = re.findall(
                            r'<div class="card-body">.*?<a class="btn btn-primary btn-dl" rel="noreferrer" target="_blank" href="(.*?)">.*?</a>.*?</div>',
                            await response.text(), re.DOTALL)

                        result = []
                        for match in matches:
                            link = match
                            title = match
                            type = 'mp4' if 'mp4' in title else 'jpg'

                            result.append({
                                'link': link,
                                'type': type,
                            })

                        import json
                        return result
                    else:
                        return {"Error occurred:", response.status}
                except:
                    return {"status": False, "message": "Something went wrong"}

    async def tiktok(url):
        async with ClientSession() as session:
            pattern = r'video/(\d+)'
            match = re.search(pattern, url)
            if match:
                async with session.get(
                        'https://api.twitterpicker.com/tiktok/mediav2?id=' + str(match.group(1))) as response:
                    t_url = await response.json()
            else:
                link2 = url.split("/")[3]
                if link2 != 't':
                    async with session.get('https://api.twitterpicker.com/tiktok/mediav2?id=' + link2) as response:
                        t_url = await response.json()
                else:
                    link23 = url.split("/")[4]

                    async with session.get('https://api.twitterpicker.com/tiktok/mediav2?id=' + link23) as response:
                        t_url = await response.json()
            dict = {}
            if t_url['video_no_watermark_alternatives']:
                dict['video2'] = t_url['video_no_watermark_alternatives'][0]['url']
                return dict
            else:
                dict = 'Bad'
                return dict

    async def youtube_1(url):
        API_BASE_URL = "https://api.ytbvideoly.com/api/thirdvideo/parse"
        video_url = f"{API_BASE_URL}?from=videodownloaded&link={url}"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(video_url) as response:
                    json_data = await response.text()
                    json_data = json.loads(json_data)
                    response_data = json_data
                    dict = {}
                    dict['audio'] = response_data['data']['audios']['m4a'][0]['url']
                    dict['360video'] = response_data['data']['formats'][0]['url']
                    dict['720video'] = response_data['data']['formats'][1]['url']
                    dict['1080videos'] = response_data['data']['videos']
                    dict['photo'] = response_data['data']['thumbnail']
                    dict['title'] = response_data['data']['title']
                    print(response_data['data'])

        except:
            return None


# YouTube Music uchun
async def get_mp3_url_yt(youtube_url):
    api_url = 'https://yt5s.io/api/ajaxSearch'
    data = {
        'q': youtube_url,
        'vt': 'mp3'
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(api_url, data=data, headers={'X-Requested-With': 'XMLHttpRequest'}) as response:
            if response.status == 200:
                result = await response.json()
                return result
            else:
                print(f"Xatolik yuz berdi: {response.status}")


async def get_all_mp3_urls(data):
    base_url = 'https://ve44.aadika.xyz/download/'
    video_id = data['vid']
    time_expires = data['timeExpires']
    token = data['token']
    mp3_info_dict = {}  # Bo'sh dictionary yaratamiz

    for index, (quality, info) in enumerate(data['links']['mp3'].items(), start=1):
        if info['f'] == 'mp3':
            mp3_info = {
                'title': data['title'],
                'format': info['k'],
                'q': info['q'],
                'size': info['size'],
                'key': info['key'],
                'url': f"{base_url}{video_id}/mp3/{info['k']}/{time_expires}/{token}/{index}?f=yt5s.io"
            }
            mp3_info_dict[index] = mp3_info  # Malumotlarni dictionaryga qo'shamiz

    return mp3_info_dict
