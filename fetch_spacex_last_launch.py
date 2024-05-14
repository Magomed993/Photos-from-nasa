import requests
import os
import argparse
from helper_script import downloading_file


def fetch_spacex_last_launch(arg):
    url = 'https://api.spacexdata.com/v5/launches/{0}'.format(arg)
    response = requests.get(url)
    response.raise_for_status()
    departure_image = response.json()['links']['flickr']['original']
    for number, picture in enumerate(departure_image):
        response_cycle = requests.get(picture)
        response_cycle.raise_for_status()
        path = 'images/spacex_{0}.jpeg'.format(number)
        downloading_file(path, response_cycle)


if __name__ == '__main__':
    os.makedirs('images', exist_ok=True)
    parser = argparse.ArgumentParser(description='''Производит скачивание последнего запуска 
    ракеты на последнюю дату. Есть возможность прописать дополнительный аргумент (id) запуска''')
    parser.add_argument('--id', help='ID', default='latest')
    args = parser.parse_args()
    fetch_spacex_last_launch(args.id)
