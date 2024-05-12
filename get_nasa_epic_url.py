import requests
import os
import datetime
from dotenv import load_dotenv
from helper_script import output_picture_format


def get_nasa_epic_url(key):
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


if __name__ == '__main__':
    load_dotenv()
    os.makedirs('images', exist_ok=True)
    nasa_key = os.environ['NASA_KEY']
    get_nasa_epic_url(nasa_key)
