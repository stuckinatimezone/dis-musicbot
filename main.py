from random import choice
import discord
from discord.ext import commands, tasks
from music import Player

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="&", intents=intents)

status = ['Music', 'Mario', 'Sleeping', 'poptropica', 'fantage', 'Heat waves', 'I love you han', 'with a million lives', 'shes cute', 'I am in love', 'Rocket league', 'Detroit become human', 'Resting', 'Alive', 'with han',]

@bot.event
async def on_ready():
    change_status.start()
    print(f"{bot.user.name} is up and running.")

async def setup():
    await bot.wait_until_ready()
    bot.add_cog(Player(bot))

@tasks.loop(seconds=30)
async def change_status():
    await bot.change_presence(activity=discord.Game(choice(status)))

bot.loop.create_task(setup())

bot.run("TOKEN")
