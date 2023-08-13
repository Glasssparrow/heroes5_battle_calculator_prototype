import discord
from discord.ext import commands
from pandas import DataFrame
from test import test_battle
from for_discord_bot import TOKEN
from get_data.read_database import read_database
from constants import ALL_DATABASES
from commands import *


HELLO = ["hello"]
database = None
FACTIONS = None
FACTIONS_DICT = {}
tmp_database = DataFrame()

bot = commands.Bot(
    command_prefix="!",
    help_command=None,
    intents=discord.Intents.all()
)


@bot.event
async def on_ready():
    global database
    global FACTIONS
    global FACTIONS_DICT
    database = read_database(ALL_DATABASES)
    FACTIONS, FACTIONS_DICT = get_factions(database)
    print(f"Bot {bot.user} is ready to work.")


@bot.command()
async def get_database(ctx):
    await ctx.send(file=discord.File("database/test_database.xlsx"))


@bot.command()
async def test(ctx, unit1, unit2, quantity1, quantity2, type_of_quantity):
    try:
        test_battle(
            data=database,
            unit1_name=unit1, unit2_name=unit2, number_of_battles=1,
            quantity_type=type_of_quantity,
            quantity1=int(quantity1), quantity2=int(quantity2))
        await ctx.send(unit1)
        await ctx.send(file=discord.File("log/battle0.log"))
    except Exception:
        await ctx.send("Что то пошло не так =\\")
        raise


@bot.command()
async def help(ctx):
    await ctx.send(
        '!test "Название первого существа" "Название второго существа" '
        '"Количество первых существ" "Количество вторых существ" "Тип количества"\n'
        'Типы количества: "Количество", "Золото", "Прирост"\n'
        'Команда !battle работает так же как !test \n'
        'Получить список фракций "!factions"\n'
        'Получить список существ фракции "!faction Название"\n'
        'Получить базу данных "!get_database"\n'
        'Добавить своё существо \n'
        '!add "Название" "Атака" "Защита" "Мин урон" "Макс урон" "Здоровье"'
        '"Инициатива" "Скорость" "Выстрелы" "Мана" "Цена" "Опыт" "Прирост"'
        '"Прирост+" "Способность1, способность2" "Существо большое?" "Уровень"'
        '"Существо улучшенное?" "Фракция"\n'
        'Пример команды "!test":\n'
        '!test Крестьянин Ополченец 25 17 Количество\n'
        'Пример команды "!add":\n'
        '!add Крестьянин 1 1 1 1 3 8 4 0 0 15 4 22 0 "Живое существо" '
        'Нет 1 Нет "Орден порядка"'
    )


@bot.command()
async def stats(ctx, name):
    await ctx.send(
        stats_of_unit(database, name)
    )


@bot.command()
async def factions(ctx):
    await ctx.send(FACTIONS)


@bot.command()
async def faction(ctx, faction_name):

    await ctx.send(FACTIONS_DICT[faction_name])


@bot.command()
async def add(
        ctx, name,
        atk, defence, min_damage, max_damage, health, initiative, speed,
        ammo, mana, cost, exp, grow, extra_grow,
        abilities, big, level, upgraded, units_faction
):
    global tmp_database

    if upgraded == "Да":
        is_upgraded = 1
    else:
        is_upgraded = 0
    if big == "Да":
        is_big = 1
    else:
        is_big = 0

    error = ""

    numbers_list = [
        atk, defence, min_damage, max_damage,
        health, initiative, speed,
        ammo, mana, cost, exp, grow, extra_grow, level, ]
    if units_faction not in FACTIONS:
        error += f"Фракция {units_faction} не найдена.\n"
    if name in database.index:
        error += f"{name} уже в базе данных"
    for i, word in enumerate(numbers_list):
        try:
            numbers_list[i] = int(word)
        except:
            error += f"{i} не число\n"

    if error:
        await ctx.send(error)
    else:
        for k, v in {
            "Атака": int(atk),
            "Защита": int(defence),
            "Мин урон": int(min_damage),
            "Макс урон": int(max_damage),
            "Здоровье": int(health),
            "Инициатива": int(initiative),
            "Скорость": int(speed),
            "Выстрелы": int(ammo),
            "Мана": int(mana),
            "Цена": int(cost),
            "Опыт": int(exp),
            "Прирост": int(grow),
            "Прирост+": int(extra_grow),
            "Способности": abilities,
            "Большое": is_big,
            "Уровень": int(level),
            "Улучшение": is_upgraded,
            "Фракция": units_faction,
        }.items():
            tmp_database.loc[name, k] = v
            database.loc[name, k] = v
        await ctx.send(f"Существо {name} добавлено.")


@bot.command()
async def battle(ctx, unit1, unit2, quantity1, quantity2, type_of_quantity):
    try:
        result = test_battle(
            data=database,
            unit1_name=unit1, unit2_name=unit2, number_of_battles=100,
            quantity_type=type_of_quantity,
            quantity1=int(quantity1), quantity2=int(quantity2))
        await ctx.send(result)
    except Exception:
        await ctx.send("Что то пошло не так =\\")
        raise


bot.run(TOKEN)
