import os
import argparse
from publication_telegram_bot import sends_photo_by_bot
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
    sends_photo_by_bot(telega_api, chat_id, args.name)
