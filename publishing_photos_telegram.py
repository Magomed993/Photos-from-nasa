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
    parse = argparse.ArgumentParser(description='''Отправляет все имеющиеся в папке 
    фотографии cогласно заданному времени или 4 часам.
    После отправки всех фотографий данные в папке отправляются повторно в бесконечном цикле.\n
    Есть возможность отправить фото прописав дополнительный аргумент с наименованием файла 
    и отправка данного файла будет происходить бесконечно''')
    parse.add_argument('-n', '--name', help='photo name')
    args = parse.parse_args()
    while True:
        if args.name is None:
            directory = 'images/'
            files = os.listdir(directory)
            random.shuffle(files)
            for file_name in files:
                file_path = f'{directory}{file_name}'
                publishes_photo(telega_api, file_path, chat_id)
                time.sleep(seconds)
        else:
            file_path = f'images/{args.name}'
            publishes_photo(telega_api, file_path, chat_id)
            time.sleep(seconds)
