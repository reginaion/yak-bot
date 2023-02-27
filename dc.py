
import discord
import asyncio
import datetime
import pytz
import os
from discord.ext import commands
from discord.ext import tasks
import discord_slash


intents = discord.Intents.all()
intents.members = True
intents.reactions = True
client = commands.Bot(command_prefix=';', intents=intents)
slash = discord_slash.SlashCommand(client, sync_commands=True)

alarm_time = '23:03'#24hrs
channel_id = 387998196422672386
channel_id_2 = 925717531082235935
channel_id_test = 925763452281159680
#invite_guild_id = 702741572344610907
#invite_channel_id = 702741572344610910
#channel_id_message_channel_1 = 925763452281159680
#channel_id_message_role_1 = 925783864092270672
invite_guild_id = 925717530545377331
invite_channel_id = 925725103801630761
channel_id_message_channel_1 = 925732268197167125
channel_id_message_role_1 = 925960555943051284
channel_id_message_role_2 = 926769088980738108
channel_message_backup_delete = 1074333559596273715
channel_message_backup_edit   = 1077264038888734810
channel_message_backup_delete_simp = 1077265391031685301
channel_message_backup_edit_simp   = 1077288231613247529
invide_mode = 2
guest_role_id = 1079793661304393800
test_channel_id = 925745745410269224

role_id = ["探險隊隊長","KemoV粉絲","禁區許可證","客家道場","王國旅人","Friends"]
role_emoji = ["<:geofforyA:925962558349934593>","<:dholeA:925962613718929490>","🔞","🔔","👑","<:suzakureservedenthusiasm:1061192355107053588>"]
role_color_id = ["難聽鳥紅","鴕鳥橘","藪ㄇ黃","嘶嘶綠","海豚藍","呼嚕嚕紫"]
role_color_emoji = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣"]

guild_ids = [702741572344610907]


@client.event
async def on_member_join(member):
    if (member.guild.id == invite_guild_id) and (invide_mode == 1):
        #guild = client.get_guild(invite_guild_id)
        #role = discord.utils.get(guild.roles, name="遊客")
        #await member.add_roles(role)

        channel = client.get_channel(invite_channel_id)
        #await member.send('Private message')
        embed=discord.Embed(title=f"ようこそジャパリパークへ! {member.name}", description=f"感謝您加入 {member.guild.name}!\n請至<#925779385729032262>閱讀守則\n請至<#925732268197167125>釘選處索取身分組以取得頻道瀏覽權限") # F-Strings!
        embed.set_thumbnail(url=member.avatar_url) # Set the embed's thumbnail to the member's avatar image!
        message="歡迎大大的加入，群組介面操作上有任何疑難雜症都可以詢問~\n\
閒聊總大廳在這裡︰<#925717531082235935>\n\
kemov聊天大廳在這裡︰<#925722682178293782>\n\
王國聊天大廳在這裡︰<#981035850429251594>\n\
群組上或操作上等有任何問題歡迎提出，或是至 <#1042429222154678312> 反應\n\
再次感謝大大的加入~"
        await channel.send(content=message,embed=embed)
    elif (member.guild.id == invite_guild_id) and (invide_mode == 2):
        #guild = client.get_guild(invite_guild_id)
        #role = discord.utils.get(guild.roles, name="遊客")
        #await member.add_roles(role)

        channel = client.get_channel(test_channel_id)
        #await member.send('Private message')
        embed=discord.Embed(title=f"ようこそジャパリパークへ! {member.name}", description=f"感謝您加入 {member.guild.name}!\n請至<#925779385729032262>閱讀守則\n請至<#925732268197167125>釘選處索取身分組以取得頻道瀏覽權限") # F-Strings!
        embed.set_thumbnail(url=member.avatar_url) # Set the embed's thumbnail to the member's avatar image!
        message="歡迎浮蓮子的加入~\n\
你現在看不到所有的頻道。待人工審核過後STAFF會給你瀏覽權限\n\
請抽時間讀 <#925779385729032262> 跟填寫入園申請~\n\
https://forms.gle/gxhFzuYCEemtfaWC7\n\n\
閒聊總大廳在這裡︰<#925717531082235935>\n\
kemov聊天大廳在這裡︰<#925722682178293782>\n\
王國聊天大廳在這裡︰<#981035850429251594>\n\
群組上或操作上等有任何問題歡迎提出，或是至 <#1079797068043923488> 反應\n\
再次感謝大大的加入~"
        await channel.send(content=message,embed=embed)
        await member.send(content=message,embed=embed)
        guest_role = member.guild.get_role(guest_role_id)
        await member.add_roles(guest_role)


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
async def delete_s(ctx, channel_id_s:int, message_id_s:int):
    #channel = client.get_channel(channel_id)
    channel = client.get_channel(channel_id_s)
    msg = await channel.fetch_message(message_id_s)
    await msg.delete()

@client.command()
@commands.is_owner()
async def edit_invite(ctx):
    embedvar = discord.Embed(title="請選取身分組!",
                              description="Click the corresponding emoji to receive your role.\n\
                                          {} - {}\n\
                                          {} - {}\n\
                                          {} - {}\n\
                                          {} - {}\n\
                                          {} - {}\n\
                                          {} - {}".format(role_emoji[0],"<@&925727966137290774>",
                                                          role_emoji[1],"<@&925729158577930310>",
                                                          role_emoji[4],"<@&1042010855396622407>",
                                                          role_emoji[5],"<@&1061155255880007771>",
                                                          role_emoji[2],"<@&925895939628105778>",
                                                          role_emoji[3],"<@&929747501727244368>"), color=0x00ff00)
    channel = client.get_channel(channel_id_message_channel_1)
    msg = await channel.fetch_message(channel_id_message_role_1)
    await msg.edit(content="頻道群組︰\n\
<#926715406683615294> - 閒聊\n\
<#925733227841343508> - けもフレ3\n\
<#925722952568279091> - けもV\n\
<#1042336425808511016> - けものフレンズキングダム\n\
　\n\
身分組︰\n\
<@&925727966137290774> - 動物朋友3玩家 (kemono friends 3 player)\n\
<@&925729158577930310> - 動物朋友V粉絲 (kemov fans)\n\
<@&1042010855396622407> - 動物朋友王國玩家 (kemono friends kingdom player)\n\
<@&1061155255880007771> - 動物朋友粉絲 (kemono fans)\n\
<@&925895939628105778> - R18頻道 (access r18 channel)\n\
<@&929747501727244368> - 客家道場提醒\n\
",embed=embedvar)
    await msg.add_reaction(role_emoji[0])
    await msg.add_reaction(role_emoji[1])
    await msg.add_reaction(role_emoji[2])
    await msg.add_reaction(role_emoji[3])
    await msg.add_reaction(role_emoji[4])
    await msg.add_reaction(role_emoji[5])
    #user = client.get_user(853662081991311371)
    #await msg.remove_reaction(role_emoji[5],user)

@client.command()
@commands.is_owner()
async def edit_color(ctx):
    embedvar = discord.Embed(title="請選取顏色身分組!",
                              description="Click the corresponding emoji to receive your role.\n\
                                          {} - {}\n\
                                          {} - {}\n\
                                          {} - {}\n\
                                          {} - {}\n\
                                          {} - {}\n\
                                          {} - {}".format(role_color_emoji[0],"<@&926766604602200074>",
                                                          role_color_emoji[1],"<@&926765413856067595>",
                                                          role_color_emoji[2],"<@&926767008891162674>",
                                                          role_color_emoji[3],"<@&926767203695611914>",
                                                          role_color_emoji[4],"<@&926767499914117131>",
                                                          role_color_emoji[5],"<@&926767717011316746>"), color=0x00ff00)
    channel = client.get_channel(channel_id_message_channel_1)
    msg = await channel.fetch_message(channel_id_message_role_2)
    await msg.edit(embed=embedvar)
    await msg.add_reaction(role_color_emoji[0])
    await msg.add_reaction(role_color_emoji[1])
    await msg.add_reaction(role_color_emoji[2])
    await msg.add_reaction(role_color_emoji[3])
    await msg.add_reaction(role_color_emoji[4])
    await msg.add_reaction(role_color_emoji[5])

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
        elif str(payload.emoji) == role_emoji[3]:
            role = discord.utils.get(guild.roles, name=role_id[3])
        elif str(payload.emoji) == role_emoji[4]:
            role = discord.utils.get(guild.roles, name=role_id[4])
        elif str(payload.emoji) == role_emoji[5]:
            role = discord.utils.get(guild.roles, name=role_id[5])

        if role is not None:
            await payload.member.add_roles(role)

    if payload.message_id == channel_id_message_role_2:
        if str(payload.emoji) == role_color_emoji[0]:
            role = discord.utils.get(guild.roles, name=role_color_id[0])
        elif str(payload.emoji) == role_color_emoji[1]:
            role = discord.utils.get(guild.roles, name=role_color_id[1])
        elif str(payload.emoji) == role_color_emoji[2]:
            role = discord.utils.get(guild.roles, name=role_color_id[2])
        elif str(payload.emoji) == role_color_emoji[3]:
            role = discord.utils.get(guild.roles, name=role_color_id[3])
        elif str(payload.emoji) == role_color_emoji[4]:
            role = discord.utils.get(guild.roles, name=role_color_id[4])
        elif str(payload.emoji) == role_color_emoji[5]:
            role = discord.utils.get(guild.roles, name=role_color_id[5])

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
        elif str(payload.emoji) == role_emoji[3]:
            role = discord.utils.get(guild.roles, name=role_id[3])
        elif str(payload.emoji) == role_emoji[4]:
            role = discord.utils.get(guild.roles, name=role_id[4])
        elif str(payload.emoji) == role_emoji[5]:
            role = discord.utils.get(guild.roles, name=role_id[5])

        if role is not None:
            await member.remove_roles(role)

    if payload.message_id == channel_id_message_role_2:
        if str(payload.emoji) == role_color_emoji[0]:
            role = discord.utils.get(guild.roles, name=role_color_id[0])
        elif str(payload.emoji) == role_color_emoji[1]:
            role = discord.utils.get(guild.roles, name=role_color_id[1])
        elif str(payload.emoji) == role_color_emoji[2]:
            role = discord.utils.get(guild.roles, name=role_color_id[2])
        elif str(payload.emoji) == role_color_emoji[3]:
            role = discord.utils.get(guild.roles, name=role_color_id[3])
        elif str(payload.emoji) == role_color_emoji[4]:
            role = discord.utils.get(guild.roles, name=role_color_id[4])
        elif str(payload.emoji) == role_color_emoji[5]:
            role = discord.utils.get(guild.roles, name=role_color_id[5])

        if role is not None:
            await member.remove_roles(role)

@slash.slash(name="test", description="Those burgers look tasty",        # Adding a new slash command with our slash variable
             options=[discord_slash.manage_commands.create_option(name="first_option", description="Please enter what you want on your burger", option_type=3, required=False)])
async def test(ctx: discord_slash.SlashContext, first_option):               # You have to name the function the 
    await ctx.send(f'I am now gonna get you a burger with {first_option}')   # same as the command

@client.command(name="ping") # Test command which works
async def ping(ctx):
    await ctx.send("ping")

@client.command(name="check_version") # Test command which works
async def check_version(ctx):
    await ctx.send("ver 0.0.9.8, date 230228, edit invite message")

@client.event
async def on_message_delete(message):
    channel = client.get_channel(channel_message_backup_delete)
    mca = message.created_at.astimezone(pytz.timezone('Asia/Taipei'))
    mea = 0
    mea_msg = ""
    mea_prx = ""
    mea_msg_simp = ""
    try:
        mea = message.edited_at.astimezone(pytz.timezone('Asia/Taipei'))
        mea_msg = f', E: {mea:%Y-%m-%d %H:%M:%S.%f %p}'
        mea_prx = "->E"
        mea_msg_simp = f' -> ({mea:%H:%M})'
    except:
        pass
    period = datetime.datetime.now(tz=pytz.timezone('Asia/Taipei')) - mca
    channel_simp = client.get_channel(channel_message_backup_delete_simp)
    await channel_simp.send(f'[Del] <#{message.channel.id}> <{message.channel}> --- {message.author}: {message.content} (P: {period.total_seconds():.2f}s) (C{mea_prx}: ({mca:%H:%M}){mea_msg_simp})')
    await channel.send(f'[Del] <#{message.channel.id}> <{message.channel}> --- {message.author}: {message.content} (P: {period.total_seconds():.2f}s) (C: {mca:%Y-%m-%d %H:%M:%S.%f %p}{mea_msg})')

@client.event
async def on_message_edit(message_before, message_after):
    channel = client.get_channel(channel_message_backup_edit)
    mcab = message_before.created_at.astimezone(pytz.timezone('Asia/Taipei'))
    mcaa = message_after.edited_at.astimezone(pytz.timezone('Asia/Taipei'))
    period = mcaa - mcab
    channel_simp = client.get_channel(channel_message_backup_edit_simp)
    await channel_simp.send(f'=================================================\n\
[Ed][Be] <#{message_before.channel.id}> <{message_before.channel}> --- {message_before.author}: {message_before.content}\n\
[Ed][Af] <#{message_after.channel.id}> <{message_after.channel}> --- {message_after.author}: {message_after.content} (P: {period.total_seconds():.2f}s) (C->E: ({mcab:%H:%M}) -> ({mcaa:%H:%M}))')
    await channel.send(f'=================================================\n\
[Ed][Be] <#{message_before.channel.id}> <{message_before.channel}> --- {message_before.author}: {message_before.content} (C: {mcab:%Y-%m-%d %H:%M:%S.%f %p})\n\
[Ed][Af] <#{message_after.channel.id}> <{message_after.channel}> --- {message_after.author}: {message_after.content} (P: {period.total_seconds():.2f}s) (C: {mcaa:%Y-%m-%d %H:%M:%S.%f %p})')

#@client.slash_command(guild_ids=[702741572344610907])
#async def hello(ctx):
#    await ctx.respond(f"Hello {ctx.author}!")

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
        channel = client.get_channel(channel_id_2)
        await channel.send('<@&929747501727244368>```客家道場```')
    if weekday == 6 and cst.hour == 22 and cst.minute == 31:
        await client.wait_until_ready()
        channel = client.get_channel(channel_id)
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