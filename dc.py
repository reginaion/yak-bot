
import discord
import asyncio
import datetime
import pytz
import os
from discord.ext import commands
from discord.ext import tasks
# import discord_slash


intents = discord.Intents.all()
intents.members = True
intents.reactions = True
client = commands.Bot(command_prefix=';', intents=intents)
# slash = discord_slash.SlashCommand(client, sync_commands=True)

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
no_welcome_msg_role_id = 1080847909513330759
test_channel_id = 925745745410269224
help_channel_id = 1079797068043923488

role_nid = ["探險隊隊長","KemoV粉絲","禁區許可證","客家道場","王國旅人","Friends"]
role_emoji = ["<:geofforyA:925962558349934593>","<:dholeA:925962613718929490>","🔞","🔔","👑","<:suzakureservedenthusiasm:1061192355107053588>"]
role_color_nid = ["難聽鳥紅","鴕鳥橘","藪ㄇ黃","嘶嘶綠","海豚藍","呼嚕嚕紫"]
role_id = [925727966137290774,925729158577930310,925895939628105778,929747501727244368,1042010855396622407,1061155255880007771]
role_color_id = [926766604602200074,926765413856067595,926767008891162674,926767203695611914,926767499914117131,926767717011316746,\
1080844701306986556,1080859136465584210,1080845993169399910,1080857106019799080,1080852277117591552,1080852769646325820,\
1080853366843899925,1080856574135910480,1080857411130232864,1080858479494959184,1080858658344288348]
role_color_emoji = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","<:cape_confuse:926401561125601310>","<:hululu_happy:926399458764263494>","<:shimahai_hai:926405048706166784>","<:coyote_sleepy:926397039393263636>",\
"<:dire_3:1080865933591052388>","<:caracal_3:1080862045563523134>","<:geoffory_worry:1080862839079706716>","<:genet_XD:1080865745195503667>","<:shimarisu_happy:1080863928160100403>",\
"<:junglecat_x:1080865791550963752>","<:usako_3:1080863905858986154>"]
guild_ids = [702741572344610907]



class server_item:
    def __init__(self):
        self.bot_id = os.getenv('BOT_ID')
        self.invite_guild_id = 0
        self.channel_id = {'help':0,
                           'suggestion':0,
                           'invite':0,
                           'rule':0,
                           'select_role':0,
                           'join_leave':0,
                           'verify_phone':0,       # Update at 230808
                           'recorder_msg_edit':0,  # Update at 240316
                           'recorder_msg_del':0,   # Update at 240316
                           'main_chat_list':[]}
        self.message_id = {'role_main':0,
                           'role_color':0,
                           'role_verify_phone':0,
                           'role_icon':0}         # Update at 240512
        self.message_id_enable = {'role_icon':0}  # Update at 240512
        self.main_chat_channel_list = []
        self.guest_role_id = 0
        self.no_welcome_msg_role_id = 0
        self.role_id = []
        self.role_emoji = []
        self.role_color_id = []
        self.role_color_emoji = []
        self.role_icon_id = []
        self.role_icon_emoji = []
        self.verify_phone_emoji = []
        self.emoji_jp = "<:japanflagemojiclipartmd:1147906462560043118>"
        self.emoji_cn = "<:GS100000:824600807340638268>"
        self.jp_info = "※日本語は {} の絵文字でリアクション"
        self.jp_info = self.jp_info.format(self.emoji_jp)
        self.cn_info = "※請點選 {} 切換中文"
        self.cn_info = self.cn_info.format(self.emoji_cn)
        self.message_on_member_join = "歡迎浮蓮子的加入~\n\
你現在看不到所有的頻道\n\
請先閱讀版規及填寫下方連結問卷，問卷提交後待STAFF審核，通過後我們會給你 <#{}> 選擇權限\n\n\
重要!!\n\
**請先填寫【入園申請】跟【閱讀 <#{}> 】~**\n\
➡️入園申請(中　文)︰ <https://forms.gle/JVxeWbQ2E4wkb3Ee6> ⬅️\n\
➡️入園申請(日本語)︰ <https://forms.gle/66dvtVJQCZZP41bS8> ⬅️\n\
➡️Application form(EN)︰ <https://forms.gle/XcR1RgJvHbWcyAxB8> ⬅️\n\
\n\
➡️如果需要幫助的話，請至 <#{}> 反應~⬅️\n\
再次感謝大大的加入~"
        self.jp_message_on_member_join = "ようこそサーバーへ\n\
あなたは今、見られるチャンネルを制限されている筈よ\n\
先に規約を読んで、下のリンクの質問票（問卷）に記入して提出後、スタッフ審査で許可が出たら、あなたに <#{}> での選択権限を渡すわ\n\
重要!!\n\
**初めに【入園申請】の記入と【 <#{}> の熟読】はお願いするわ**\n\
➡️中国語入園申請︰ <https://forms.gle/JVxeWbQ2E4wkb3Ee6> ⬅️\n\
➡️日本語入園申請︰ <https://forms.gle/66dvtVJQCZZP41bS8> ⬅️\n\
➡️Application form(EN)︰ <https://forms.gle/XcR1RgJvHbWcyAxB8> ⬅️\n\
\n\
➡️もし困ったことがあれば、 <#{}> でメッセージを送って ⬅️\n\
改めて入ってきてくれて本当にありがとう"

        self.message_verify_phone = "感謝{}的加入，請先至 <#{}> 進行手機驗證\n{}、加入してくれてありがとう\n最初に <#{}> で携帯認証をしてきて"
        self.message_on_member_update = "感謝浮蓮子的加入，群組介面操作上有任何疑難雜症都可以詢問~\n\n\
可以在 <#{}> 領取你喜歡的【身份組】及【個性化名字染色】喔~\n\
\n\
閒聊總大廳在這裡︰<#{}>\n\
kemov聊天大廳在這裡︰<#{}>\n\
王國聊天大廳在這裡︰<#{}>\n\
群組上或操作上等有任何問題歡迎提出，或是至 <#{}> 反應\n\
再次感謝大大的加入~"
        self.jp_message_on_member_update = "加入してくれてありがとう\n\
このサーバーの使い方で困ったことがあれば何でも質問するといいわ\n\
 <#{}> であなたの好きな【ロール】と【ユーザー名の色変更】を選びましょう\n\
\n\
総合雑談部屋はこっち︰<#{}>\n\
けもVチャット部屋はこっち︰<#{}>\n\
キングダムチャット部屋はこっち︰<#{}>\n\
グループや使い方等のことについては気軽に <#{}> で質問を送ってくれてもいいわ\n\
改めて入ってきてくれて本当にありがとう"
        self.embed_on_member_update = "感謝您加入 {}!\n請至<#{}>閱讀守則\n請至<#{}>釘選處索取身分組以取得頻道瀏覽權限"
        self.embed_edit_invite = "Click the corresponding emoji to receive your role (select at least one).\n\
                                          {} - <@&{}>\n\
                                          {} - <@&{}>\n\
                                          {} - <@&{}>\n\
                                          {} - <@&{}>\n\n\
Click the corresponding emoji to receive your role.\n\
                                          {} - <@&{}>\n\
                                          {} - <@&{}>\n\
                                          {} - <@&{}>\n\
                                          {} - <@&{}>\n\
                                          {} - <@&{}>\n\
                                          {} - <@&{}>\n\
                                          {} - <@&{}>\n\
                                          {} - <@&{}>\n\
                                          {} - <@&{}>"
        self.message_edit_invite = "頻道群組︰\n\
<#{}> - 閒聊\n\
<#{}> - けもフレ3\n\
<#{}> - けもV\n\
<#{}> - けものフレンズキングダム\n\
　\n\
➡️權限功能身分組(至少領取以下四個其中之一身份組)⬅️\n\
<@&{}> - 動物朋友3玩家 (Kemono friends 3 player)\n\
<@&{}> - 動物朋友V粉絲 (Kemov fans)\n\
<@&{}> - 動物朋友王國玩家 (Kemono friends kingdom player)\n\
<@&{}> - 動物朋友粉絲 (Kemono fans)\n\
　\n\
額外功能身份組\n\
<@&{}> - R18頻道 (Access r18 channel)\n\
<@&{}> - R18G頻道 (Access r18g channel)\n\
<@&{}> - 活動通知提醒 (Send event notifications to you)\n\
<@&{}> - 日版客家道場提醒 (For KF3 (JP) only, reminded every Sunday at 22:30 (UTC+8))\n\
<@&{}> - 繁中版客家道場提醒 (For KF3 (ZH) only, reminded every Sunday at 23:30 (UTC+8))\n\
<@&{}> - Japanese friends\n\
<@&{}> - English friends\n\
<@&{}> - Creator\n\
<@&{}> - Coser\n\
"
        self.message_edit_verify_phone_content = "請點 {} 進行手機驗證\n最初に {} をタップして携帯認証をしてきて\n"
        self.message_edit_color = "這是看起來很棒的顏色身分組，可以為你的名字染色。歡迎領取 (無額外權限功能)\n"
        self.embed_edit_color = "Click the corresponding emoji to receive your role.\n\
                                          {} - <@&{}>\n\
                                          {} - <@&{}>\n\
                                          {} - <@&{}>\n\
                                          {} - <@&{}>\n\
                                          {} - <@&{}>\n\
                                          {} - <@&{}>\n\
                                          {} - <@&{}>\n\
                                          {} - <@&{}>\n\
                                          {} - <@&{}>\n\
                                          {} - <@&{}>\n\
                                          {} - <@&{}>\n\
                                          {} - <@&{}>\n\
                                          {} - <@&{}>\n\
                                          {} - <@&{}>\n\
                                          {} - <@&{}>\n\
                                          {} - <@&{}>\n\
                                          {} - <@&{}>"

        self.message_edit_icon = "圖標身分組。歡迎領取 (無額外權限功能)\nRole of icon, welcome to receive (No specfic permission)\n"
        self.embed_edit_icon = "\
Kemo3\n\
{} - <@&{}>\n\
{} - <@&{}>\n\
{} - <@&{}>\n\
{} - <@&{}>\n\
KemoV\n\
{} - <@&{}>\n\
{} - <@&{}>\n\
{} - <@&{}>\n\
Kingdom\n\
{} - <@&{}>\n\
Friends\n\
{} - <@&{}>\n"
        
    def set_on_member_join(self):
        self.message_on_member_join = self.message_on_member_join.format(self.channel_id['select_role'],
                                                                         self.channel_id['rule'],
                                                                         self.channel_id['help'])
        self.jp_message_on_member_join = self.jp_message_on_member_join.format(self.channel_id['select_role'],
                                                                               self.channel_id['rule'],
                                                                               self.channel_id['help'])
    def set_message_verify_phone(self):
        self.message_verify_phone = self.message_verify_phone.format('{}',self.channel_id['verify_phone'],'{}',self.channel_id['verify_phone'])

    def set_on_member_update(self):
        self.message_on_member_update = self.message_on_member_update.format(self.channel_id['select_role'],
                                                                             self.channel_id['main_chat_list'][0],
                                                                             self.channel_id['main_chat_list'][1],
                                                                             self.channel_id['main_chat_list'][2],
                                                                             self.channel_id['suggestion'])
        self.jp_message_on_member_update = self.jp_message_on_member_update.format(self.channel_id['select_role'],
                                                                                   self.channel_id['main_chat_list'][0],
                                                                                   self.channel_id['main_chat_list'][1],
                                                                                   self.channel_id['main_chat_list'][2],
                                                                                   self.channel_id['suggestion'])
        self.embed_on_member_update = self.embed_on_member_update.format('{}',
                                                                         self.channel_id['rule'],
                                                                         self.channel_id['select_role'])
        
        
    def set_edit_invite(self):
        self.embed_edit_invite = self.embed_edit_invite.format(self.role_emoji[0],self.role_id[0],
                                                               self.role_emoji[1],self.role_id[1],
                                                               self.role_emoji[4],self.role_id[4],
                                                               self.role_emoji[5],self.role_id[5],
                                                               self.role_emoji[2],self.role_id[2],
                                                               self.role_emoji[12],self.role_id[12],
                                                               self.role_emoji[6],self.role_id[6],
                                                               self.role_emoji[3],self.role_id[3],
                                                               self.role_emoji[7],self.role_id[7],
                                                               self.role_emoji[8],self.role_id[8],
                                                               self.role_emoji[9],self.role_id[9],
                                                               self.role_emoji[10],self.role_id[10],
                                                               self.role_emoji[11],self.role_id[11])
        
        self.message_edit_invite = self.message_edit_invite.format("{}","{}","{}","{}",self.role_id[0],
                                                                                       self.role_id[1],
                                                                                       self.role_id[4],
                                                                                       self.role_id[5],
                                                                                       self.role_id[2],
                                                                                       self.role_id[6],
                                                                                       self.role_id[3],
                                                                                       self.role_id[7],
                                                                                       self.role_id[8],
                                                                                       self.role_id[9],
                                                                                       self.role_id[10],
                                                                                       self.role_id[11],
                                                                                       self.role_id[12])
    
    def set_edit_color(self):
        self.embed_edit_color = self.embed_edit_color.format(self.role_color_emoji[0],self.role_color_id[0],
                                                             self.role_color_emoji[1],self.role_color_id[1],
                                                             self.role_color_emoji[2],self.role_color_id[2],
                                                             self.role_color_emoji[3],self.role_color_id[3],
                                                             self.role_color_emoji[4],self.role_color_id[4],
                                                             self.role_color_emoji[5],self.role_color_id[5],
                                                             self.role_color_emoji[6],self.role_color_id[6],
                                                             self.role_color_emoji[7],self.role_color_id[7],
                                                             self.role_color_emoji[8],self.role_color_id[8],
                                                             self.role_color_emoji[9],self.role_color_id[9],
                                                             self.role_color_emoji[10],self.role_color_id[10],
                                                             self.role_color_emoji[11],self.role_color_id[11],
                                                             self.role_color_emoji[12],self.role_color_id[12],
                                                             self.role_color_emoji[13],self.role_color_id[13],
                                                             self.role_color_emoji[14],self.role_color_id[14],
                                                             self.role_color_emoji[15],self.role_color_id[15],
                                                             self.role_color_emoji[16],self.role_color_id[16])

    def set_edit_icon(self):
        if self.message_id_enable['role_icon'] == 0:
            return
        self.embed_edit_icon = self.embed_edit_icon.format(self.role_icon_emoji[0],self.role_icon_id[0],
                                                           self.role_icon_emoji[1],self.role_icon_id[1],
                                                           self.role_icon_emoji[2],self.role_icon_id[2],
                                                           self.role_icon_emoji[3],self.role_icon_id[3],
                                                           self.role_icon_emoji[4],self.role_icon_id[4],
                                                           self.role_icon_emoji[5],self.role_icon_id[5],
                                                           self.role_icon_emoji[6],self.role_icon_id[6],
                                                           self.role_icon_emoji[7],self.role_icon_id[7],
                                                           self.role_icon_emoji[8],self.role_icon_id[8])

    def set_message_edit_verify_phone_content(self):
        self.message_edit_verify_phone_content = self.message_edit_verify_phone_content.format(self.verify_phone_emoji[0],self.verify_phone_emoji[0])

test_guild = 1085468421870845952

s1 = server_item()
s1.invite_guild_id = 925717530545377331
s1.channel_id['help'] = 1079797068043923488
s1.channel_id['suggestion'] = 1042429222154678312
s1.channel_id['invite'] = 925725103801630761
s1.channel_id['rule'] = 925779385729032262
s1.channel_id['select_role'] = 925732268197167125
s1.channel_id['join_leave'] = 925745745410269224
s1.channel_id['verify_phone'] = 1138494443746504724 # 230808
s1.channel_id['recorder_msg_edit'] = 1218454206126489600 # 240316
s1.channel_id['recorder_msg_del'] = 1218454250363949138 # 240316
s1.channel_id['main_chat_list'] = [925717531082235935,925722682178293782,981035850429251594]
s1.message_id['role_main'] = 925960555943051284
s1.message_id['role_color'] = 926769088980738108
s1.message_id['role_verify_phone'] = 1138494764694638613 # 230808
s1.message_id['role_icon'] = 1239097361628926044 # 240512
s1.message_id_enable['role_icon'] = 1 # 240512

s1.guest_role_id = 1079793661304393800
s1.no_welcome_msg_role_id = 1080847909513330759
s1.role_id = [925727966137290774,925729158577930310,925895939628105778,929747501727244368,1042010855396622407,1061155255880007771,1023127510801715201,1095689201757995069,
1097790288904343635,1097790097916690433,1097791345709563947,1180406024126074972,1262272402734448710]
s1.role_emoji = ["<:geofforyA:925962558349934593>","<:dholeA:925962613718929490>","🔞","🔔","👑","<:suzakureservedenthusiasm:1061192355107053588>","<:EzoSmug:788033424928669736>","🔊",
"🌸","🆒","🎨","<:aquagf:706822828900483093>","🇬"]
s1.role_color_id = [926766604602200074,926765413856067595,926767008891162674,926767203695611914,926767499914117131,926767717011316746,\
1080844701306986556,1080859136465584210,1080845993169399910,1080857106019799080,1080852277117591552,1080852769646325820,\
1080853366843899925,1080856574135910480,1080857411130232864,1080858479494959184,1080858658344288348]
s1.role_color_emoji = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","<:cape_confuse:926401561125601310>","<:hululu_happy:926399458764263494>","<:shimahai_hai:926405048706166784>","<:coyote_sleepy:926397039393263636>",\
"<:dire_3:1080865933591052388>","<:caracal_3:1080862045563523134>","<:geoffory_worry:1080862839079706716>","<:genet_XD:1080865745195503667>","<:shimarisu_happy:1080863928160100403>",\
"<:junglecat_x:1080865791550963752>","<:usako_3:1080863905858986154>"]

# line 1: kemo3
# line 2: kemoV
# line 3: kingdom
# line 4: friends
s1.role_icon_id = [1238790596072701972,1238878017619497053,1238886890548105268,1239027403280617545,
1238784494903889992,1239027840184356885,1239088337776803870,
1239087973757358131,
1239088455263457370]
s1.role_icon_emoji = ['<:hana_maru:1239098685720236053>','<:japari_dan:1239088908755533824>','<:Picnic240:1239089096954089523>','<:kirakira:1239089673507438705>',
'<:kemov_logo:1239089128511901736>','<:kani_hai:1239089219821899806>','<:shimahai_Pantsu:1239089588216139796>',
'<:paperairplane:1239088780217024522>',
'<:kemono_logo:1239088704996376636>']

s1.verify_phone_emoji = ["📱"] # 230808
s1.set_on_member_join()
s1.set_message_verify_phone() # 230808
s1.set_on_member_update()
s1.set_edit_invite()
s1.set_edit_color()
s1.set_edit_icon() # 240512
s1.set_message_edit_verify_phone_content() # 230808
#s1.embed_on_member_update = s1.embed_on_member_update.format(">2351<")
s1.message_edit_invite = s1.message_edit_invite.format("926715406683615294","925733227841343508","925722952568279091","1042336425808511016")

s2 = server_item()
s2.invite_guild_id = 1085468421870845952
s2.channel_id['help'] = 1085468422474829829
s2.channel_id['suggestion'] = 1085468422743277599
s2.channel_id['invite'] = 1085468422474829828
s2.channel_id['rule']  = 1085468422474829827
s2.channel_id['select_role'] = 1085468422474829830
s2.channel_id['join_leave'] = 1085468422743277601
s2.channel_id['verify_phone'] = 1138450597104853062 # 230808
s2.channel_id['main_chat_list'] = [1085468422743277603,1085468422743277604,1085468423812825159]
s2.message_id['role_main'] = 1085495104762032178
s2.message_id['role_color'] = 1085495131081289738
s2.message_id['role_verify_phone'] = 1138451434304720968 # 230808
s2.guest_role_id = 1085468421870845954
s2.no_welcome_msg_role_id = 1085468421870845953
s2.role_id = [1085468421891821610,1085468421870845961,1085468421870845957,1085468421870845956,1085468421891821609,1085468421891821608,1090978081033965629,1095718252631572563,
1099295924716589146,1099295976289751191,1099296010787901491,1085468421891821610,1085468421891821610]
s2.role_emoji = ["<:geoffory_A:925962558349934593>","<:dhole_A:925962613718929490>","🔞","🔔","👑","<:suzakureservedenthusiasm:1061192355107053588>","<:EzoSmug:788033424928669736>","🔊",
"🌸","🆒","🎨","<:aquagf:706822828900483093>","🇬"]
s2.role_color_id = [1085468421912805385,1085468421912805384,1085468421912805383,1085468421912805382,1085468421912805381,1085468421912805380,\
1085468421912805379,1085468421912805378,1085468421912805377,1085468421912805376,1085468421891821617,1085468421891821616,\
1085468421891821615,1085468421891821614,1085468421891821613,1085468421891821612,1085468421891821611]
s2.role_color_emoji = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","<:cape_confuse:926401561125601310>","<:hululu_happy:926399458764263494>","<:shimahai_hai:926405048706166784>","<:coyote_sleepy:926397039393263636>",\
"<:dire_3:1080865933591052388>","<:caracal_3:1080862045563523134>","<:geoffory_worry:1080862839079706716>","<:genet_XD:1080865745195503667>","<:shimarisu_happy:1080863928160100403>",\
"<:junglecat_x:1080865791550963752>","<:usako_3:1080863905858986154>"]
s2.verify_phone_emoji = ["📱"] # 230808
s2.set_on_member_join()
s2.set_message_verify_phone() # 230808
s2.set_on_member_update()
s2.set_edit_invite()
s2.set_edit_color()
s2.set_message_edit_verify_phone_content() # 230808
#s2.embed_on_member_update = s2.embed_on_member_update.format(">2352<")
s2.message_edit_invite = s2.message_edit_invite.format("1085468422743277602","1085468423041056822","1085468424190296074","1085468423334662199")

s3 = server_item()
s3.invite_guild_id = 1237351637383774219
s3.channel_id['help'] = 1237351638151336037
s3.channel_id['suggestion'] = 1237351638520430670
s3.channel_id['invite'] = 1237351638520430665
s3.channel_id['rule']  = 1237351638520430663
s3.channel_id['select_role'] = 1237351638520430666
s3.channel_id['join_leave'] = 1237351638151336038
s3.channel_id['verify_phone'] = 1237351638151336042 # 230808
s3.channel_id['recorder_msg_edit'] = 1237351638151336043 # 240316
s3.channel_id['recorder_msg_del'] = 1237351638151336044 # 240316
s3.channel_id['main_chat_list'] = [1237351638856110081,1237351638856110084,1237351640085041172]
s3.message_id['role_main'] = 1237414705220423864
s3.message_id['role_color'] = 1237414711851745322
s3.message_id['role_verify_phone'] = 1237414891116298371 # 230808
s3.guest_role_id = 1237351637383774223
s3.no_welcome_msg_role_id = 1237351637383774222
s3.role_id = [1237351637568192567,1237351637530710135,1237351637530710131,1237351637383774226,1237351637530710137,1237351637530710136,1237351637383774224,1237351637383774225,
1237351637530710130,1237351637530710129,1237351637530710128,1237351637383774227,1237351637383774227]
s3.role_emoji = ["<:geoffory_A:925962558349934593>","<:dhole_A:925962613718929490>","🔞","🔔","👑","<:suzakureservedenthusiasm:1061192355107053588>","<:EzoSmug:788033424928669736>","🔊",
"🌸","🆒","🎨","<:aquagf:706822828900483093>","🇬"]
s3.role_color_id = [1237351637610266672,1237351637610266671,1237351637610266670,1237351637610266669,1237351637610266668,1237351637610266667,\
1237351637610266666,1237351637610266665,1237351637568192576,1237351637568192575,1237351637568192574,1237351637568192573,\
1237351637568192572,1237351637568192571,1237351637568192570,1237351637568192569,1237351637568192568]
s3.role_color_emoji = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","<:cape_confuse:926401561125601310>","<:hululu_happy:926399458764263494>","<:shimahai_hai:926405048706166784>","<:coyote_sleepy:926397039393263636>",\
"<:dire_3:1080865933591052388>","<:caracal_3:1080862045563523134>","<:geoffory_worry:1080862839079706716>","<:genet_XD:1080865745195503667>","<:shimarisu_happy:1080863928160100403>",\
"<:junglecat_x:1080865791550963752>","<:usako_3:1080863905858986154>"]
s3.verify_phone_emoji = ["📱"] # 230808
s3.set_on_member_join()
s3.set_message_verify_phone() # 230808
s3.set_on_member_update()
s3.set_edit_invite()
s3.set_edit_color()
s3.set_message_edit_verify_phone_content() # 230808
#s2.embed_on_member_update = s2.embed_on_member_update.format(">2352<")
s3.message_edit_invite = s3.message_edit_invite.format("1237351638856110080","1237351639220748309","1237351640575508484","1237351639623532551")




guild_list = {s1.invite_guild_id: s1, s2.invite_guild_id: s2, s3.invite_guild_id: s3}
channal_ignore_channal = [s1.channel_id['recorder_msg_edit'], s1.channel_id['recorder_msg_del'],
s3.channel_id['recorder_msg_edit'], s3.channel_id['recorder_msg_del']]


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
    elif (member.guild.id == invite_guild_id) and (invide_mode == 3):
        #guild = client.get_guild(invite_guild_id)
        #role = discord.utils.get(guild.roles, name="遊客")
        #await member.add_roles(role)

        #channel = client.get_channel(invite_channel_id)
        channel_2 = client.get_channel(help_channel_id)
        #await member.send('Private message')
        #embed=discord.Embed(title=f"ようこそジャパリパークへ! {member.name}", description=f"感謝您加入 {member.guild.name}!\n請至<#925779385729032262>閱讀守則\n請至<#925732268197167125>釘選處索取身分組以取得頻道瀏覽權限") # F-Strings!
        #embed.set_thumbnail(url=member.avatar_url) # Set the embed's thumbnail to the member's avatar image!
        mention_message = f'<@{member.id}>\n'
        message="歡迎浮蓮子的加入~\n\
你現在看不到所有的頻道\n\
請先閱讀版規及填寫下方連結問卷，問卷提交後待STAFF審核，通過後我們會給你 <#925732268197167125> 選擇權限\n\n\
重要!!\n\
**請先填寫【入園申請】跟【閱讀 <#925779385729032262> 】~**\n\
➡️入園申請︰ https://forms.gle/JVxeWbQ2E4wkb3Ee6 ⬅️\n\
\n\
➡️如果需要幫助的話，請至 <#1079797068043923488> 反應~⬅️\n\
再次感謝大大的加入~"
        guest_role = member.guild.get_role(guest_role_id)
        await member.add_roles(guest_role)
        await channel_2.send(content=(mention_message+message))#,embed=embed)
        #await channel.send(content=message,embed=embed)
        await member.send(content=message)#,embed=embed)
    elif (member.guild.id in guild_list) and (invide_mode == 4) and (member.guild.id == s1.invite_guild_id or member.guild.id == s3.invite_guild_id): # 230808
        svr             = guild_list[member.guild.id]
        channel         = client.get_channel(svr.channel_id['help'])
        mention_message = f'<@{member.id}>\n'
        message         = svr.message_on_member_join
        guest_role      = member.guild.get_role(svr.guest_role_id)
        await member.add_roles(guest_role)
        await channel.send(content=(mention_message+message))#,embed=embed)
        await member.send(content=message)#,embed=embed)

        channel_ji = client.get_channel(svr.channel_id['join_leave'])
        mja        = member.joined_at.astimezone(pytz.timezone('Asia/Taipei'))
        await channel_ji.send(f'[+][Jn] {member.guild.name} --- <@{member.id}> ({member}) (J: ({mja:%Y-%m-%d %H:%M:%S.%f %p}))')

    elif (member.guild.id in guild_list) and (invide_mode == 2):
        svr             = guild_list[member.guild.id]
        channel         = client.get_channel(svr.channel_id['help'])
        mention_message = f'<@{member.id}>'
        message         = svr.message_verify_phone
        message         = message.format(mention_message,mention_message)
        
        # await channel.send(content=(mention_message+message))#,embed=embed)
        await member.send(content=message)#,embed=embed)

        channel_ji = client.get_channel(svr.channel_id['join_leave'])
        mja        = member.joined_at.astimezone(pytz.timezone('Asia/Taipei'))
        await channel_ji.send(f'[+][Jn] {member.guild.name} --- <@{member.id}> ({member}) (J: ({mja:%Y-%m-%d %H:%M:%S.%f %p}))')

@client.event
async def on_member_remove(member):
    if (member.guild.id in guild_list) and (invide_mode == 2):
        svr        = guild_list[member.guild.id]
        channel_ji = client.get_channel(svr.channel_id['join_leave'])
        mja        = member.joined_at.astimezone(pytz.timezone('Asia/Taipei'))
        tn         = datetime.datetime.now(tz=pytz.timezone('Asia/Taipei'))
        period     = tn - mja
        nk_message = ""
        if member.nick:
            nk_message = f", nickname: {member.nick}"
        await channel_ji.send(f'[-][Lv] {member.guild.name} --- <@{member.id}> ({member}{nk_message}) (P: {period.total_seconds():.2f}s) (J->L: ({mja:%Y-%m-%d %H:%M:%S.%f %p}) -> ({tn:%Y-%m-%d %H:%M:%S.%f %p}))')

@client.event
async def on_member_update(before, after):
    if (after.guild.id == invite_guild_id) and (invide_mode == 3):
        if [i.id for i in before.roles].count(guest_role_id) == 1:
            if [i.id for i in after.roles].count(guest_role_id) == 0:
                channel = client.get_channel(invite_channel_id)
                embed=discord.Embed(title=f"ようこそジャパリパークへ! {after.name}", description=f"感謝您加入 {after.guild.name}!\n請至<#925779385729032262>閱讀守則\n請至<#925732268197167125>釘選處索取身分組以取得頻道瀏覽權限") # F-Strings!
                embed.set_thumbnail(url=after.avatar_url) # Set the embed's thumbnail to the member's avatar image!
                mention_message = f'<@{after.id}>\n'
                message="感謝浮蓮子的加入，群組介面操作上有任何疑難雜症都可以詢問~\n\n\
可以在 <#925732268197167125> 領取你喜歡的【身份組】及【個性化名字染色】喔~\n\
\n\
閒聊總大廳在這裡︰<#925717531082235935>\n\
kemov聊天大廳在這裡︰<#925722682178293782>\n\
王國聊天大廳在這裡︰<#981035850429251594>\n\
群組上或操作上等有任何問題歡迎提出，或是至 <#1042429222154678312> 反應\n\
再次感謝大大的加入~"
                if [i.id for i in after.roles].count(no_welcome_msg_role_id) == 0:
                    await channel.send(content=(mention_message+message),embed=embed)
                await after.send(content=message)

    elif (after.guild.id in guild_list) and (invide_mode == 2):
        svr = guild_list[after.guild.id]
        if [i.id for i in before.roles].count(svr.guest_role_id) == 1:
            if [i.id for i in after.roles].count(svr.guest_role_id) == 0:
                channel = client.get_channel(svr.channel_id['invite'])
                mention_message = f'<@{after.id}>\n'
                await channel.send(content=(mention_message))

                embed   = discord.Embed(title=f"ようこそジャパリパークへ! {after.name}", description=svr.embed_on_member_update.format(after.guild.name))
                embed.set_thumbnail(url=after.avatar_url) # Set the embed's thumbnail to the member's avatar image!
                message = svr.message_on_member_update
                if [i.id for i in after.roles].count(svr.no_welcome_msg_role_id) == 0:
                    msg_entry = await channel.send(content=(message+"\n\n"+svr.jp_info),embed=embed)
                    await msg_entry.add_reaction(svr.emoji_jp)
                await after.send(content=message)

                # friend_role = after.guild.get_role(svr.role_id[5]) # @friend role # 230808: phase out auto add role
                # await after.add_roles(friend_role)


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
    print('time_check.start()')
    time_check.start()
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
    if invide_mode == 2:
        return
    embedvar = discord.Embed(title="請選取身分組!",
                              description="Click the corresponding emoji to receive your role (select at least one).\n\
                                          {} - {}\n\
                                          {} - {}\n\
                                          {} - {}\n\
                                          {} - {}\n\n\
Click the corresponding emoji to receive your role.\n\
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
➡權限功能身分組(至少領取以下四個其中之一身份組)⬅️\n\
<@&925727966137290774> - 動物朋友3玩家 (Kemono friends 3 player)\n\
<@&925729158577930310> - 動物朋友V粉絲 (Kemov fans)\n\
<@&1042010855396622407> - 動物朋友王國玩家 (Kemono friends kingdom player)\n\
<@&1061155255880007771> - 動物朋友粉絲 (Kemono fans)\n\
　\n\
額外功能身份組\n\
<@&925895939628105778> - R18頻道 (Access r18 channel)\n\
<@&929747501727244368> - 客家道場提醒 (For KF3 only, reminded every Sunday at 22:30 (UTC+8))\n\
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
    if invide_mode == 2:
        return
    embedvar = discord.Embed(title="請選取顏色身分組!",
                              description="Click the corresponding emoji to receive your role.\n\
                                          {} - {}\n\
                                          {} - {}\n\
                                          {} - {}\n\
                                          {} - {}\n\
                                          {} - {}\n\
                                          {} - {}\n\
                                          {} - {}\n\
                                          {} - {}\n\
                                          {} - {}\n\
                                          {} - {}\n\
                                          {} - {}\n\
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
                                                          role_color_emoji[5],"<@&926767717011316746>",
                                                          role_color_emoji[6],"<@&1080844701306986556>",
                                                          role_color_emoji[7],"<@&1080859136465584210>",
                                                          role_color_emoji[8],"<@&1080845993169399910>",
                                                          role_color_emoji[9],"<@&1080857106019799080>",
                                                          role_color_emoji[10],"<@&1080852277117591552>",
                                                          role_color_emoji[11],"<@&1080852769646325820>",
                                                          role_color_emoji[12],"<@&1080853366843899925>",
                                                          role_color_emoji[13],"<@&1080856574135910480>",
                                                          role_color_emoji[14],"<@&1080857411130232864>",
                                                          role_color_emoji[15],"<@&1080858479494959184>",
                                                          role_color_emoji[16],"<@&1080858658344288348>"), color=0x00ff00)

    channel = client.get_channel(channel_id_message_channel_1)
    msg = await channel.fetch_message(channel_id_message_role_2)
    await msg.edit(content="這是看起來很棒的顏色身分組，可以為你的名字染色。歡迎領取 (無額外權限功能)\n",embed=embedvar)
    for i in range(len(role_color_emoji)):
        await msg.add_reaction(role_color_emoji[i])
#    await msg.add_reaction(role_color_emoji[0])
#    await msg.add_reaction(role_color_emoji[1])
#    await msg.add_reaction(role_color_emoji[2])
#    await msg.add_reaction(role_color_emoji[3])
#    await msg.add_reaction(role_color_emoji[4])
#    await msg.add_reaction(role_color_emoji[5])

@client.command()
@commands.is_owner()
async def edit_verify_phone_s(ctx, guild_id:int): # 230808
    if guild_id not in guild_list:
        return
    if invide_mode != 2:
        return
    
    svr = guild_list[guild_id]
    channel = client.get_channel(svr.channel_id['verify_phone'])
    msg = await channel.fetch_message(svr.message_id['role_verify_phone'])
    await msg.edit(content=svr.message_edit_verify_phone_content)
    for i in range(len(svr.verify_phone_emoji)):
        await msg.add_reaction(svr.verify_phone_emoji[i])

@client.command()
@commands.is_owner()
async def edit_invite_s(ctx, guild_id:int):
    if guild_id not in guild_list:
        return
    if invide_mode != 2:
        return
    svr = guild_list[guild_id]
    embedvar = discord.Embed(title="請選取身分組!",
                              description=svr.embed_edit_invite, color=0x00ff00)
    channel = client.get_channel(svr.channel_id['select_role'])
    msg = await channel.fetch_message(svr.message_id['role_main'])
    await msg.edit(content=svr.message_edit_invite,embed=embedvar)
    for i in range(len(svr.role_emoji)):
        await msg.add_reaction(svr.role_emoji[i])

@client.command()
@commands.is_owner()
async def edit_color_s(ctx, guild_id:int):
    if guild_id not in guild_list:
        return
    if invide_mode != 2:
        return
    svr = guild_list[guild_id]
    embedvar = discord.Embed(title="請選取顏色身分組!",
                              description=svr.embed_edit_color, color=0x00ff00)
    channel = client.get_channel(svr.channel_id['select_role'])
    msg = await channel.fetch_message(svr.message_id['role_color'])
    await msg.edit(content=svr.message_edit_color,embed=embedvar)
    for i in range(len(svr.role_color_emoji)):
        await msg.add_reaction(svr.role_color_emoji[i])

@client.command()
@commands.is_owner()
async def edit_icon_s(ctx, guild_id:int):
    if guild_id not in guild_list:
        return
    if invide_mode != 2:
        return
    svr = guild_list[guild_id]
    if svr.message_id_enable['role_icon'] == 0:
        return

    embedvar = discord.Embed(title="請選取圖標身分組! (Receive your icon's role)",
                              description=svr.embed_edit_icon, color=0x00ff00)
    channel = client.get_channel(svr.channel_id['select_role'])
    msg = await channel.fetch_message(svr.message_id['role_icon'])
    await msg.edit(content=svr.message_edit_icon,embed=embedvar)
    for i in range(len(svr.role_icon_emoji)):
        await msg.add_reaction(svr.role_icon_emoji[i])


@client.event
async def on_raw_reaction_add(payload):
    if payload.member.bot:
        return

    if payload.guild_id in guild_list:
        svr = guild_list[payload.guild_id]
        guild = client.get_guild(payload.guild_id)
        member = discord.utils.get(guild.members, id=payload.user_id)

        if payload.message_id == svr.message_id['role_main']:
            for i in range(len(svr.role_emoji)):
                if str(payload.emoji) == svr.role_emoji[i]:
                    role = guild.get_role(svr.role_id[i])
                    break
            if role is not None:
                await payload.member.add_roles(role)
            return

        elif payload.message_id == svr.message_id['role_color']:
            for i in range(len(svr.role_color_emoji)):
                if str(payload.emoji) == svr.role_color_emoji[i]:
                    role = guild.get_role(svr.role_color_id[i])
                    break
            if role is not None:
                await payload.member.add_roles(role)
            return

        #240512
        elif payload.message_id == svr.message_id['role_icon']:
            for i in range(len(svr.role_icon_emoji)):
                if str(payload.emoji) == svr.role_icon_emoji[i]:
                    role = guild.get_role(svr.role_icon_id[i])
                    break
            if role is not None:
                await payload.member.add_roles(role)
            return
        
        elif payload.message_id == svr.message_id['role_verify_phone']: # 230808
            for i in range(len(svr.verify_phone_emoji)):
                if str(payload.emoji) == svr.verify_phone_emoji[i]:
                    role = guild.get_role(svr.guest_role_id)
                    break
            if role is not None:
                await payload.member.add_roles(role)

            channel         = client.get_channel(svr.channel_id['help'])
            mention_message = f'<@{member.id}>\n'
            await channel.send(content=(mention_message))

            message         = svr.message_on_member_join
            msg_entry = await channel.send(content=(message+"\n\n"+svr.jp_info))#,embed=embed)
            await msg_entry.add_reaction(svr.emoji_jp)
            await payload.member.send(content=message)#,embed=embed)

            return

        elif payload.channel_id == svr.channel_id['invite'] or payload.channel_id == svr.channel_id['help']:
            if str(payload.emoji) != svr.emoji_jp and str(payload.emoji) != svr.emoji_cn:
                return

            entry_channel = client.get_channel(payload.channel_id)
            entry_msg     = await entry_channel.fetch_message(payload.message_id)

            check = 0
            for reaction in entry_msg.reactions:
                if str(reaction.emoji) == svr.emoji_jp or str(reaction.emoji) == svr.emoji_cn:
                    if reaction.count >= 2:
                        check = 1

            if payload.channel_id == svr.channel_id['invite']:
                await entry_msg.clear_reactions()

                msg = ""
                info = ""
                if str(reaction.emoji) == svr.emoji_jp:
                    msg = svr.jp_message_on_member_update
                    info = svr.cn_info
                    await entry_msg.add_reaction(svr.emoji_cn)
                elif str(reaction.emoji) == svr.emoji_cn:
                    msg = svr.message_on_member_update
                    info = svr.jp_info
                    await entry_msg.add_reaction(svr.emoji_jp)

                await entry_msg.edit(content=(msg+"\n\n"+info))
                await payload.member.send(content=msg)\
                    
                return

            elif payload.channel_id == svr.channel_id['help']:
                await entry_msg.clear_reactions()

                msg = ""
                info = ""
                if str(reaction.emoji) == svr.emoji_jp:
                    msg = svr.jp_message_on_member_join
                    info = svr.cn_info
                    await entry_msg.add_reaction(svr.emoji_cn)
                elif str(reaction.emoji) == svr.emoji_cn:
                    msg = svr.message_on_member_join
                    info = svr.jp_info
                    await entry_msg.add_reaction(svr.emoji_jp)

                await entry_msg.edit(content=(msg+"\n\n"+info))
                await payload.member.send(content=msg)
                
                return

            return

        return

    guild = client.get_guild(payload.guild_id)
    member = discord.utils.get(guild.members, id=payload.user_id)
    # channel and message IDs should be integer:
    if payload.message_id == channel_id_message_role_1:
        if str(payload.emoji) == role_emoji[0]:
            role = guild.get_role(role_id[0])
        elif str(payload.emoji) == role_emoji[1]:
            role = guild.get_role(role_id[1])
        elif str(payload.emoji) == role_emoji[2]:
            role = guild.get_role(role_id[2])
        elif str(payload.emoji) == role_emoji[3]:
            role = guild.get_role(role_id[3])
        elif str(payload.emoji) == role_emoji[4]:
            role = guild.get_role(role_id[4])
        elif str(payload.emoji) == role_emoji[5]:
            role = guild.get_role(role_id[5])

        if role is not None:
            await payload.member.add_roles(role)

    if payload.message_id == channel_id_message_role_2:
        for i in range(len(role_color_emoji)):
            if str(payload.emoji) == role_color_emoji[i]:
                role = guild.get_role(role_color_id[i])
                break


#        if str(payload.emoji) == role_color_emoji[0]:
#            role = guild.get_role(role_color_id[0])
#        elif str(payload.emoji) == role_color_emoji[1]:
#            role = guild.get_role(role_color_id[1])
#        elif str(payload.emoji) == role_color_emoji[2]:
#            role = guild.get_role(role_color_id[2])
#        elif str(payload.emoji) == role_color_emoji[3]:
#            role = guild.get_role(role_color_id[3])
#        elif str(payload.emoji) == role_color_emoji[4]:
#            role = guild.get_role(role_color_id[4])
#        elif str(payload.emoji) == role_color_emoji[5]:
#            role = guild.get_role(role_color_id[5])

        if role is not None:
            await payload.member.add_roles(role)


@client.event
async def on_raw_reaction_remove(payload):
    if payload.guild_id in guild_list:
        svr = guild_list[payload.guild_id]
        guild = client.get_guild(payload.guild_id)
        member = discord.utils.get(guild.members, id=payload.user_id)

        total = [i.id for i in member.roles].count(svr.role_id[0]) + [i.id for i in member.roles].count(svr.role_id[1]) + [i.id for i in member.roles].count(svr.role_id[4]) + [i.id for i in member.roles].count(svr.role_id[5])

        if payload.message_id == svr.message_id['role_main']:
            for i in range(len(svr.role_emoji)):
                if str(payload.emoji) == svr.role_emoji[i]:
                    role = guild.get_role(svr.role_id[i])
                    if i in [0,1,4,5]:
                        total = total - 1
                    break
            if role is not None and total: # 230808
                await member.remove_roles(role)

        elif payload.message_id == svr.message_id['role_color']:
            for i in range(len(svr.role_color_emoji)):
                if str(payload.emoji) == svr.role_color_emoji[i]:
                    role = guild.get_role(svr.role_color_id[i])
                    break
            if role is not None:
                await member.remove_roles(role)

        # 240512
        elif payload.message_id == svr.message_id['role_icon']:
            for i in range(len(svr.role_icon_emoji)):
                if str(payload.emoji) == svr.role_icon_emoji[i]:
                    role = guild.get_role(svr.role_icon_id[i])
                    break
            if role is not None:
                await member.remove_roles(role)
        
        if payload.message_id == svr.message_id['role_verify_phone']: # 230808
            for i in range(len(svr.verify_phone_emoji)):
                if str(payload.emoji) == svr.verify_phone_emoji[i]:
                    role = guild.get_role(svr.guest_role_id)
                    break
            if role is not None:
                await member.remove_roles(role)

        return


    guild = client.get_guild(payload.guild_id)
    member = discord.utils.get(guild.members, id=payload.user_id)

    if payload.message_id == channel_id_message_role_1:
        if str(payload.emoji) == role_emoji[0]:
            role = guild.get_role(role_id[0])
        elif str(payload.emoji) == role_emoji[1]:
            role = guild.get_role(role_id[1])
        elif str(payload.emoji) == role_emoji[2]:
            role = guild.get_role(role_id[2])
        elif str(payload.emoji) == role_emoji[3]:
            role = guild.get_role(role_id[3])
        elif str(payload.emoji) == role_emoji[4]:
            role = guild.get_role(role_id[4])
        elif str(payload.emoji) == role_emoji[5]:
            role = guild.get_role(role_id[5])

        if role is not None:
            await member.remove_roles(role)

    if payload.message_id == channel_id_message_role_2:
        for i in range(len(role_color_emoji)):
            if str(payload.emoji) == role_color_emoji[i]:
                role = guild.get_role(role_color_id[i])
                break


#        if str(payload.emoji) == role_color_emoji[0]:
#            role = guild.get_role(role_color_id[0])
#        elif str(payload.emoji) == role_color_emoji[1]:
#            role = guild.get_role(role_color_id[1])
#        elif str(payload.emoji) == role_color_emoji[2]:
#            role = guild.get_role(role_color_id[2])
#        elif str(payload.emoji) == role_color_emoji[3]:
#            role = guild.get_role(role_color_id[3])
#        elif str(payload.emoji) == role_color_emoji[4]:
#            role = guild.get_role(role_color_id[4])
#        elif str(payload.emoji) == role_color_emoji[5]:
#            role = guild.get_role(role_color_id[5])

        if role is not None:
            await member.remove_roles(role)

# @slash.slash(name="test", description="Those burgers look tasty",        # Adding a new slash command with our slash variable
#              options=[discord_slash.manage_commands.create_option(name="first_option", description="Please enter what you want on your burger", option_type=3, required=False)])
# async def test(ctx: discord_slash.SlashContext, first_option):               # You have to name the function the 
#     await ctx.send(f'I am now gonna get you a burger with {first_option}')   # same as the command

@client.command(name="ping") # Test command which works
async def ping(ctx):
    await ctx.send("ping")

# ver 0.0.9.20, date 240316, add recorder of edit/del msg
# ver 0.0.9.21, date 240316, add recorder of edit/del msg, fix bug
# ver 0.0.9.22, date 240316, add recorder of edit/del msg, fix bug
# ver 0.0.9.23, date 240316, add recorder of edit/del msg, fix bug
# ver 0.0.9.26, date 240316, add recorder of edit/del msg, fix bug
# ver 0.0.9.27, date 240316, add recorder of edit/del msg, fix bug
# ver 0.0.9.28, date 240316, add recorder of edit/del msg, fix bug
# ver 0.0.9.32, date 240507, add s3 server
# ver 0.0.9.33, date 240512, add new role receiver
# ver 0.0.9.34, date 240512, add new role receiver, fix bug
# ver 0.0.9.35, date 240512, add new role receiver, change message format
# ver 0.0.9.36, date 240512, add new role receiver, change message format
# ver 0.0.9.37, date 240512, add new role receiver, change message format
# ver 0.0.9.38, date 240710, fix crash
# ver 0.0.9.39, date 240715, add new role
@client.command(name="check_version") # Test command which works
async def check_version(ctx):
    await ctx.send("ver 0.0.9.39, date 240715, add new role")

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

    msg_channel_simp = f'[Del] <#{message.channel.id}> <{message.channel}> --- {message.author}: {message.content} (P: {period.total_seconds():.2f}s) (C{mea_prx}: ({mca:%H:%M}){mea_msg_simp})'
    await channel_simp.send(content=msg_channel_simp,silent=True)

    msg_channel = f'[Del] <#{message.channel.id}> <{message.channel}> --- {message.author}: {message.content} (P: {period.total_seconds():.2f}s) (C: {mca:%Y-%m-%d %H:%M:%S.%f %p}{mea_msg})'
    await channel.send(content=msg_channel,silent=True)

    if (message.guild.id in guild_list):
        svr = guild_list[message.guild.id]
        if svr.channel_id['recorder_msg_del'] and message.channel.id not in channal_ignore_channal:
            channel_simp_svr = client.get_channel(svr.channel_id['recorder_msg_del'])

            msg_channel_simp_svr = f'[Del] <#{message.channel.id}> <{message.channel}> --- {message.author}: {message.content} (P: {period.total_seconds():.2f}s) (C{mea_prx}: ({mca:%H:%M}){mea_msg_simp})'
            await channel_simp_svr.send(content=msg_channel_simp_svr,silent=True)

@client.event
async def on_message_edit(message_before, message_after):
    channel = client.get_channel(channel_message_backup_edit)
    mcab = message_before.created_at.astimezone(pytz.timezone('Asia/Taipei'))
    mcaa = message_after.edited_at.astimezone(pytz.timezone('Asia/Taipei'))
    period = mcaa - mcab
    channel_simp = client.get_channel(channel_message_backup_edit_simp)

    msg_channel_simp = f'=================================================\n\
[Ed][Be] <#{message_before.channel.id}> <{message_before.channel}> --- {message_before.author}: {message_before.content}\n\
[Ed][Af] <#{message_after.channel.id}> <{message_after.channel}> --- {message_after.author}: {message_after.content} (P: {period.total_seconds():.2f}s) (C->E: ({mcab:%H:%M}) -> ({mcaa:%H:%M}))'
    await channel_simp.send(content=msg_channel_simp,silent=True)

    msg_channel = f'=================================================\n\
[Ed][Be] <#{message_before.channel.id}> <{message_before.channel}> --- {message_before.author}: {message_before.content} (C: {mcab:%Y-%m-%d %H:%M:%S.%f %p})\n\
[Ed][Af] <#{message_after.channel.id}> <{message_after.channel}> --- {message_after.author}: {message_after.content} (P: {period.total_seconds():.2f}s) (C: {mcaa:%Y-%m-%d %H:%M:%S.%f %p})'
    await channel.send(content=msg_channel,silent=True)

    if (message_after.guild.id in guild_list):
        svr = guild_list[message_after.guild.id]
        if svr.channel_id['recorder_msg_edit'] and message_after.channel.id not in channal_ignore_channal:
            channel_simp_svr = client.get_channel(svr.channel_id['recorder_msg_edit'])

            msg_channel_simp_svr = f'=================================================\n\
[Ed][Be] <#{message_before.channel.id}> <{message_before.channel}> --- {message_before.author}: {message_before.content}\n\
[Ed][Af] <#{message_after.channel.id}> <{message_after.channel}> --- {message_after.author}: {message_after.content} (P: {period.total_seconds():.2f}s) (C->E: ({mcab:%H:%M}) -> ({mcaa:%H:%M}))'
            await channel_simp_svr.send(content=msg_channel_simp_svr,silent=True)


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
        await channel.send('<@&929747501727244368>```客家道場 (JP dojo)```')
    if weekday == 6 and cst.hour == 23 and cst.minute == 30:
        await client.wait_until_ready()
        channel = client.get_channel(channel_id_2)
        await channel.send('<@&1095689201757995069>```客家道場 (ZH dojo)```')
    if weekday == 6 and cst.hour == 22 and cst.minute == 31:
        await client.wait_until_ready()
        channel = client.get_channel(channel_id)
        await channel.send('```客家道場```')
    #if cst.hour == 22 and cst.minute == 43:
    #    await client.wait_until_ready()
    #    channel_2 = client.get_channel(1085468422743277603)
    #    await channel_2.send('<@&1085468421870845956>```客家道場 (JP dojo)```')
    #if cst.hour == 22 and cst.minute == 42:
    #    await client.wait_until_ready()
    #    channel_2 = client.get_channel(1085468422743277603)
    #    await channel_2.send('<@&1095718252631572563>```客家道場 (JP dojo)```')
#Mod Leave Announcement
"""
@client.event
async def on_member_remove(member):
    print("Recognized that " + member.name + " left")
    await client.send_message(discord.Object(id=702741572344610910), '**' + member.mention + '** just left.')
    print("Sent message to #CHANNEL")
"""


# time_check.start()

client.run(os.getenv('BOT_TOKEN'))