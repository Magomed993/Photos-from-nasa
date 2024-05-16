import os
import time
import argparse
import random
from dotenv import load_dotenv
from publication_telegram_bot import publishes_photo


if __name__ == '__main__':
    load_dotenv()
    os.makedirs('images', exist_ok=True)
    telega_api = os.environ['TELEGA_API']
    chat_id = os.environ['TG_CHAT_ID']
    four_hours = 14400
    seconds = int(os.getenv('TIME', four_hours))
    parse = argparse.ArgumentParser(description='''Скачивает фотографии в бесконечном цикле.
    Есть возможность скачать фото прописав дополнительный аргумент с наименованием файла''')
    parse.add_argument('-n', '--name', help='photo name')
    args = parse.parse_args()
    if args.name is None:
        directory = 'images/'
        files = os.listdir(directory)
        random_files = random.choice(files)
        file_path = f'{directory}{random_files}'
    else:
        file_path = f'images/{args.name}'
    while True:
        publishes_photo(telega_api, file_path, chat_id)
        time.sleep(seconds)
