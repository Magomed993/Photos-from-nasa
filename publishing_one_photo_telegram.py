import os
import argparse
import random
from publication_telegram_bot import publishes_photo
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    os.makedirs('images', exist_ok=True)
    telega_api = os.environ['TELEGA_API']
    chat_id = os.environ['TG_CHAT_ID']
    parse = argparse.ArgumentParser(description='''Скачивает одно случайное фото. 
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
    publishes_photo(telega_api, file_path, chat_id)
