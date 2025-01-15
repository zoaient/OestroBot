import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content  = True
bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())

token_file=open(".env")
TOKEN=token_file.read()
Bot_channel_id=1329186153378615336

@bot.event
async def on_ready():
    channel=bot.get_channel(Bot_channel_id)
    await channel.send("gros pd")

bot.run(TOKEN)