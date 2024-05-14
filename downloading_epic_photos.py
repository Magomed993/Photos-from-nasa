import requests
import os
import datetime
from dotenv import load_dotenv
from helper_script import output_format_picture, downloading_file


def downloading_epic_photos(key):
    url = 'https://api.nasa.gov/EPIC/api/natural'
    payload = {
        'api_key': key,
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    url_contents = response.json()
    for number, loop_contents in enumerate(url_contents):
        name_image = loop_contents['image']
        date_time = loop_contents['date']
        date = datetime.datetime.fromisoformat(date_time)
        formatted_date = date.strftime('%Y/%m/%d')
        url_1 = 'https://api.nasa.gov/EPIC/archive/natural/{0}/png/{1}.png'.format(formatted_date,
                                                                                   name_image)
        response_cycle = requests.get(url_1, params=payload)
        response.raise_for_status()
        path = 'images/epic_{0}{1}'.format(number, output_format_picture(response_cycle.url))
        downloading_file(path, response_cycle)


if __name__ == '__main__':
    load_dotenv()
    os.makedirs('images', exist_ok=True)
    nasa_key = os.environ['NASA_KEY']
    downloading_epic_photos(nasa_key)
