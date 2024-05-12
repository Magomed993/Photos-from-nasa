import requests
import os
from urllib.parse import urlparse


def get_picture(url):
    headers = {
        'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (HTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    with open('images/hubble.jpeg', 'wb') as file:
        file.write(response.content)


def output_picture_format(url):
    response = requests.get(url)
    response.raise_for_status()
    resp_parse = urlparse(response.url)
    path_separation = os.path.splitext(resp_parse.path)
    path_picture, changed_format = path_separation
    return changed_format


if __name__ == '__main__':
    url_picture = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    os.makedirs('images', exist_ok=True)
    get_picture(url_picture)
