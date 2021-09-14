"""
Boilerplate taken from
https://realpython.com/how-to-make-a-discord-bot-python/#what-is-a-bot
"""

import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL = os.getenv("CHANNEL")

bot = commands.Bot(command_prefix="-")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name="play")
async def play_single(context, *args):
    message = context.message
    if (message.webhook_id):
        # Message generated by a webhook and not a valid user.
        return
    # Message was sent by a valid user.
    
    user = message.author#.voice.voice_channel
    voice_state = user.voice
    
    # Bot will join the user's voice channel, if possible
    if (not voice_state):
        # User was not in a voice channel
        await context.send("User must be in a voice channel.")
        return

    channel = voice_state.channel
    await channel.connect()
    
bot.run(TOKEN)