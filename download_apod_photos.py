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
    photo_address = []
    for url_content in url_contents:
        if 'video' in url_content['media_type']:
            continue
        url = url_content['url']
        photo_address.append(url)
    for number, picture in enumerate(photo_address):
        path = 'images/nasa_apod_{0}{1}'.format(number, displays_image_format(picture))
        download_files(picture, path)


if __name__ == '__main__':
    load_dotenv()
    os.makedirs('images', exist_ok=True)
    nasa_key = os.environ['NASA_KEY']
    download_apod_photos(nasa_key)
