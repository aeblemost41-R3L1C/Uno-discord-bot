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

hand = {} #Key = "user_id", Value = ["kort på hånd 1", "kort på hånd 2", etc.]
deck = [] # [] liste over alle kort man kan trække
ActiveCard = [] # [] = de fjernede kort fra "User_cards" tilføjes hertil, og det aktive kort opdateres

turn_list = [] #
turn_count = 0
game = False

class Uno_Card:
    def __init__(self,type,color):
        self.type = type
        self.color = color

    def card_name(self):
        return self.type, self.color
    
def get_token():
    tokfile = open(TOK_FILE, 'r')
    token = tokfile.read()
    tokfile.close()
    return token

def get_cards(user_id):
    cards = []
    random.shuffle(deck)
    for i in range(7):
        cards.append(deck[0].card_name())
        deck.pop(0) 
    return cards

def round_turn_update():
  global turn_count
  global round
  turn_count += 1
  if turn_count > len(turn_list) - 1:
    round += 1
    turn_count = 0


@bot.tree.command(name="playuno")
async def PlayUno(interaction: discord.Interaction):
    user_id = interaction.user.id
    hand[user_id] = []
    if game == False:
        await interaction.response.send_message(f"Welcome to Uno {interaction.user.mention}")
    else:
        await interaction.response.send_message(f"{interaction.user.mention} a game is already in progress")

"""
@bot.tree.command(name="start")
async def start(interaction: discord.Interaction):
    global game
    game = True
    global players
    players = list(playcard.keys())
    for x in players:
        card_1 = get_cards()
        User_cards[x]["cards"].append(card_1)
        turn_list.append(x)
    await interaction.response.send_message("siiuuu")
"""

@bot.tree.command(name="start")
async def start(interaction: discord.Interaction):
    global game
    game = True
    global players

    for color in card_color:
        for type in card_type:
           deck.append(Uno_Card(type, color))
           deck.append(Uno_Card(type, color))

    for card in deck:
       print(f"{card.type} {card.color}")
    
    players = hand.keys()
    print(players)
    for user_id in players:
       print(user_id)
       cards = get_cards(user_id)
       hand[user_id] = cards
    
  



    """
    players = list(hand.keys())
    for x in players:
        deck = get_cards()
        hand[x]["cards"].append(deck)
        turn_list.append(x)
    """
    await interaction.response.send_message("Starting Game")


@bot.tree.command(name="draw")
async def draw_cards(interaction: discord.Interaction):
   user_id = interaction.user.id

            
   
   




@bot.tree.command(name="see_cards")
async def see_cards(interaction: discord.Interaction):
    global game
    user_id = interaction.user.id
    if game == True:
        await interaction.response.send_message(f"your cards are {(hand[user_id])}", ephemeral=True)






@bot.event
async def on_ready():
  print("connected")
  try:
    synced = await bot.tree.sync()
    print(f"s'Synced {len(synced)} command(s)")
  except Exception as e:
    print(e)

token = get_token()
bot.run(token)