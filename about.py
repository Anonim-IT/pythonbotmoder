import disnake
from disnake.ext import commands
from disnake.ui import Button, View


class About(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="about", description="Информация о боте.")
    async def about(self, inter: disnake.ApplicationCommandInteraction):
        """Информация о боте с кнопками для последнего обновления."""

        # Создание кнопок
        update_button = Button(label="Последние обновления", style=disnake.ButtonStyle.primary,
                               custom_id="updates_button")

        # Вьюшка для кнопок
        view = View()
        view.add_item(update_button)

        # Эмбед с информацией о боте
        embed = disnake.Embed(
            title="🐾 Мяу! Немного обо мне:",
            description=(
                "Привет! Я твой пушистый помощник, всегда готов следить за порядком и помогать! ✨\n\n"
                "**Вот что я могу делать:**\n"
                "🐾 **Следить за порядком на сервере** — всегда вовремя! ⏰\n"
                "📜 **Показывать правила** — не забудь их прочитать! 📚\n"
                "💬 **Поддерживать пушистую атмосферу** — чат будет всегда уютным и добрым! 🐱\n\n"
                "**Написан на:** Python 🐍\n"
                "**Проект:** Anonim Community 🏡\n"
                "🛠 **Разработчики:** Множество замечательных людей, включая тебя! 🌟"
            ),
            color=disnake.Color.purple()
        )
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/1288861816763580488/a_dfd4cbe9dfbdbb1edf99e8a146103fff?size=256")  # Замените на URL изображения
        embed.set_footer(text="Спасибо, что выбрали меня! Мяу~ 🐾")

        await inter.response.send_message(embed=embed, view=view)

    # Обработка нажатия кнопки "Последние обновления"
    @commands.Cog.listener()
    async def on_button_click(self, inter: disnake.MessageInteraction):
        if inter.custom_id == "updates_button":
            # Эмбед с последними обновлениями
            update_embed = disnake.Embed(
                title="📢 Последние обновления бота:",
                description=(
                    "✨ **Версия 1.2.0** — добавлены новые команды для управления чатом и улучшения модерации!\n"
                    "🐾 **Версия 1.1.0** — улучшены слеш-команды и интеграция с Discord API.\n"
                    "💡 **Версия 1.0.0** — первый релиз бота с базовыми командами.\n"
                ),
                color=disnake.Color.green()
            )
            update_embed.set_footer(text="Спасибо, что используешь нашего пушистого бота!")
            await inter.response.send_message(embed=update_embed, ephemeral=True)


def setup(bot):
    bot.add_cog(About(bot))
