import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

TOK_FILE = "token.txt"


card_type = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9"
]

card_color = [
    "Red",
    "Yellow",
    "Green",
    "Blue"
]

table = {}
public_cards = []

game = False



class cards:




def get_token():
    tokfile = open(TOK_FILE, 'r')
    token = tokfile.read()
    tokfile.close()
    return token


def pull_cards():
    card_type =
    card_color =
    card = cards(card_type, card_color).card_name()
    return card


@bot.tree.command(name="start")
async def start(interaction)

append




token = get_token()
bot.run(token)