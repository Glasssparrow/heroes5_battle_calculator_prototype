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
FACTIONS_DICT = {}

bot = commands.Bot(
    command_prefix="!",
    help_command=None,
    intents=discord.Intents.all()
)


@bot.event
async def on_ready():
    global DATABASE
    global FACTIONS
    global FACTIONS_DICT
    DATABASE = read_database(ALL_DATABASES)
    FACTIONS, FACTIONS_DICT = get_factions(DATABASE)
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
async def faction(ctx, faction_name):

    await ctx.send(FACTIONS_DICT[faction_name])

bot.run(TOKEN)
