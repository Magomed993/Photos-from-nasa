import requests
import os
import datetime
from dotenv import load_dotenv
from helper_script import download_file


def download_epic_photos(key):
    url = 'https://api.nasa.gov/EPIC/api/natural'
    payload = {
        'api_key': key,
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    url_contents = response.json()
    for number, url_content in enumerate(url_contents):
        name_image = url_content['image']
        date_time = url_content['date']
        date = datetime.datetime.fromisoformat(date_time)
        formatted_date = date.strftime('%Y/%m/%d')
        url_1 = 'https://api.nasa.gov/EPIC/archive/natural/{0}/png/{1}.png'.format(formatted_date,
                                                                                   name_image)
        path = 'images/epic_{0}.png'.format(number)
        download_file(url_1, path, payload)


if __name__ == '__main__':
    load_dotenv()
    os.makedirs('images', exist_ok=True)
    nasa_key = os.environ['NASA_KEY']
    download_epic_photos(nasa_key)
