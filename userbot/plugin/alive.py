Import datetime
Import random
Import time

From telethon.errors import ChatSendInlineForbiddenError as noin
From telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

From . import *

#-------------------------------------------------------------------------------

ALIVE_TEMP = βββ
<b><i>π₯π₯EAGLEMAFIA-USPAMBOT π₯π₯</b></i>
<i><b>βΌ ΓwΓ±Γͺr β</i></b> : γ <a href=βtg://user?id={}β>{}</a> γ
β­ββββββββββββββ
β£β <b>Β» Telethon ~</b> <i>{}</i>
β£β <b>Β» πππ£π¦π π°π­ππͺ ππ¬π± ~</b> <i>{}</i>
β£β <b>Β» Sudo ~</b> <i>{}</i>
β£β <b>Β» Uptime ~</b> <i>{}</i>
β£β <b>Β» Ping ~</b> <i>{}</i>
β°ββββββββββββββ
<b><i>Β»Β»Β» <a href=βhttps://t.me/its_userbot'>[ πππ£π¦π ππ­ππͺ ππ¬π± ]</a> Β«Β«Β«</i></b>
βββ
#-------------------------------------------------------------------------------

@userbot_cmd(pattern=βalive$β)
Async def up(event):
    cid = await client_id(event)
    ForGo10God, USERBOT_USER, userbot_mention = cid[0], cid[1], cid[2]
    Start = datetime.datetime.now()
    Userbot = await eor(event, β`Building Alive....`β)
    Uptime = await get_time((time.time() β StartTime))
    A = gvarstat(βALIVE_PICβ)
    If a is not None:
        B = a.split(β β)
        C = []
        If len(b) >= 1:
            For d in b:
                c.append(d)
        PIC = random.choice(c)
    Else:
        PIC = 
    Userbot_pic = PIC
    End = datetime.datetime.now()
    Ling = (end β start).microseconds / 1000
    Omk = ALIVE_TEMP.format(ForGo10God, USERBOT_USER, tel_ver, userbot_ver, is_sudo, uptime, ling)
    Await event.client.send_file(event.chat_id, file=userbot_pic, caption=omk, parse_mode=βHTMLβ)
    Await userbot.delete()


Msg = βββ{}\n
<b><i>π π±ππ ππππππ π</b></i>
<b>Telethon β</b>  <i>{}</i>
<b>spam botβ</b>  <i>{}</i>
<b>Uptime β</b>  <i>{}</i>
<b>Abuse β</b>  <i>{}</i>
<b>Sudo β</b>  <i>{}</i>
βββ
Botname = Config.BOT_USERNAME

@userbot_cmd(pattern=βuserbot$β)
Async def userbot_a(event):
    cid = await client_id(event)
    ForGo10God, USERBOT_USER, userbot_mention = cid[0], cid[1], cid[2]
    Uptime = await get_time((time.time() β StartTime))
    Am = gvarstat(βALIVE_MSGβ) or β<b>Β»Β» Mafia spam bot ΞΉΡ ΟΠΈβΞΉΠΈΡ Β«Β«</b>β
    Try:
        Userbot = await event.client.inline_query(botname, βaliveβ)
        Await userbot[0].click(event.chat_id)
        If event.sender_id == ForGo10God:
            Await event.delete()
    Except (noin, dedbot):
        Await eor(event, msg.format(am, tel_ver, userbot_ver, uptime, abuse_m, is_sudo), parse_mode=βHTMLβ)


CmdHelp(βaliveβ).add_command(
  βaliveβ, None, βShows the Default Alive Messageβ
).add_command(
  βuserbotβ, None, βShows Inline Alive Menu with more details.β
).add_warning(
  ββ Harmless Moduleβ
).add()
