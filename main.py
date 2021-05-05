import os
import discord
from discord.ext import commands
from discord_slash import SlashCommand # Importing the newly installed library.
from bolsacaos.caos import draw_caos

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(intents = intents, command_prefix='!LADA' , case_insesitive=True)
slash = SlashCommand(bot, sync_commands=True) # Declares slash commands through the client.

guild_ids = [555142549757493254,834195635574014043]

@bot.event
async def on_ready():
    print("Conectado correctamente con {0.user}".format(bot))

@bot.event
async def on_member_join(member):
  channel = bot.get_channel(834443569279664128)
  colorsenior = 0x3e55e4
  colormayor = 0xc2182b
  colorjunior = 0x337731
  colorsupremo = 0xf1c40f
  colorgeneral = 0x2f3136
  rolname = member.roles[1].name
  if rolname == 'Senior':
    colorrol = colorsenior
  elif rolname == 'Mayor':
    colorrol = colormayor
  elif rolname == 'Junior':
    colorrol = colorjunior
  elif rolname == 'Supremo':
    colorrol = colorsupremo
  else:
    colorrol = colorgeneral
  embed = discord.Embed (color=colorrol, title=f'Un nuevo archivero {rolname} se ha unido a la investigación' , description=f'Dad una buena bienvenida a {member.mention}!!')
  embed.set_thumbnail(url = member.avatar_url)
  await channel.send(embed=embed)

@slash.subcommand(base="lada",
                  name="caos",
                  description='Roba una ficha de la bolsa del caos',
                  guild_ids=guild_ids)
async def _caos(ctx): # Defines a new "context" (ctx) command called "ping."
  channel = bot.get_channel(ctx.channel_id)
  resultado = draw_caos (ctx)
  await ctx.send('Sacando un token de la bolsa del caos...')
  await channel.send(resultado)

@bot.command(name='test')
async def _test(ctx):
  colorsenior = 0x3e55e4
  colormayor = 0xc2182b
  colorjunior = 0x337731
  colorsupremo = 0xf1c40f
  colorgeneral = 0x2f3136
  channel = bot.get_channel(834443569279664128)
  #rolname = ctx.author.roles[1].name
  rolname = 'Mayor'
  if rolname == 'Senior':
    colorrol = colorsenior
  elif rolname == 'Mayor':
    colorrol = colormayor
  elif rolname == 'Junior':
    colorrol = colorjunior
  elif rolname == 'Supremo':
    colorrol = colorsupremo
  else:
    colorrol = colorgeneral

  embed = discord.Embed (color=colorrol, title=f'Un nuevo archivero {rolname} se ha unido a la investigación' , description=f'Dad una buena bienvenida a {ctx.author.mention}!!')
  embed.set_thumbnail(url = ctx.author.avatar_url)
  await channel.send(embed=embed)


bot.run(os.getenv('TOKEN'))