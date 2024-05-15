import os
import time
import argparse
from dotenv import load_dotenv
from publication_telegram_bot import sends_photo_by_bot


if __name__ == '__main__':
    load_dotenv()
    os.makedirs('images', exist_ok=True)
    telega_api = os.environ['TELEGA_API']
    chat_id = os.environ['TG_CHAT_ID']
    four_hours = 14400
    seconds = int(os.getenv('TIME', four_hours))
    parse = argparse.ArgumentParser(description='Описание программы')
    parse.add_argument('-n', '--name', help='photo name')
    args = parse.parse_args()
    while True:
        sends_photo_by_bot(telega_api, chat_id, args.name)
        time.sleep(seconds)
