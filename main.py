import os

from discord.ext import commands
from discord_slash import SlashCommand # Importing the newly installed library.


bot = commands.Bot(command_prefix='!LADA ' , case_insesitive=True)
slash = SlashCommand(bot, sync_commands=True) # Declares slash commands through the client.

@bot.event
async def on_ready():
    print("Ready!")

guild_ids = [555142549757493254] # Put your server ID in this array.

@slash.slash(name="ping", description='Testear ping del bot', guild_ids=guild_ids)
async def _ping(ctx): # Defines a new "context" (ctx) command called "ping."
    await ctx.send(f"Pong! ({bot.latency*1000}ms)")



bot.run(os.getenv('TOKEN'))
