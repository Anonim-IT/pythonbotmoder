import disnake
from disnake.ext import commands

class RP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message):
        """Обрабатывает упоминания бота."""
        if message.author.bot:
            return  # Игнорируем сообщения от ботов

        if self.bot.user.mentioned_in(message):
            await message.channel.send(f"Привет, {message.author.mention}! 🐾")

    # Слеш-команды
    @commands.slash_command(name="purr", description="Мурчание котика!")
    async def purr(self, interaction: disnake.ApplicationCommandInteraction, user: disnake.Member):
        """Мурчание котика для упомянутого пользователя."""
        embed = disnake.Embed(
            description=f"Мррррр! 🐾 Я мурчу для тебя, {user.mention}, лапка! 🐱💖",
            color=disnake.Color.gold()
        )
        await interaction.response.send_message(embed=embed)

    @commands.slash_command(name="lick_face", description="Лизнуть в лицо!")
    async def lick_face(self, interaction: disnake.ApplicationCommandInteraction, user: disnake.Member):
        """Лизнуть лицо упомянутого пользователя."""
        embed = disnake.Embed(
            description=f"Я лизнул лицо {user.mention}! 🐾 *нежно* 🐱💖",
            color=disnake.Color.gold()
        )
        await interaction.response.send_message(embed=embed)

    @commands.slash_command(name="hug", description="Обнимашки!")
    async def hug(self, interaction: disnake.ApplicationCommandInteraction, user: disnake.Member):
        """Обнять упомянутого пользователя."""
        embed = disnake.Embed(
            description=f"Я обнимаю {user.mention} крепко! 🐾 *обнимает* Мяу! 💖",
            color=disnake.Color.gold()
        )
        await interaction.response.send_message(embed=embed)

    @commands.slash_command(name="tail", description="Покачивание хвостиком!")
    async def tail(self, interaction: disnake.ApplicationCommandInteraction, user: disnake.Member):
        """Покачивание хвостиком для упомянутого пользователя."""
        embed = disnake.Embed(
            description=f"Мой хвостик машет влево и вправо, {user.mention}! 🐾💓 Мяу! 🐾",
            color=disnake.Color.gold()
        )
        await interaction.response.send_message(embed=embed)

    @commands.slash_command(name="growl", description="Рычание фурри!")
    async def growl(self, interaction: disnake.ApplicationCommandInteraction, user: disnake.Member):
        """Рычание для упомянутого пользователя."""
        embed = disnake.Embed(
            description=f"Гррррр... 🐾 Я рычу, как зверь, {user.mention}! Мяу!",
            color=disnake.Color.gold()
        )
        await interaction.response.send_message(embed=embed)

    @commands.slash_command(name="scratch", description="Царапание!")
    async def scratch(self, interaction: disnake.ApplicationCommandInteraction, user: disnake.Member):
        """Царапание упомянутого пользователя."""
        embed = disnake.Embed(
            description=f"Я немного поцарапаю тебя, {user.mention}, но это по-дружески! 🐾 *царапает* 🐱✨",
            color=disnake.Color.gold()
        )
        await interaction.response.send_message(embed=embed)

    @commands.slash_command(name="sniff", description="Понюхать воздух.")
    async def sniff(self, interaction: disnake.ApplicationCommandInteraction, user: disnake.Member):
        """Понюхать воздух рядом с упомянутым пользователем."""
        embed = disnake.Embed(
            description=f"Я нюхаю воздух рядом с тобой, {user.mention}... *нюхает* Хмм... Пахнет вкусно! 🐾👃",
            color=disnake.Color.gold()
        )
        await interaction.response.send_message(embed=embed)

    @commands.slash_command(name="lick", description="Лизание!")
    async def lick(self, interaction: disnake.ApplicationCommandInteraction, user: disnake.Member):
        """Лизнуть упомянутого пользователя."""
        embed = disnake.Embed(
            description=f"Я нежно лизнул тебя, {user.mention}... 🐾 Ласковое лизание! 🐱💖",
            color=disnake.Color.gold()
        )
        await interaction.response.send_message(embed=embed)

    @commands.slash_command(name="play", description="Поиграть с котиком!")
    async def play(self, interaction: disnake.ApplicationCommandInteraction, user: disnake.Member):
        """Предложить поиграть упомянутому пользователю."""
        embed = disnake.Embed(
            description=f"Играть со мной, {user.mention}? 🐾 Давай поиграем, лапка! 🎮🐱",
            color=disnake.Color.gold()
        )
        await interaction.response.send_message(embed=embed)

    @commands.slash_command(name="meow", description="Мяуканье фурри!")
    async def meow(self, interaction: disnake.ApplicationCommandInteraction, user: disnake.Member):
        """Мяуканье для упомянутого пользователя."""
        embed = disnake.Embed(
            description=f"Мяу! Мяу! 🐱 Мяуканье для тебя, {user.mention}! 💕",
            color=disnake.Color.gold()
        )
        await interaction.response.send_message(embed=embed)

    @commands.slash_command(name="cuddle", description="Потискать и прижать!")
    async def cuddle(self, interaction: disnake.ApplicationCommandInteraction, user: disnake.Member):
        """Потискать и прижать упомянутого пользователя."""
        embed = disnake.Embed(
            description=f"Я тебя прижимаю и тискаю, {user.mention}! 🐾 *обнимает крепко* 💖🐱",
            color=disnake.Color.gold()
        )
        await interaction.response.send_message(embed=embed)

    @commands.slash_command(name="nuzzle", description="Носик в носик!")
    async def nuzzle(self, interaction: disnake.ApplicationCommandInteraction, user: disnake.Member):
        """Носик в носик с упомянутым пользователем."""
        embed = disnake.Embed(
            description=f"Я прижимаю свой носик к твоему, {user.mention}! 🐾 *нuzzles* 🐱💖",
            color=disnake.Color.gold()
        )
        await interaction.response.send_message(embed=embed)

    @commands.slash_command(name="yawn", description="Зевота!")
    async def yawn(self, interaction: disnake.ApplicationCommandInteraction, user: disnake.Member):
        """Зевота рядом с упомянутым пользователем."""
        embed = disnake.Embed(
            description=f"Ох, как я зеваю... 🐾 *зевает* {user.mention}, ты тоже зеваешь? 😽",
            color=disnake.Color.gold()
        )
        await interaction.response.send_message(embed=embed)


    @commands.slash_command(name="pet", description="Погладить кого-то! 🐾")
    async def pet(interaction: disnake.ApplicationCommandInteraction, member: disnake.Member):
        """Позволяет погладить другого участника!"""
        await interaction.response.send_message(f"Мяу! {interaction.author.mention} гладит {member.mention}! 🐱💖")


    @commands.slash_command(name="hug", description="Обнять кого-то! 🤗")
    async def hug(interaction: disnake.ApplicationCommandInteraction, member: disnake.Member):
        """Позволяет обнять другого участника!"""
        await interaction.response.send_message(f"Мяу! {interaction.author.mention} обнимает {member.mention}! 🤗💖")


def setup(bot):
    bot.add_cog(RP(bot))
