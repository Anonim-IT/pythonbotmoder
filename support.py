import disnake
from disnake.ext import commands

class Support(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def send_support_message(self, user):
        """Отправляет сообщение о поддержке."""
        embed = disnake.Embed(
            title="📩 Связь с техподдержкой",
            description=(
                "Мяу! Если у вас есть вопросы или проблемы, просто напишите сюда, "
                "и наша команда пушистиков обязательно поможет вам! 🐾\n\n"
                "**Техподдержка доступна:**\n"
                "• Через это сообщение.\n"
                "• Или через модераторов проекта."
            ),
            color=disnake.Color.orange()
        )
        embed.set_footer(text="Мы всегда готовы помочь! Мур-мур~")
        await user.send(embed=embed)

    @commands.slash_command(name="support", description="Связаться с техподдержкой.")
    async def support(self, inter: disnake.ApplicationCommandInteraction):
        """Слеш-команда для отправки сообщения о поддержке."""
        await inter.response.defer(ephemeral=True)  # Ответ только для пользователя
        try:
            await self.send_support_message(inter.user)
            await inter.edit_original_message(content="Мяу! Я отправил сообщение вам в личные сообщения! 🐾")
        except disnake.Forbidden:
            await inter.edit_original_message(content="Мяу! Не могу отправить сообщение в личные сообщения. Проверьте, открыты ли они. 🐾")

def setup(bot):
    bot.add_cog(Support(bot))
