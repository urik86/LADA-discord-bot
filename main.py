import os

from discord.ext import commands
from discord_slash import SlashCommand # Importing the newly installed library.
from bolsacaos.caos import draw_caos


bot = commands.Bot(command_prefix='!LADA ' , case_insesitive=True)
slash = SlashCommand(bot, sync_commands=True) # Declares slash commands through the client.

guild_ids = [555142549757493254]

@bot.event
async def on_ready():
    print("Ready!")
@slash.slash(name="caos", description='Roba una ficha de la bolsa del caos', guild_ids=guild_ids)
async def _caos(ctx): # Defines a new "context" (ctx) command called "ping."
  channel = bot.get_channel(ctx.channel_id)
  resultado = draw_caos (ctx)
  await ctx.send('Sacando un token de la bolsa del caos...')
  await channel.send(resultado)

bot.run(os.getenv('TOKEN'))