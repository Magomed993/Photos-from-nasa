import requests
import os
import argparse
from helper_script import download_file


def fetch_spacex_last_launch(arg):
    url = 'https://api.spacexdata.com/v5/launches/{0}'.format(arg)
    response = requests.get(url)
    response.raise_for_status()
    departure_images = response.json()['links']['flickr']['original']
    for number, picture in enumerate(departure_images):
        path = 'images/spacex_{0}.jpeg'.format(number)
        download_file(picture, path)


if __name__ == '__main__':
    os.makedirs('images', exist_ok=True)
    parser = argparse.ArgumentParser(description='''Производит скачивание последнего запуска 
    ракеты на последнюю дату. Есть возможность прописать дополнительный аргумент (id) запуска''')
    parser.add_argument('--id', help='ID', default='latest')
    args = parser.parse_args()
    fetch_spacex_last_launch(args.id)
