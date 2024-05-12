import telegram
import os
import argparse
import random
from dotenv import load_dotenv


def sending_photos(api, ch_id, arg=None):
    if arg is None:
        bot = telegram.Bot(token=api)
        directory = 'images/'
        files = os.listdir(directory)
        random_files = random.choice(files)
        bot.send_document(chat_id=ch_id, document=open(f'{directory}{random_files}', 'rb'))
    else:
        bot = telegram.Bot(token=api)
        bot.send_document(chat_id=ch_id, document=open(f'images/{arg}', 'rb'))


if __name__ == '__main__':
    load_dotenv()
    os.makedirs('images', exist_ok=True)
    telega_api = os.environ['TELEGA_API']
    chat_id = os.environ['CHAT_ID']
    parse = argparse.ArgumentParser(description='Описание программы')
    parse.add_argument('-n', '--name', help='photo name')
    args = parse.parse_args()
    try:
        sending_photos(telega_api, chat_id, args.name)
    except FileNotFoundError:
        print('Введите правильно наименование картинки или формат')
