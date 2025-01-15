import disnake
from disnake.ext import commands
import datetime


class SystemMessages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def generate_message(self, username, title, body, footer):
        """Генерирует системное сообщение для указанного пользователя."""
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        message = f"""
**Уведомление от системы Anonim Furry**  

Уважаемый {username},  

{title}  

{body}

Дата и время отправки: **{current_time}**.

{footer}
        """
        return message

    async def send_system_message(self, user, title, body, footer):
        """Отправляет системное сообщение конкретному пользователю."""
        system_message = await self.generate_message(user.name, title, body, footer)
        await user.send(system_message)  # Отправляем личное сообщение пользователю

    @commands.slash_command(name="system_notify", description="Отправить системное уведомление пользователю.")
    async def system_notify(
        self,
        inter: disnake.ApplicationCommandInteraction,
        user: disnake.User = commands.Param(description="Пользователь для уведомления"),
        title: str = commands.Param(description="Заголовок уведомления"),
        body: str = commands.Param(description="Основной текст уведомления"),
        footer: str = commands.Param(description="Текст внизу уведомления")
    ):
        """Слеш-команда для отправки системного уведомления пользователю."""
        await self.send_system_message(user, title, body, footer)
        await inter.response.send_message(f"Сообщение отправлено пользователю {user.name}.", ephemeral=True)


def setup(bot):
    bot.add_cog(SystemMessages(bot))
