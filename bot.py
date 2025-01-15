import disnake
from disnake.ext import commands, tasks
import os
from dotenv import load_dotenv
import asyncio
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Загрузка токена из переменной окружения
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    logging.error("Токен не найден! Проверьте файл .env.")
    exit(1)

# Инициализация бота
intents = disnake.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(intents=intents)

status_messages = [
    "мурчание для всех лапок",
    "игру с пушистыми друзьями",
    "наблюдение за хвостиками",
    "прыжки по чатам Anonim Community",
    "собирает мурлыканья от фурри",
    "следит за порядком в Anonim Community",
    "игры с вашими сообщениями",
    "поиск новых игрушек в чате",
    "охоту за плохими сообщениями",
    "слежку за хвостиками фурри",
    "помощь в управлении Anonim Community Furry",
    "тихое рычание для порядку"
]

@bot.event
async def on_ready():
    print(f"Бот {bot.user} успешно запущен! 🐾")
    change_status.start()  # Запуск таска для смены статуса

    # Пушистый приветственный статус
    await bot.change_presence(activity=disnake.Game(name="готов к мурчанию! 🐾"))

@bot.event
async def on_message(message: disnake.Message):
    """Обработчик сообщений: отвечает 'Привет' на упоминание."""
    if message.author.bot:
        return

    if bot.user.mention in message.content:
        await message.channel.send(f"Мяу, {message.author.mention}! 🐾 Я тут, лапка!")
    await bot.process_commands(message)  # Обработка команд

@tasks.loop(seconds=60)
async def change_status():
    """Циклически меняет статус бота каждые 60 секунд."""
    for status in status_messages:
        await bot.change_presence(activity=disnake.Game(name=status))
        await asyncio.sleep(60)

# Пример слеш-команды очистки
@bot.slash_command(name="clear", description="Удалить указанное количество сообщений.")
async def clear(interaction: disnake.ApplicationCommandInteraction, amount: int):
    """Удаляет указанное количество сообщений."""
    if amount < 1:
        await interaction.response.send_message("Мяу! Укажи число больше 0, лапка!", ephemeral=True)
        return

    deleted = await interaction.channel.purge(limit=amount)
    embed = disnake.Embed(
        title="🧹 Очистка чата!",
        description=f"Мяу! Я удалил {len(deleted)} сообщений в этом канале.",
        color=disnake.Color.purple()
    )
    await interaction.response.send_message(embed=embed, ephemeral=True)

# Пример слеш-команды для тестирования
@bot.slash_command(name="hello", description="Поздороваться с ботом.")
async def hello(interaction: disnake.ApplicationCommandInteraction):
    """Пример слеш-команды."""
    await interaction.response.send_message(f"Привет, {interaction.author.mention}! 🐾 Мяу!")

# Загрузка команд из файлов
extensions = ["rules", "about", "support", "furryhelp", "rp", "furryhelpconsole", "moderation", "message_handler", "minecraft",]
for ext in extensions:
    try:
        bot.load_extension(ext)
        logging.info(f"Успешно загружено расширение {ext} 🐾")
    except Exception as e:
        logging.error(f"Ошибка при загрузке расширения {ext}: {e}")

# Запуск бота
bot.run(TOKEN)
