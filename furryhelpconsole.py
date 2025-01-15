import disnake
from disnake.ext import commands

class FurryHelpConsole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message):
        """Обрабатывает упоминания бота."""
        if message.author.bot:
            return  # Игнорируем сообщения от ботов

        if self.bot.user.mentioned_in(message):
            await message.channel.send(f"Привет, {message.author.mention}! Используй слеш-команды для взаимодействия. 🐾")

    # Слэш-команда: furryhelpconsole
    @commands.slash_command(name="furryhelpconsole", description="Список консольных команд с фурри-темой.")
    async def furry_help_console(self, interaction: disnake.ApplicationCommandInteraction):
        help_text = (
            "`/ls` - Показать содержимое текущего каталога.\n"
            "`/pwd` - Показать текущий каталог.\n"
            "`/top` - Вывести процессы на сервере.\n"
            "`/df` - Информация о дисках и свободном месте.\n"
            "`/cat` - Показать содержимое файла.\n"
            "`/reload` - Перезагрузить бота.\n"
            "`/shutdown` - Остановить бота.\n"
            "`/status` - Проверить статус бота.\n"
            "`/log` - Показать логи бота.\n"
            "`/clearconsole` - Очистить чат.\n"
            "`/neofetch` - Вывести информацию о системе в стиле Neofetch.\n"
            "`/htop` - Вывести процессы в стиле htop.\n"
            "`/lsblk` - Показать информацию о блоках (дисках).\n"
            "`/uptime` - Время работы системы.\n"
            "`/whoami` - Текущий пользователь.\n"
            "`/free` - Информация о памяти.\n"
            "`/dmesg` - Сообщения ядра.\n"
            "`/ping` - Пинг хоста.\n"
            "`/history` - История команд.\n"
            "`/man` - Страница справочника для команды.\n"
            "`/uname` - Информация о системе.\n"
            "`/ps` - Запущенные процессы.\n"
            "`/id` - Информация о пользователе."
        )
        embed = disnake.Embed(
            title="Furry Help Console",
            description=help_text,
            color=disnake.Color.gold()
        )
        await interaction.response.send_message(embed=embed)

    # Слэш-команда: neofetch
    @commands.slash_command(name="neofetch", description="Вывести информацию о системе в стиле Neofetch.")
    async def neofetch(self, interaction: disnake.ApplicationCommandInteraction):
        system_info = """
        Host: Mojang Global Infrastructure
        Location: Stockholm, Sweden
        OS: Ubuntu 20.04.6 LTS x86_64
        Kernel: Linux 5.4.0-137-generic
        CPU: Intel Xeon Platinum 8272CL (26 cores)
        GPU: Software Renderer
        Memory: 128GB ECC DDR4
        Disk: 10TB NVMe SSD RAID-10
        Uptime: 12 days, 4 hours
        Load Average: 2.34, 2.12, 2.08
        Network: 10Gbps
        IP: 192.168.1.1
        Services: Docker, Java 17 Runtime
        """
        await interaction.response.send_message(f"```\n{system_info}\n```")

    # Слэш-команда: ls
    @commands.slash_command(name="ls", description="Показать содержимое текущего каталога.")
    async def ls(self, interaction: disnake.ApplicationCommandInteraction):
        files = ["bot.py", "config.json", "Dockerfile", "logs/", "requirements.txt", "README.md"]
        output = "\n".join(files)
        await interaction.response.send_message(f"```\n{output}\n```")

    # Слэш-команда: pwd
    @commands.slash_command(name="pwd", description="Показать текущий каталог.")
    async def pwd(self, interaction: disnake.ApplicationCommandInteraction):
        await interaction.response.send_message("```\n~/furry_bot/\n```")

    # Слэш-команда: top
    @commands.slash_command(name="top", description="Вывести процессы на сервере.")
    async def top(self, interaction: disnake.ApplicationCommandInteraction):
        processes = [
            "bot.py - 12.5% CPU - 1024MB RAM",
            "discord.py - 5.3% CPU - 512MB RAM",
            "python3 - 3.7% CPU - 256MB RAM"
        ]
        output = "\n".join(processes)
        await interaction.response.send_message(f"```\n{output}\n```")

    # Слэш-команда: df
    @commands.slash_command(name="df", description="Информация о дисках и свободном месте.")
    async def df(self, interaction: disnake.ApplicationCommandInteraction):
        disk_usage = [
            "Filesystem      Size  Used  Avail  Use%  Mounted on",
            "/dev/md0       100T   20T   80T    20%  /data",
            "/dev/sda1       1T    400G  600G   40%  /"
        ]
        output = "\n".join(disk_usage)
        await interaction.response.send_message(f"```\n{output}\n```")

    # Слэш-команда: cat
    @commands.slash_command(name="cat", description="Показать содержимое файла.")
    async def cat(self, interaction: disnake.ApplicationCommandInteraction, file: str):
        if file == "bot.log":
            log_content = "Bot started\nUser commands processed\nError: None\n"
        else:
            log_content = "Файл не найден."
        await interaction.response.send_message(f"```\n{log_content}\n```")

    # Слэш-команда: reload
    @commands.slash_command(name="reload", description="Перезагрузить бота.")
    async def reload(self, interaction: disnake.ApplicationCommandInteraction):
        await interaction.response.send_message("```\nПерезагружаю бота... Пожди немного... 🐾\n```")
        await interaction.followup.send("```\nБот успешно перезагружен! 🐾 Мяу!\n```")

    # Слэш-команда: shutdown
    @commands.slash_command(name="shutdown", description="Остановить бота.")
    async def shutdown(self, interaction: disnake.ApplicationCommandInteraction):
        await interaction.response.send_message("```\nОстанавливаю бота... Пока, лапка! 🐾\n```")
        await interaction.followup.send("```\nБот был остановлен... До свидания! 🐾\n```")

    # Слэш-команда: status
    @commands.slash_command(name="status", description="Проверить статус бота.")
    async def status(self, interaction: disnake.ApplicationCommandInteraction):
        status = "Бот работает стабильно 🐾. Время работы: 2 часа 30 минут."
        await interaction.response.send_message(f"```\n{status}\n```")

    # Слэш-команда: log
    @commands.slash_command(name="log", description="Показать логи бота.")
    async def log(self, interaction: disnake.ApplicationCommandInteraction):
        log_content = "Загружены последние данные. Ошибок не найдено."
        await interaction.response.send_message(f"```\n{log_content}\n```")

    # Слэш-команда: clearconsole
    @commands.slash_command(name="clearconsole", description="Очистить чат.")
    async def clearconsole(self, interaction: disnake.ApplicationCommandInteraction, amount: int = 10):
        if amount > 0:
            await interaction.channel.purge(limit=amount)
            await interaction.response.send_message(f"```\nЧат очищен на {amount} сообщений! 🧹🐾\n```")
        else:
            await interaction.response.send_message("```\nОшибка: Укажите корректное количество сообщений для удаления.\n```")

    # Слэш-команда: htop
    @commands.slash_command(name="htop", description="Вывести процессы в стиле htop.")
    async def htop(self, interaction: disnake.ApplicationCommandInteraction):
        htop_output = """
        top - 12:34:56 up 2:30,  1 user,  load average: 0.12, 0.08, 0.05
        Tasks: 105 total,   1 running,  104 sleeping,   0 stopped,   0 zombie
        %Cpu(s):  5.1 us,  2.4 sy,  0.0 ni, 91.8 id,  0.7 wa,  0.0 hi,  0.0 si,  0.0 st
        MiB Mem :  15999.2 total,   4563.7 free,   7121.5 used,   4314.0 buff/cache
        MiB Swap:   4096.0 total,   4096.0 free,      0.0 used.   7813.4 avail Mem 

        PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
        12345 bot      20   0  100000  12000   3500 S   12.3  0.8   1:12.34 bot.py
        23456 root     20   0  500000  20000   5000 S    3.2  1.3   0:12.56 python3
        34567 user     20   0  200000  15000   4000 S    2.4  0.9   0:02.34 discord.py
        """
        await interaction.response.send_message(f"```\n{htop_output}\n```")

    # Слэш-команда: lsblk
    @commands.slash_command(name="lsblk", description="Показать информацию о блоках (дисках).")
    async def lsblk(self, interaction: disnake.ApplicationCommandInteraction):
        lsblk_output = """
        NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
        sda      8:0    0  100G  0 disk 
        ├─sda1   8:1    0   40G  0 part /
        └─sda2   8:2    0   60G  0 part /data
        sdb      8:16   0  500G  0 disk 
        └─sdb1   8:17   0  500G  0 part /backup
        """
        await interaction.response.send_message(f"```\n{lsblk_output}\n```")

    # Слэш-команда: uptime
    @commands.slash_command(name="uptime", description="Вывести время работы системы.")
    async def uptime(self, interaction: disnake.ApplicationCommandInteraction):
        uptime_output = """
        2:30 up 3 days,  1 user,  load average: 0.10, 0.07, 0.03
        """
        await interaction.response.send_message(f"```\n{uptime_output}\n```")

    # Слэш-команда: whoami
    @commands.slash_command(name="whoami", description="Показать текущего пользователя.")
    async def whoami(self, interaction: disnake.ApplicationCommandInteraction):
        await interaction.response.send_message("```\nuser\n```")

    # Слэш-команда: free
    @commands.slash_command(name="free", description="Показать информацию о памяти.")
    async def free(self, interaction: disnake.ApplicationCommandInteraction):
        free_output = """
        Mem:   10485760 MB total,  5242880 MB free,  2621440 MB used,  2621440 MB cache
        Swap:  4194304 MB total,  2097152 MB free,  2097152 MB used
        """
        await interaction.response.send_message(f"```\n{free_output}\n```")

    # Слэш-команда: dmesg
    @commands.slash_command(name="dmesg", description="Показать сообщения ядра.")
    async def dmesg(self, interaction: disnake.ApplicationCommandInteraction):
        dmesg_output = """
        [  123.456] Kernel log start...
        [  125.789] Disk check successful
        [  130.001] Boot process completed successfully
        """
        await interaction.response.send_message(f"```\n{dmesg_output}\n```")

    # Слэш-команда: ping
    @commands.slash_command(name="ping", description="Пинговать хост.")
    async def ping(self, interaction: disnake.ApplicationCommandInteraction, host: str):
        ping_result = f"Пинг к {host}: 32ms"
        await interaction.response.send_message(f"```\n{ping_result}\n```")

    # Слэш-команда: history
    @commands.slash_command(name="history", description="Показать историю команд.")
    async def history(self, interaction: disnake.ApplicationCommandInteraction):
        history_output = """
        1. /ls
        2. /uptime
        3. /top
        4. /free
        """
        await interaction.response.send_message(f"```\n{history_output}\n```")

    # Слэш-команда: man
    @commands.slash_command(name="man", description="Показать справку для команды.")
    async def man(self, interaction: disnake.ApplicationCommandInteraction, command: str):
        man_page = f"Справка для команды {command}:\nИспользование команды для отображения информации.\n"
        await interaction.response.send_message(f"```\n{man_page}\n```")

    # Слэш-команда: uname
    @commands.slash_command(name="uname", description="Показать информацию о системе.")
    async def uname(self, interaction: disnake.ApplicationCommandInteraction):
        uname_output = "Linux FurryAI 5.15.0 #42 SMP Thu Jan 15 14:00:00 UTC 2025 x86_64 GNU/Linux"
        await interaction.response.send_message(f"```\n{uname_output}\n```")

    # Слэш-команда: ps
    @commands.slash_command(name="ps", description="Показать запущенные процессы.")
    async def ps(self, interaction: disnake.ApplicationCommandInteraction):
        processes = [
            "bot.py - 12.5% CPU - 1024MB RAM",
            "discord.py - 5.3% CPU - 512MB RAM",
            "python3 - 3.7% CPU - 256MB RAM"
        ]
        output = "\n".join(processes)
        await interaction.response.send_message(f"```\n{output}\n```")

    # Слэш-команда: id
    @commands.slash_command(name="id", description="Показать информацию о пользователе.")
    async def id(self, interaction: disnake.ApplicationCommandInteraction):
        user_info = f"User ID: {interaction.user.id}\nUsername: {interaction.user.name}"
        await interaction.response.send_message(f"```\n{user_info}\n```")

def setup(bot):
    bot.add_cog(FurryHelpConsole(bot))
