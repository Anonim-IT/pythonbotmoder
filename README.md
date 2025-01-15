# FurryBot

**FurryBot** — это фурри-бот для Discord, который помогает следить за порядком, управлять ролями и поддерживать пушистую атмосферу на сервере. Он создан для того, чтобы сделать общение более уютным и приятным.

## 🐾 Мяу! Немного обо мне

Привет! Я твой пушистый помощник, всегда готов следить за порядком и помогать! ✨

Вот что я могу делать:
- 🐾 **Следить за порядком на сервере** — всегда вовремя! ⏰
- 📜 **Показывать правила** — не забудь их прочитать! 📚
- 💬 **Поддерживать пушистую атмосферу** — чат будет всегда уютным и добрым! 🐱

## Техническая информация

- **Написан на:** Python 🐍
- **Проект:** Anonim Community 🏡
- **Разработчики:** Множество замечательных людей, включая тебя! 🌟

## Установка

1. **Клонировать репозиторий**:
   Для начала необходимо клонировать репозиторий на свой компьютер. Используйте команду:
   ```
   git clone https://github.com/Anonim-IT/Furrybot.git
   cd Furrybot
   ```

2. **Установить зависимости**:
   Все необходимые зависимости для работы бота указаны в файле `requirements.txt`. Чтобы установить их, выполните:

   ```
   pip install -r requirements.txt
   ```

3. **Создать и настроить файл конфигурации**:
   Создайте файл `.env` в корне проекта и добавьте в него необходимые параметры, такие как токен вашего Discord бота и другие данные для подключения:

   Пример содержимого `.env`:
   ```
   DISCORD_TOKEN=ваш_токен
   SERVER_ID=ID_вашего_сервера
   ```

   **Обратите внимание**, что вам нужно получить токен бота через [Discord Developer Portal](https://discord.com/developers/applications), если у вас его еще нет.

4. **Запуск бота**:
   Теперь, когда все настроено, вы можете запустить бота с помощью следующей команды:

   ```bash
   python bot/main.py
   ```

   После этого бот начнет работать и подключится к вашему серверу Discord.

## Развертывание с Docker

Если вы хотите развернуть бота с помощью Docker, следуйте этим шагам:

1. **Собрать Docker-образ**:
   В директории с проектом выполните команду для сборки образа:

   ```bash
   docker build -t furrybot .
   ```

2. **Запустить контейнер**:
   После того как образ собран, запустите контейнер:

   ```bash
   docker run --env-file .env furrybot
   ```

   Это запустит бота внутри Docker-контейнера.

## Логи

Все действия бота логируются в файл `logs/bot.log`. Вы можете использовать этот файл для отслеживания активности бота и диагностики ошибок.

## Разработчики

- **Anonim** — Основной разработчик и создатель бота.
