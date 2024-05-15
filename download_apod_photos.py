import requests
import os
from helper_script import displays_image_format, download_files
from dotenv import load_dotenv


def download_apod_photos(key):
    url_nasa = 'https://api.nasa.gov/planetary/apod'
    min_loading_quantity = 10
    payload = {
        'api_key': key,
        'count': min_loading_quantity,
        'thumbs': False
    }
    response = requests.get(url_nasa, params=payload)
    response.raise_for_status()
    url_contents = response.json()
    photo_address_list = []
    for loop_content in url_contents:
        if 'video' in loop_content['media_type']:
            continue
        url = loop_content['url']
        photo_address_list.append(url)
    for number, picture in enumerate(photo_address_list):
        response_cycle = requests.get(picture)
        response_cycle.raise_for_status()
        path = 'images/nasa_apod_{0}{1}'.format(number, displays_image_format(response_cycle.url))
        download_files(path, response_cycle)


if __name__ == '__main__':
    load_dotenv()
    os.makedirs('images', exist_ok=True)
    nasa_key = os.environ['NASA_KEY']
    download_apod_photos(nasa_key)
