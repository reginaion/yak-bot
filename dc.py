
import discord
import asyncio
import datetime
import pytz
import os
from discord.ext import commands
from discord.ext import tasks


intents = discord.Intents.all()
intents.members = True
intents.reactions = True
client = commands.Bot(command_prefix=';', intents=intents)

alarm_time = '23:03'#24hrs
channel_id = 387998196422672386
channel_id_2 = 925725103801630761
channel_id_test = 925763452281159680
#invite_guild_id = 702741572344610907
#invite_channel_id = 702741572344610910
#channel_id_message_channel_1 = 925763452281159680
#channel_id_message_role_1 = 925783864092270672
invite_guild_id = 925717530545377331
invite_channel_id = 925725103801630761
channel_id_message_channel_1 = 925732268197167125
channel_id_message_role_1 = 925960555943051284

role_id = ["探險隊隊長","KemoV粉絲","禁區許可證"]
role_emoji = ["<:geofforyA:925962558349934593>","<:dholeA:925962613718929490>","🔞"]


@client.event
async def on_member_join(member):
    if member.guild.id == invite_guild_id:
        #guild = client.get_guild(invite_guild_id)
        #role = discord.utils.get(guild.roles, name="遊客")
        #await member.add_roles(role)

        channel = client.get_channel(invite_channel_id)
        #await member.send('Private message')
        embed=discord.Embed(title=f"ようこそジャパリパークへ! {member.name}", description=f"感謝您加入 {member.guild.name}!\n請至<#925779385729032262>閱讀守則\n請至<#925732268197167125>釘選處索取身分組以取得頻道瀏覽權限") # F-Strings!
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

@client.command()
@commands.is_owner()
async def send_s(ctx, channel_id_s:int, *, message:str):
    #channel = client.get_channel(channel_id)
    channel = client.get_channel(channel_id_s)
    await channel.send(message)

@client.command()
@commands.is_owner()
async def edit_invite(ctx):
    embedvar = discord.Embed(title="請選取身分組!",
                              description="Click the corresponding emoji to receive your role.\n\
                                          {} - {}\n\
                                          {} - {}\n\
                                          {} - {}".format(role_emoji[0],"<@&925727966137290774>",role_emoji[1],"<@&925729158577930310>",role_emoji[2],"<@&925895939628105778>"), color=0x00ff00)
    channel = client.get_channel(channel_id_message_channel_1)
    msg = await channel.fetch_message(channel_id_message_role_1)
    await msg.edit(content="頻道群組︰\n\
<#926715406683615294> - 閒聊\n\
<#925733227841343508> - けもフレ3\n\
<#925722952568279091> - けもV\n\
　\n\
身分組︰\n\
<@&925727966137290774> - 動物朋友3玩家\n\
<@&925729158577930310> - 動物朋友V粉絲\n\
<@&925895939628105778> - R18頻道\n\
",embed=embedvar)
    await msg.add_reaction(role_emoji[0])
    await msg.add_reaction(role_emoji[1])
    await msg.add_reaction(role_emoji[2])

@client.event
async def on_raw_reaction_add(payload):
    guild = client.get_guild(payload.guild_id)
    member = discord.utils.get(guild.members, id=payload.user_id)
    # channel and message IDs should be integer:
    if payload.message_id == channel_id_message_role_1:
        if str(payload.emoji) == role_emoji[0]:
            role = discord.utils.get(guild.roles, name=role_id[0])
        elif str(payload.emoji) == role_emoji[1]:
            role = discord.utils.get(guild.roles, name=role_id[1])
        elif str(payload.emoji) == role_emoji[2]:
            role = discord.utils.get(guild.roles, name=role_id[2])

        if role is not None:
            await payload.member.add_roles(role)


@client.event
async def on_raw_reaction_remove(payload):
    guild = client.get_guild(payload.guild_id)
    member = discord.utils.get(guild.members, id=payload.user_id)

    if payload.message_id == channel_id_message_role_1:
        if str(payload.emoji) == role_emoji[0]:
            role = discord.utils.get(guild.roles, name=role_id[0])
        elif str(payload.emoji) == role_emoji[1]:
            role = discord.utils.get(guild.roles, name=role_id[1])
        elif str(payload.emoji) == role_emoji[2]:
            role = discord.utils.get(guild.roles, name=role_id[2])

        if role is not None:
            await member.remove_roles(role)


async def on_message_delete(message):
    channel = client.get_channel(925763452281159680)
    await channel.send(f"{deleter.name} deleted message by {message.author.name}")
    if message.guild.id == 702741572344610907:
        async for entry in message.guild.audit_logs(limit=1,action=discord.AuditLogAction.message_delete):
            deleter = entry.user
        channel = client.get_channel(925763452281159680)
        await channel.send(f"{deleter.name} deleted message by {message.author.name}")

"""
@client.event
async def on_raw_reaction_add(payload):
    msgID = channel_id_message_role_1
    guild = client.get_guild(payload.guild_id)
    role = discord.utils.get(guild.roles, name='test_role_1')
    if payload is not None:
        if payload.message_id == msgID:
            if str(payload.emoji) == "<:geoffory:894246779661484072>":
                await payload.member.add_roles(role)


@client.event
async def on_raw_reaction_remove(payload):
    msgID = channel_id_message_role_1
    guild = client.get_guild(payload.guild_id)
    role = discord.utils.get(guild.roles, name='test_role_1')
    if payload is not None:
        if payload.message_id == msgID:
            if str(payload.emoji) == "<:geoffory:894246779661484072>":
                await payload.member.remove_roles(role)

"""

"""
@client.event
async def on_reaction_add(reaction, user):
    channel = client.get_channel(channel_id_message_channel_1)
    await channel.send('{},{}'.format(reaction.message.id,reaction.emoji))

    if reaction.message.id == channel_id_message_role_1:
        if reaction.emoji == "<:geoffory:894246779661484072>":
            role = discord.utils.get(user.server.roles, name="test_role_1")
            await client.add_roles(user, role)

@client.event
async def on_reaction_remove(reaction, user):
    if reaction.message.id == channel_id_message_role_1:
        if reaction.emoji == "<:geoffory:894246779661484072>":
            role = discord.utils.get(user.server.roles, name="test_role_1")
            await client.remove_roles(user, role)
"""

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