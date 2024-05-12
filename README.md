# Космический Телеграм
Проект производит скачивание картинок с сайта, а также публикацию в группу социальной сети Телеграм
## Как установить
Python3 должен быть уже установлен. Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:

	pip install -r requirements.txt
## Окружения
Необходимо сгенерировать `API Key` на сайте [NASA](https://api.nasa.gov).
Сгенерировать в мессенджере телеграм `API token` и его адрес у [Отца Ботов](https://telegram.me/BotFather).
## Переменные окружения
Сгенерированный API необходим для установления переменной окружения в секретный файл формата `.env`.
### Как получить
Для корректной работы `.env` задать в файле `.env` наименование переменной окружения схожей в имеющемся коде, например, `NASA_KEY=(ваш ключ)`,
`TELEGA_API=(ваш ключ)` и `CHAT_ID=(адрес группы где бует установлен бот)`\
## Исключения
Из файла `.gitignore` исключить формат `.env` для корректного запуска.
## Запуск
Запускать данный проект через командную строку, 
в которой изначально указывается путь к местонахождению скрипта `наименование скрипта.py` и далее запуск.
А также возможно запускать данный проект через любую IDE (интегрированная среда разработки).
