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
open_cards = []
turn_list = []
turn_count = 0
game = False



class Uno_Card:
    def __init__(self,type,color):
        self.type = type
        self.suit = color

    def card_name(self):
        return self.type, self.color

def get_token():
    tokfile = open(TOK_FILE, 'r')
    token = tokfile.read()
    tokfile.close()
    return token


def pull_cards():
    card_type = random.choice(card_type)
    card_color = random.choice(card_color)
    card = Uno_Card(card_type, card_color).card_name()
    return card

def round_turn_update():
  global turn_count
  global round
  turn_count += 1
  if turn_count > len(turn_list) - 1:
    round += 1
    turn_count = 0


@bot.tree.command(name="PlayUno")
async def PlayUno(interaction: discord.Interaction):
    user_id = interaction.user
    if game == False:
        await interaction.response.send_message(f"Welcome to Uno {interaction.user.mention}")
    else:
        await interaction.response.send_message(f"{interaction.user.mention} a game is already in progress")


@bot.tree.command(name="start")
async def start(interaction: discord.Interaction):
    global game
    game = True
    global players
    players = list(table.keys())
    for x in players:
        



@bot.tree.command(name="get_cards")
async def get_cards(interaction: discord.Interaction):
    global game
    user_id = interaction.user
    if game == True:
        await interaction.response.send_message(f"your cards are {(table[user_id]['cards'])}", ephemeral=True)





token = get_token()
bot.run(token)