import discord 

from discord.ext import commands 

import random

import os

from dotenv import load_dotenv

from keep_alive import keep_alive

load_dotenv()

gif_list = ["https://media.giphy.com/media/SRISNle9ppFhizFkSo/giphy.gif?cid=ecf05e478tx4awncthjcoety9jpbazram6du0ir6uxs4enm1&rid=giphy.gif&ct=g", "https://media.giphy.com/media/iWTnpqPv2N1PG/giphy.gif?cid=ecf05e4709mld6mdjpwhpdyldy41w72fmgv4tajfdtffr2ha&rid=giphy.gif&ct=g", "https://media.giphy.com/media/lW0bCP325kDfi/giphy.gif?cid=ecf05e4709mld6mdjpwhpdyldy41w72fmgv4tajfdtffr2ha&rid=giphy.gif&ct=g", "https://media.giphy.com/media/xTiTncVep2khPGhK1i/giphy.gif?cid=ecf05e4709mld6mdjpwhpdyldy41w72fmgv4tajfdtffr2ha&rid=giphy.gif&ct=g", "https://media.giphy.com/media/qhlsTA1PWejaU/giphy.gif?cid=ecf05e4709mld6mdjpwhpdyldy41w72fmgv4tajfdtffr2ha&rid=giphy.gif&ct=g", "https://media.giphy.com/media/zWOnltJgKVlsc/giphy.gif?cid=ecf05e47mpygeoabjn19u52t3t0nulhk6zt68ml6r3aouguk&rid=giphy.gif&ct=g", "https://media.giphy.com/media/Xb4yTzWn71t9ZmqA5e/giphy.gif", "https://media.giphy.com/media/428dIJljoEbxS/giphy.gif", "https://media.giphy.com/media/d3YIeqQj0bCgFoNa/giphy.gif","https://i.imgur.com/douNF7E.jpg","https://i.imgur.com/RbLSBUu.gif","https://i.imgur.com/OecQFZJ.gif","https://i.imgur.com/BUOGMOZ.gif","https://i.imgur.com/tmUKNKf.jpg","https://i.imgur.com/D6mJDKg.gif","https://i.imgur.com/5NLYpcd.gif","https://images-ext-1.discordapp.net/external/4Xn8NRJfHh3LwV9ASJ8haSoQsE4DVaZUIS28gI_uhAU/https/i.imgur.com/JGXLvVq.jpg","https://images-ext-1.discordapp.net/external/wCjg7tc4c3w_TVWNiVuS55eJGO9MPBm3a2m-GjeGkpA/https/i.imgur.com/7rzw3Ev.jpg?width=568&height=406","https://images-ext-1.discordapp.net/external/cUPShXSiT6pudbYwUnnJoUCh6hyVuCsaWAzBsYHiFWo/https/i.imgur.com/nHTVRlR.jpg?width=455&height=406","https://i.imgur.com/ARN2NYT.gif","https://imgur.com/o8JndEn.gif ","https://i.imgur.com/PUIWTUk.gif","https://imgur.com/8Ct0PZp.gif ","https://images-ext-1.discordapp.net/external/DcGnLE9FX3_q7oC0h2g2boBSFG90QgXHTljdPQuD7Sk/https/i.imgur.com/7a4fBaW.jpg","https://images-ext-1.discordapp.net/external/RhkOM80dyKB-JNWuanjeHttLhAU1KDlebmEenA6QauU/https/i.imgur.com/EjCNIFr.jpg?width=406&height=406","https://i.imgur.com/RCCDQiP.gif","https://images-ext-2.discordapp.net/external/w4hzhwf-jEXUq1e9h350Cd5G7lGdusDaK1F_MGYBwjc/https/i.imgur.com/2RopyJP.jpg?width=324&height=406","https://imgur.com/IwS1Wn1.gif ","https://images-ext-1.discordapp.net/external/vhQjhMk0y2kH6a2RVWtNVzwh_Stli0jLgsFLmw-WUWs/https/i.imgur.com/LGFZ9A5.jpg?width=304&height=405","https://i.imgur.com/HUEPVFb.gif","https://i.imgur.com/9g7hDmb.gif","https://i.imgur.com/3KXpexE.gif","https://images-ext-2.discordapp.net/external/LhuD4EmpRaSWPZtxcPeBaDkCDmTJae8Hv-8Ofsdsx6Y/https/i.imgur.com/udWctui.jpg","https://imgur.com/OecQFZJ.gif "]

gif = random.choice(gif_list)

client = commands.Bot(command_prefix="w.")

@client.event

async def on_ready():

  await client.change_presence(status=discord.Status.idle, activity=discord.Game('w.waterhelp'))

  print("Bot is online")

@client.event

async def on_command_error(ctx, error):

  if ctx.channel.id == 874538486873620481:

    if isinstance(error, commands.CommandOnCooldown):

      day = round(error.retry_after/86400)

      hour = round(error.retry_after/3600)

      minute = round(error.retry_after/60)

      if day > 0:

        await ctx.send('This command is in cooldown right now, try again after '+str(day)+' day(s)')

      elif hour > 0:

        await ctx.send('This command is in cooldown right now, try again after '+str(hour)+' hour(s)')

      elif minute > 0:

        await ctx.send('This command is in cooldown right now, try again after '+str(minute)+ 'minute(s)')

      else:

        await ctx.send(f'This command is in cooldown right now, try again after {error.retry_after:.2f} second(s)')

  else:

    await ctx.send("<:dum:888023879979761664> You can use this command in <#874538486873620481> channel only")

@client.command()

@commands.cooldown(1,7200, commands.BucketType.guild)

async def water(ctx):

  if ctx.channel.id == 874538486873620481:

    embed = discord.Embed(title = "Water Ping",description = '''Drink your way to better health.\nStay hydrated!''',colour = discord.Colour.blue())

    embed.set_image(url=gif)

  

    await ctx.send("<@&874530032633151519> Time to drink water <:drinkwater:888001912627150849>")

    await ctx.send(embed=embed)

  else:

    return

@client.command()

async def waterhelp(ctx):

  embed = discord.Embed(title='Help',description='The prefix for the server is `w.` | Use `w.water` to get the ping of water reminder <:ZuckWater:887998417958227989> \nThere is cooldown for `w.water` command to prevent the spam\nThe cooldown time is 2hrs',color=discord.Color.blue())

  embed.set_image(url="https://cdn.discordapp.com/attachments/885099421006725150/887999564009832468/drink-water-stickers-drink-water-liquid-stickers-cartoon-220880353.jpg")

  await ctx.send(embed=embed)

keep_alive()

my_secret = os.environ['TOKEN']

client.run(my_secret)
