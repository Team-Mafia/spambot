import glob
import logging
import os
from pathlib import Path
from sys import argv

import telethon.utils
from telethon import TelegramClient

from userbot import CMD_HNDLR, bot
from userbot.Config import Var
from userbot.thunderconfig import Config
from userbot.utils import load_assistant, load_module, start_assistant

TELE = Var.PRIVATE_GROUP_ID
BOTNAME = Var.TG_BOT_USER_NAME_BF_HER
LOAD_MYBOT = Var.LOAD_MYBOT
sed = logging.getLogger("EAGLEMAFIA SPAMUSERBOT")

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


async def startup_log_all_done():
    try:
        await bot.send_message(
            TELE,
            f"**EAGLEMAFIA SPAMUSERBOT has been deployed.\nSend** `{CMD_HNDLR}alive` **to see if the bot is working.\n\nAdd** @{BOTNAME} **to this group and make it admin for enabling all the features of userbot**",
        )
    except BaseException:
        print("Either PRIVATE_GROUP_ID is wrong or you have left the group.")


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished, no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()

path = "userbot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        try:
            
         load_module(shortname.replace(".py", ""))
        except Exception:
            pass
print("EAGLEMAFIA has been deployed! ")

print("Setting up EAGLEMAFIA")


if Config.ENABLE_ASSISTANTBOT == "ENABLE":
    path = "userbot/plugins/assistant/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            try:
                
            
             load_assistant(shortname.replace(".py", ""))
            except Exception:
                pass
    sed.info("EAGLEMAFIA SPAMUSERBOT Has Been Deployed Successfully !")
    sed.info("╔════❰ Ⲃⲟⲧ Ⲓⲛϝⲟʀⲙⲁⲧⲓⲟⲛ ❱═❍⊱❁۪۪")
    sed.info("║┣⪼ Ⲟⲱⲛⲉʀ -  ꧁༺ɛǟɢʟʍǟʄɨǟ ֆքǟʍʊֆɛʀɮօȶ༻꧂ ")
    sed.info("║┣⪼ Ⲋⲧⲁⲧυⲋ - Ⲟⲛⳑⲓⲛⲉ")
    sed.info("║┣⪼ Ⲃⲟⲧ Ⳳⲉʀⲋⲓⲟⲛ - 1.2.0")   
    sed.info("║┣⪼ Ⳙⲣⲧⲓⲙⲉ - 00h:00m:4s ")
    sed.info("║┣⪼ Ⲃⲟⲧ Ⲣⲓⲛⳋ - 0.006")
    sed.info("║┣⪼ Ⲣⲩⲧⲏⲟⲛ - 3.9.2")
    sed.info("║┣⪼ Ⲧⲉⳑⲉⲧⲏⲟⲛ - 1.17.0 ")
    sed.info("║┣⪼ ✨𝐄𝐀𝐆𝐋𝐌𝐀𝐅𝐈𝐀 𝐒𝐏𝐀𝐌𝐔𝐒𝐄𝐑𝐁𝐎𝐓✨")
    sed.info("║╰━━━━━━━━━━━━━━━➣ ")
    sed.info("╚══════════════════❍⊱❁۪۪")
else:
    sed.info("EAGLEMAFIA SPAMUSERBOT Has Been Installed Sucessfully !")
    sed.info("You Can Visit @BLACK_MAFIA_OP_BOLTE For Any Support Or Doubts")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()               