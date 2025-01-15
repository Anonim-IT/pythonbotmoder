import disnake
from disnake.ext import commands
import aiohttp

# Ссылки на правила
BOT_RULES_URL = "https://raw.githubusercontent.com/AnonimCompani/botrules/refs/heads/main/README.md"
PROJECT_RULES_URL = "https://raw.githubusercontent.com/AnonimCompani/AnonimCommunityRules/refs/heads/main/README.md"  # Замените ссылку на реальную

class Rules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def fetch_rules(self, url):
        """Загружает правила с указанного URL."""
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    return "Мяу! Не удалось загрузить правила. Попробуйте позже. 🐾"

    @commands.slash_command(name="botrules", description="Показать правила использования бота.")
    async def show_bot_rules(self, inter: disnake.ApplicationCommandInteraction):
        """Слеш-команда для отображения правил бота."""
        await inter.response.defer()  # Откладываем ответ, чтобы показать загрузку
        bot_rules_content = await self.fetch_rules(BOT_RULES_URL)
        embed = disnake.Embed(
            title="📜 Мяу! Вот мои правила:",
            description=bot_rules_content[:4096],  # Ограничение на длину описания
            color=disnake.Color.blue()
        )
        embed.set_footer(text="Anonim Community Furry всегда на страже порядка! 🐾")
        await inter.edit_original_message(embed=embed)

    @commands.slash_command(name="projectrules", description="Показать правила проекта.")
    async def show_project_rules(self, inter: disnake.ApplicationCommandInteraction):
        """Слеш-команда для отображения правил проекта."""
        await inter.response.defer()  # Откладываем ответ, чтобы показать загрузку
        project_rules_content = await self.fetch_rules(PROJECT_RULES_URL)
        embed = disnake.Embed(
            title="📜 Правила проекта: мяу-мяу!",
            description=project_rules_content[:4096],  # Ограничение на длину описания
            color=disnake.Color.green()
        )
        embed.set_footer(text="Следуйте правилам, и у нас будет лапочково! 🐾")
        await inter.edit_original_message(embed=embed)

def setup(bot):
    bot.add_cog(Rules(bot))
