import requests
import os
from urllib.parse import urlparse


def displays_image_format(url):
    response = requests.get(url)
    response.raise_for_status()
    resp_parse = urlparse(response.url)
    path_separation = os.path.splitext(resp_parse.path)
    path_picture, changed_format = path_separation
    return changed_format


def download_files(path, response):
    with open(path, 'wb') as file:
        file.write(response.content)
