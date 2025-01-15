import disnake
from disnake.ext import commands


class FurryHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Главная слэш-команда для вывода помощи
    @commands.slash_command(name="furryhelp", description="Получить помощь по доступным командам бота.")
    async def furryhelp(self, inter: disnake.ApplicationCommandInteraction):
        """Отправка кастомизированной помощи по командам."""
        embed = disnake.Embed(
            title="🌟 Помощь от пушистого модератора! 🌟",
            description=(
                "Привет, мяу! Вот список всех команд, которые ты можешь использовать с этим ботом. "
                "Ты также можешь пингануть меня с упомянанием команды.\n\n"
                "Нажми на кнопки ниже для навигации по категориям команд!"
            ),
            color=disnake.Color.blue()
        )

        embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/1288861816763580488/a_dfd4cbe9dfbdbb1edf99e8a146103fff?size=256"
        )

        embed.set_footer(
            text="Мяу! Если у тебя есть вопросы, не стесняйся использовать команду !support."
        )

        # Создаем кнопки для навигации по категориям команд
        button_about = disnake.ui.Button(label="Основные команды", custom_id="about_commands",
                                         style=disnake.ButtonStyle.primary)
        button_moderation = disnake.ui.Button(label="Команды модерации", custom_id="moderation_commands",
                                              style=disnake.ButtonStyle.success)
        button_rp = disnake.ui.Button(label="RP команды", custom_id="rp_commands", style=disnake.ButtonStyle.danger)
        button_linux = disnake.ui.Button(label="Linux помощь", custom_id="linux_help",
                                         style=disnake.ButtonStyle.secondary)

        # Добавляем кнопки в разметку
        action_row = disnake.ui.ActionRow(button_about, button_moderation, button_rp, button_linux)

        # Отправляем сообщение с embed и кнопками
        await inter.response.send_message(embed=embed, components=[action_row])

    # Обработчики кнопок
    @commands.Cog.listener()
    async def on_button_click(self, inter: disnake.MessageInteraction):
        """Обрабатывает нажатие на кнопки."""
        if inter.component.custom_id == "about_commands":
            await self.send_about_commands(inter)
        elif inter.component.custom_id == "moderation_commands":
            await self.send_moderation_commands(inter)
        elif inter.component.custom_id == "rp_commands":
            await self.send_rp_commands(inter)
        elif inter.component.custom_id == "linux_help":
            await self.send_linux_help(inter)

    async def send_about_commands(self, inter: disnake.MessageInteraction):
        """Отправка информации о основных командах."""
        embed = disnake.Embed(
            title="Основные команды:",
            description=(
                "/about — Узнать больше о боте и проекте.\n"
                "/support — Связаться с техподдержкой.\n"
                "/botrules — Показать правила.\n"
                "/projectrules — Показать правила проекта.\n"
            ),
            color=disnake.Color.purple()
        )
        await inter.response.edit_message(embed=embed)

    async def send_moderation_commands(self, inter: disnake.MessageInteraction):
        """Отправка команд модерации."""
        embed = disnake.Embed(
            title="Команды модерации:",
            description=(
                "/ban @пользователь [причина] — Забанить пушистика.\n"
                "/kick @пользователь [причина] — Кикнуть пушистика с сервера.\n"
                "/warn @пользователь [причина] — Выдать предупреждение.\n"
                "/mute @пользователь [причина] — Замутить пушистика.\n"
                "/unmute @пользователь — Размутить пушистика.\n"
            ),
            color=disnake.Color.orange()
        )
        await inter.response.edit_message(embed=embed)

    async def send_rp_commands(self, inter: disnake.MessageInteraction):
        """Отправка RP команд."""
        embed = disnake.Embed(
            title="RP команды:",
            description=(
                "/purr — Мурчание котика!\n"
                "/tail — Покачивание хвостиком!\n"
                "/bow — Поклон фурри!\n"
                "/growl — Рычание фурри!\n"
                "/scratch — Царапание!\n"
                "/sniff — Пахнет чем-то интересным!\n"
                "/lick — Лизание!\n"
                "/play — Поиграем вместе!\n"
                "/meow — Мяуканье фурри!\n"
                "/hug — Обнимашки!\n"
            ),
            color=disnake.Color.green()
        )
        await inter.response.edit_message(embed=embed)

    async def send_linux_help(self, inter: disnake.MessageInteraction):
        """Отправка помощи для работы в Linux."""
        embed = disnake.Embed(
            title="Помощь по работе в Linux:",
            description=(
                "/furryhelpcosole — Мурчание котика!\n"
            ),
            color=disnake.Color.red()
        )
        await inter.response.edit_message(embed=embed)


def setup(bot):
    bot.add_cog(FurryHelp(bot))
