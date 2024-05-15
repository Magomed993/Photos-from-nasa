import telegram
import os
import argparse
import random
from dotenv import load_dotenv


def sends_photo_by_bot(api, ch_id, arg=None):
    if arg is None:
        directory = 'images/'
        files = os.listdir(directory)
        random_files = random.choice(files)
        file_path = f'{directory}{random_files}'
    else:
        file_path = f'images/{arg}'
    publishes_photo(api, file_path, ch_id)


def publishes_photo(api, path, ch_id):
    bot = telegram.Bot(token=api)
    with open(path, 'rb') as save_file:
        bot.send_document(chat_id=ch_id, document=save_file)


if __name__ == '__main__':
    load_dotenv()
    os.makedirs('images', exist_ok=True)
    telega_api = os.environ['TELEGA_API']
    chat_id = os.environ['TG_CHAT_ID']
    parse = argparse.ArgumentParser(description='''Скачивает одно случайное фото. 
    Есть возможность скачать фото прописав дополнительный аргумент с наименованием файла''')
    parse.add_argument('-n', '--name', help='photo name')
    args = parse.parse_args()
    sends_photo_by_bot(telega_api, chat_id, args.name)
