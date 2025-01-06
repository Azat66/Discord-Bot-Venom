import discord
from discord.ext import commands
import random

# Создаем экземпляр бота с необходимыми интентами
intents = discord.Intents.default()
intents.message_content = True  # Включаем интент для чтения содержимого сообщений
bot = commands.Bot(command_prefix='/', intents=intents)

# Список гифок
gifs = [
    "https://media.giphy.com/media/2Hudi43Wq1g14W0HzR/giphy.gif",
    "https://media.giphy.com/media/gPnBunez8PqGpG7thB/giphy.gif",
    "https://media.giphy.com/media/dDB4TCB9yb3pwmypoR/giphy.gif",
    "https://media.giphy.com/media/GIWweBqolpaQfKkQ2a/giphy.gif",
    "https://media.giphy.com/media/LWyBwSzX7iydxKz1eV/giphy.gif",
    "https://media.giphy.com/media/bzFPPzgTjvNhIVlgng/giphy.gif",
    "https://media.giphy.com/media/ifSj03tY2wf5CzCDPI/giphy.gif",
    "https://media.giphy.com/media/GcQ3xjOYZaYQbfnh92/giphy.gif",
    "https://media.giphy.com/media/lCJY93SVbrttRaEtcS/giphy.gif",
    "https://media.giphy.com/media/E1s18LCYTv12FnMNa6/giphy.gif",
]

# Ответы для команды Venom_ball
responses = [
    "Да, определенно!",
    "Я думаю, что это возможно.",
    "Сложно сказать, но попробуй.",
    "Лучше оставить это на будущее.",
    "Неа, не получится.",
    "Скорее всего, нет.",
    "Попробуй еще раз позже.",
    "Чего-то не хватает.",
    "Пока не знаю, возможно позже.",
    "Это не лучший вариант.",
    "Совсем не мой стиль.",
    "Пожалуй, это будет интересно.",
    "Мне это не по душе.",
    "Тебе решать!",
    "Звучит интригующе!",
    "Кто знает!",
    "Это твой шанс.",
    "Да, рискни!",
    "Абсолютно правильно.",
    "Сложная задача.",
    "Никогда не знаешь, пока не попробуешь.",
    "Это может сработать.",
    "Я в этом сомневаюсь.",
    "Вероятно, стоит попробовать.",
    "Возможно, ты прав.",
    "Все возможно в этом мире.",
    "Как посмотришь, так и будет.",
    "На это надо время.",
    "Это зависит от обстоятельств.",
    "Только в том случае, если...",
    "Звучит как план.",
    "Может быть стоит обдумать это еще раз.",
    "Может мне помочь?",
    "Не самое лучшее решение, но тоже вариант.",
]

# Команда Venom_gif
@bot.command()
async def Venom_gif(ctx):
    # Возвращаем одну случайную гифку
    gif = random.choice(gifs)
    await ctx.send("Вот случайная гифка:")
    await ctx.send(gif)

# Команда Venom_spam
@bot.command()
async def Venom_spam(ctx, count: int):
    if 1 <= count <= 10:
        for _ in range(count):
            await ctx.send("Спам от Venom")
    else:
        await ctx.send("Введите допустимое количество: от 1 до 10.")

# Команда Venom_commands
@bot.command()
async def Venom_commands(ctx):
    help_message = (
        "/Venom_gif - Показывает случайную гифку.\n"
        "/Venom_spam <количество> - Спам в чат (1-10 сообщений).\n"
        "/Venom_ball <вопрос> - Дает случайный ответ на ваш вопрос.\n"
        "/Venom_help - Показывает описание команд."
    )
    await ctx.send(help_message)

# Команда Venom_ball
@bot.command()
async def Venom_ball(ctx, *, question: str):
    response = random.choice(responses)
    await ctx.send(response)

# Новая команда Venom_help
@bot.command()
async def Venom_help(ctx):
    help_description = (
        "Я - бот Venom! Вот что я могу:\n"
        "/Venom_gif - Вернуть случайную гифку.\n"
        "/Venom_spam <количество> - Отправит указанное количество сообщений в чат.\n"
        "/Venom_ball <вопрос> - Ответит на ваш вопрос случайным образом.\n"
        "/Venom_commands - Показывает список команд."
    )
    await ctx.send(help_description)

# Сообщение при входе бота на сервер
@bot.event
async def on_ready():
    print(f'Бот {bot.user} успешно запущен!')
    
    # Приветственная сообщение в каждом текстовом канале, где бот имеет доступ
    for guild in bot.guilds:
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                await channel.send("Привет, я бот Venom! Я готов помогать вам. Используйте /Venom_commands для получения списка команд.")
                break  # Отправляем сообщение только в первый доступный текстовый канал

# Запуск бота

bot.run('Ваш токен бота') 
