import telegram
import os
import random


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
