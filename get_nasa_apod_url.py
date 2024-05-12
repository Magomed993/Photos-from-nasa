import requests
import os
from helper_script import output_picture_format
from dotenv import load_dotenv


def get_nasa_apod_url(key):
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
        with open('images/nasa_apod_{0}{1}'.format(number,
                                                   output_picture_format(requests.get(picture).url)),
                  'wb') as file:
            file.write(requests.get(picture).content)


if __name__ == '__main__':
    load_dotenv()
    os.makedirs('images', exist_ok=True)
    nasa_key = os.environ['NASA_KEY']
    get_nasa_apod_url(nasa_key)
