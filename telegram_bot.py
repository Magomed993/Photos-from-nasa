import telegram
import os
import time
import argparse
import random
from dotenv import load_dotenv


def sending_photos(api, ch_id, arg=None):
    if arg is None:
        bot = telegram.Bot(token=api)
        directory = 'images/'
        files = os.listdir(directory)
        random_files = random.choice(files)
        with open(f'{directory}{random_files}', 'rb') as save_file:
            bot.send_document(chat_id=ch_id, document=save_file)
    else:
        bot = telegram.Bot(token=api)
        with open(f'images/{arg}', 'rb') as save_file:
            bot.send_document(chat_id=ch_id, document=save_file)


if __name__ == '__main__':
    load_dotenv()
    os.makedirs('images', exist_ok=True)
    telega_api = os.environ['TELEGA_API']
    chat_id = os.environ['TG_CHAT_ID']
    seconds = int(os.getenv('TIME', 14400))
    parse = argparse.ArgumentParser(description='Описание программы')
    parse.add_argument('-n', '--name', help='photo name')
    args = parse.parse_args()
    try:
        while True:
            sending_photos(telega_api, chat_id, args.name)
            time.sleep(seconds)
    except FileNotFoundError:
        print('Введите правильно наименование картинки или формат')
