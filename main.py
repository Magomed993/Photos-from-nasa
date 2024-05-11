import requests
import os
from urllib.parse import urlparse
import datetime
from dotenv import load_dotenv


def get_picture(url, path):
    headers = {
        'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    with open('images/hubble.jpeg', 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(url, path):
    response = requests.get(url)
    response.raise_for_status()
    resp_json = response.json()['links']['flickr']['original']
    for number, picture in enumerate(resp_json):
        with open('images/spacex_{0}.jpeg'.format(number), 'wb') as file:
            file.write(requests.get(picture).content)


def get_nasa_apod_url(key, path):
    url_nasa = 'https://api.nasa.gov/planetary/apod'
    payload = {
        'api_key': key,
        'count': 30,
        'thumbs': False
    }
    response = requests.get(url_nasa, params=payload)
    response.raise_for_status()
    resp_json = response.json()
    lst = []
    for i in resp_json:
        if 'video' in i['media_type']:
            continue
        a = i['url']
        lst.append(a)
    for number, picture in enumerate(lst):
        with open('images/nasa_apod_{0}{1}'.format(number, output_picture_format(requests.get(picture).url)),
                  'wb') as file:
            file.write(requests.get(picture).content)


def output_picture_format(url):
    response = requests.get(url)
    response.raise_for_status()
    resp_parse = urlparse(response.url)
    path_separation = os.path.splitext(resp_parse.path)
    path_picture, format = path_separation
    return format


def get_nasa_epic_url(key, path):
    url = 'https://api.nasa.gov/EPIC/api/natural'
    payload = {
        'api_key': key,
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    resp_json = response.json()
    for number, loop_contents in enumerate(resp_json):
        name_image = loop_contents['image']
        date_time = loop_contents['date']
        date = datetime.datetime.fromisoformat(date_time)
        formatted_date = date.strftime('%Y/%m/%d')
        url_1 = 'https://api.nasa.gov/EPIC/archive/natural/{0}/png/{1}.png'.format(formatted_date, 
                                                                                   name_image)
        response_1 = requests.get(url_1, params=payload)
        with open('images/epic_{0}{1}'.format(number, output_picture_format(response_1.url)),
                  'wb') as file:
            file.write(response_1.content)


def main():
    load_dotenv()
    nasa_key = os.environ['NASA_KEY']
    url_picture = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    save_path = os.makedirs('images', exist_ok=True)
    url_spacex = 'https://api.spacexdata.com/v5/launches/5eb87d42ffd86e000604b384'
    get_picture(url_picture, save_path)
    fetch_spacex_last_launch(url_spacex, save_path)
    get_nasa_apod_url(nasa_key, save_path)
    get_nasa_epic_url(nasa_key, save_path)

if __name__ == '__main__':
    main()