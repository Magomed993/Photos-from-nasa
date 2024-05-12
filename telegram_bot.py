import telegram
import os
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    telega_api = os.environ['TELEGA_API']
    chat_id = os.environ['CHAT_ID']
    bot = telegram.Bot(token=telega_api)
    bot.send_message(chat_id=chat_id, text="Привет, Ку-Ку.")
    bot.send_document(chat_id=chat_id, document=open('images/hubble.jpeg', 'rb'))
    