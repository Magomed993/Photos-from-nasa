import requests
import os
import argparse


def fetch_spacex_last_launch(arg=None):
    if arg is None:
        url = 'https://api.spacexdata.com/v5/launches/latest'
        response = requests.get(url)
        response.raise_for_status()
        resp_json = response.json()['links']['flickr']['original']
        for number, picture in enumerate(resp_json):
            with open('images/spacex_{0}.jpeg'.format(number), 'wb') as file:
                file.write(requests.get(picture).content)
    else:
        url = 'https://api.spacexdata.com/v5/launches/{0}'.format(arg)
        response = requests.get(url)
        response.raise_for_status()
        resp_json = response.json()['links']['flickr']['original']
        for number, picture in enumerate(resp_json):
            with open('images/spacex_{0}.jpeg'.format(number), 'wb') as file:
                file.write(requests.get(picture).content)


if __name__ == '__main__':
    os.makedirs('images', exist_ok=True)
    parser = argparse.ArgumentParser(description='Описание программы')
    parser.add_argument('--id', help='ID')
    args = parser.parse_args()
    try:
        fetch_spacex_last_launch(args.id)
        print('Если скачивание изображений не произошло, значит на дату запуска фотографий не было сделано.\n'
              'Введите id (дополнительный аргумент)')
    except requests.exceptions.HTTPError:
        print('Произошла ошибка. Id введен неверно!')
