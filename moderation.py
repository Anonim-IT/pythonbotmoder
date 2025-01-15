import disnake
from disnake.ext import commands
from disnake import Member

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def perform_action(self, ctx, command, member, reason=None):
        """Выполняет действие в зависимости от команды."""
        if command == "ban":
            await self.ban(ctx, member, reason=reason)
        elif command == "kick":
            await self.kick(ctx, member, reason=reason)
        elif command == "warn":
            await self.warn(ctx, member, reason=reason)
        elif command == "mute":
            await self.mute(ctx, member, reason=reason)
        elif command == "unmute":
            await self.unmute(ctx, member)
        else:
            await ctx.send("Мяу! Команда не распознана.")

    @commands.slash_command(name="ban")
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: Member, reason="Не указана"):
        """Бан пользователя."""
        await member.ban(reason=reason)
        embed = disnake.Embed(
            title="🚫 Бан!",
            description=f"Мяу! Пользователь {member.mention} был забанен!\nПричина: **{reason}**",
            color=disnake.Color.red()
        )
        await ctx.send(embed=embed)

    @commands.slash_command(name="kick")
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: Member, reason="Не указана"):
        """Кик пользователя."""
        await member.kick(reason=reason)
        embed = disnake.Embed(
            title="👢 Кик!",
            description=f"Пользователь {member.mention} был кикнут из сервера.\nПричина: **{reason}**",
            color=disnake.Color.orange()
        )
        await ctx.send(embed=embed)

    @commands.slash_command(name="warn")
    @commands.has_permissions(administrator=True)
    async def warn(self, ctx, member: Member, reason="Не указана"):
        """Выдать предупреждение пользователю."""
        embed = disnake.Embed(
            title="⚠️ Предупреждение!",
            description=f"Мяу! Пользователь {member.mention} получил предупреждение.\nПричина: **{reason}**",
            color=disnake.Color.yellow()
        )
        await ctx.send(embed=embed)

    @commands.slash_command(name="mute")
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, member: Member, reason="Не указана"):
        """Замутить пользователя."""
        mute_role = disnake.utils.get(ctx.guild.roles, name="Muted")
        if not mute_role:
            mute_role = await ctx.guild.create_role(name="Muted")
            for channel in ctx.guild.channels:
                await channel.set_permissions(mute_role, speak=False, send_messages=False, add_reactions=False)
        await member.add_roles(mute_role, reason=reason)
        embed = disnake.Embed(
            title="🔇 Мут!",
            description=f"Мяу! Пользователь {member.mention} был замучен.\nПричина: **{reason}**",
            color=disnake.Color.blue()
        )
        await ctx.send(embed=embed)

    @commands.slash_command(name="unmute")
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, member: Member):
        """Размутить пользователя."""
        mute_role = disnake.utils.get(ctx.guild.roles, name="Muted")
        if mute_role in member.roles:
            await member.remove_roles(mute_role)
            embed = disnake.Embed(
                title="🔊 Размут!",
                description=f"Мяу! Пользователь {member.mention} был размучен.",
                color=disnake.Color.green()
            )
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"Мяу! Пользователь {member.mention} не был замучен.")

    @commands.Cog.listener()
    async def on_message(self, message):
        """Слушатель для обработки упоминаний бота с командами."""
        if self.bot.user in message.mentions:  # Если бот упомянут
            content = message.content.lower()
            if "ban" in content:
                member = message.mentions[0]  # Извлекаем упомянутого пользователя
                await self.perform_action(message, "ban", member)
            elif "kick" in content:
                member = message.mentions[0]  # Извлекаем упомянутого пользователя
                await self.perform_action(message, "kick", member)
            elif "warn" in content:
                member = message.mentions[0]  # Извлекаем упомянутого пользователя
                await self.perform_action(message, "warn", member)
            elif "mute" in content:
                member = message.mentions[0]  # Извлекаем упомянутого пользователя
                await self.perform_action(message, "mute", member)
            elif "unmute" in content:
                member = message.mentions[0]  # Извлекаем упомянутого пользователя
                await self.perform_action(message, "unmute", member)
            else:
                await message.channel.send("Мяу! Я не понимаю эту команду.")

def setup(bot):
    bot.add_cog(Moderation(bot))
