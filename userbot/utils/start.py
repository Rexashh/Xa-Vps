from telethon import Button

from userbot import BOTLOG, BOTLOG_CHATID, LOGS, tgbot


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/9b010ead0692e3bc28df6.jpg",
                caption="š¦ **Xa Userbot Has Been Actived**!!\nāāāāāāāāāāāāā\nā¬ **Userbot Version** - 8.0@Xa-Userbot\nāāāāāāāāāāāāā\nā¬ **Powered By:** @tirexgugel ",
                buttons=[(Button.url("ź±į“į“į“į“Źį“", "https://t.me/tirexgugel"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
