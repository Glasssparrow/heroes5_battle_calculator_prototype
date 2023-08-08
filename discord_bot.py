import discord
from discord.ext import commands
from test import test_battle
from for_discord_bot import TOKEN
from get_data.read_database import read_database
from constants import ALL_DATABASES
from commands import *


HELLO = ["hello"]
DATABASE = None
FACTIONS = None

bot = commands.Bot(
    command_prefix="!",
    help_command=None,
    intents=discord.Intents.all()
)


@bot.event
async def on_ready():
    global DATABASE
    global FACTIONS
    DATABASE = read_database(ALL_DATABASES)
    FACTIONS = get_factions(DATABASE)
    print(f"Bot {bot.user} is ready to work.")


@bot.command()
async def test(ctx, unit1, unit2, quantity1, quantity2, type_of_quantity):
    try:
        test_battle(unit1, unit2, 1, type_of_quantity, int(quantity1), int(quantity2))
        await ctx.send(unit1)
        await ctx.send(file=discord.File("log/battle0.log"))
    except:
        await ctx.send("Что то пошло не так =\\")


@bot.command()
async def help(ctx):
    await ctx.send(
        '!test "Название первого существа" "Название второго существа" '
        '"Количество первых существ" "Количество вторых существ" "Тип количества"\n'
        'Типы количества: "Количество", "Золото", "Прирост"\n'
        'Получить список фракций "!factions"\n'
        'Пример команды "!test":\n'
        '!test Крестьянин Ополченец 25 17 Количество'
    )


@bot.command()
async def stats(ctx, name):
    await ctx.send(
        stats_of_unit(DATABASE, name)
    )


@bot.command()
async def factions(ctx):
    await ctx.send(FACTIONS)


@bot.command()
async def humans(ctx):

    await ctx.send(
        "Крестьянин\n"
        "Ополченец\n"
        "Лендлорд\n"
        "Лучник\n"
        "Арбалетчик\n"
        "Стрелок\n"
        "Мечник\n"
        "Латник\n"
        "Ревнитель веры\n"
        "Грифон\n"
        "Королевский грифон\n"
        "Боевой грифон\n"
        "Монах\n"
        "Инквизитор\n"
        "Адепт\n"
        "Рыцарь\n"
        "Паладин\n"
        "Рыцарь изабель\n"
        "Ангел\n"
        "Архангел\n"
        "Серафим"
    )


@bot.command()
async def forest_elfs(ctx):

    await ctx.send(
        "Существо\n"
        "Фея\n"
        "Дриада\n"
        "Нимфа\n"
        "Танцующий с клинками\n"
        "Танцующий со смертью\n"
        "Танцующий с ветром\n"
        "Эльфийский лучний\n"
        "Мастер лука\n"
        "Лесной стрелок\n"
        "Друид\n"
        "Верховный друид\n"
        "Старший друид\n"
        "Единорог\n"
        "Боевой единорог\n"
        "Светлый единорог\n"
        "Энт\n"
        "Древний энт\n"
        "Дикий энт\n"
        "Зеленый дракон\n"
        "Изумрудный дракон\n"
        "Кристаллический дракон\n"
    )


@bot.command()
async def mages(ctx):

    await ctx.send(
        "Гремлин\n"
        "Старший гремлин\n"
        "Гремлин-вредитель\n"
        "Каменная горгулья\n"
        "Обсидиановая горгулья\n"
        "Стихийная горгулья\n"
        "Железный голем\n"
        "Стальной голем\n"
        "Обсидиановый голем\n"
        "Маг\n"
        "Архимаг\n"
        "Боевой маг\n"
        "Джинн\n"
        "Султан джиннов\n"
        "Визирь джиннов\n"
        "Принцесса-ракшас\n"
        "Ракшас-раджа\n"
        "Кшатрий-ракшас\n"
        "Колосс\n"
        "Титан\n"
        "Громовержец\n"
    )

bot.run(TOKEN)
