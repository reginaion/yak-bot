
import discord
import asyncio
import datetime
import pytz
import os
from discord.ext import commands
from discord.ext import tasks


intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=';', intents=intents)

alarm_time = '23:03'#24hrs
channel_id = 387998196422672386
channel_id_2 = 925725103801630761
channel_id_test = 925763452281159680
channel_id_invent = 702741572344610910


@client.event
async def on_member_join(member):
    channel = client.get_channel(channel_id_invent)
    #await member.send('Private message')
    embed=discord.Embed(title=f"ようこそジャパリパークへ! {member.name}", description=f"感謝您加入 {member.guild.name}!\n請至<#925781066990624858>索取身分組 {member.guild.id} {str(type(member.guild.id))}") # F-Strings!
    embed.set_thumbnail(url=member.avatar_url) # Set the embed's thumbnail to the member's avatar image!
    await channel.send(embed=embed)

#@client.event
#async def on_member_remove(member):
#    channel = client.get_channel(channel_id_test)
#    message = "Recognised that a member called " + member.name + " left"
#    await channel.send(discord.Object(id=channel_id_invent), member.name + ' left')

@client.event
async def on_ready():
    activity = discord.Game(name="command list: [;help, ;shutdown]")
    await client.change_presence(status=discord.Status.online, activity=activity)
    #await client.change_presence(activity=activity)
    #await client.change_presence(activity=discord.Streaming(name='Fortnite', url='https://www.twitch.tv/UR_TWITCH_GOES_HERE You cant do YT only Twitch.'))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command()
@commands.is_owner()
async def send_2(ctx, *, message:str):
    #channel = client.get_channel(channel_id)
    channel = client.get_channel(channel_id_2)
    await channel.send(message)

@client.command()
@commands.is_owner()
async def send(ctx, *, message:str):
    #channel = client.get_channel(channel_id)
    channel = client.get_channel(channel_id)
    await channel.send(message)


@client.command()
@commands.is_owner()
async def send_t(ctx, *, message:str):
    #channel = client.get_channel(channel_id)
    channel = client.get_channel(channel_id_test)
    await channel.send(message)
"""
@client.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@client.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@client.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@client.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@client.command()
async def info(ctx):
    embed = discord.Embed(title="nice bot", description="Nicest bot there is ever.", color=0xeee657)
    
    # give info about you here
    embed.add_field(name="Author", value="<YOUR-USERNAME>")
    
    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(client.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="[Invite link](<insert your OAuth invitation link here>)")

    await ctx.send(embed=embed)

client.remove_command('help')

@client.command()
async def help(ctx):
    embed = discord.Embed(title="nice bot", description="A Very Nice bot. List of commands are:", color=0xeee657)

    embed.add_field(name=";add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name=";multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name=";greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name=";cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name=";info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name=";help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)
"""
# Close the bot
@client.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("The bot will shutdown await a minute")
    await ctx.bot.close()

@tasks.loop(minutes=1)
async def time_check():
    cst = datetime.datetime.now(tz=pytz.timezone('Asia/Taipei')).time()
    weekday = datetime.datetime.now(tz=pytz.timezone('Asia/Taipei')).weekday()
    if weekday == 6 and cst.hour == 22 and cst.minute == 30:
        await client.wait_until_ready()
        channel = client.get_channel(channel_id)
        await channel.send('```客家道場```')
    if weekday == 6 and cst.hour == 22 and cst.minute == 35:
        await client.wait_until_ready()
        channel = client.get_channel(channel_id_2)
        await channel.send('```客家道場```')

#Mod Leave Announcement
"""
@client.event
async def on_member_remove(member):
    print("Recognized that " + member.name + " left")
    await client.send_message(discord.Object(id=702741572344610910), '**' + member.mention + '** just left.')
    print("Sent message to #CHANNEL")
"""


time_check.start()

client.run(os.getenv('BOT_TOKEN'))