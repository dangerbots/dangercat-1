from DangerCatHub.DB.pmlogger_sql import add_nolog, del_nolog, get_all_nolog, is_nolog
from . import *

lg_id = Config.PM_LOG_ID


@danger_cat_cmd(pattern="save(?:\s|$)([\s\S]*)")
async def _(event):
    if f"{hl}savewelcome" in event.text:
        return
    DANGERCATUSERID, _, _ = await client_id(event)
    if lg_id:
        if event.reply_to_msg_id:
            reply_msg = await event.get_reply_message()
            await reply_msg.forward_to(lg_id)
        elif event.pattern_match.group(1):
            user = f"#LOG | Chat ID: `{event.chat_id}`\n\n"
            textx = user + event.pattern_match.group(1)
            await event.client.send_message(lg_id, textx)
        else:
            await parse_error(event, "Nothing given to save !")
            return
        await eod(event, "`Saved Successfully`")
    else:
        if event.reply_to_msg_id:
            reply_msg = await event.get_reply_message()
            await reply_msg.forward_to(DANGERCATUSERID)
        elif event.pattern_match.group(1):
            user = f"#LOG | Chat ID: `{event.chat_id}`\n\n"
            textx = user + event.pattern_match.group(1)
            await event.client.send_message(DANGERCATUSERID, textx)
        else:
            await parse_error(event, "Nothing given to save !")
            return
        await eod(event, "`Saved Successfully`")


@dangerbot_handler(func=lambda e: e.is_private, incoming=True)
async def _(event):
    if lg_id is None:
        return
    DANGERCATUSERID, _, _ = await client_id(event)
    sender = await event.get_sender()
    if not sender.bot:
        chat = await event.get_chat()
        if lg_id:
            if is_nolog(str(chat.id)):
                return
            if chat.id != DANGERCATUSERID:
                try:
                    await event.client.forward_messages(
                        lg_id, event.message, silent=True
                    )
                except Exception as e:
                    LOGS.info(str(e))


@danger_cat_cmd(pattern="elog$")
async def _(event):
    if lg_id:
        chat = await event.get_chat()
        if event.is_private:
            try:
                del_nolog(str(chat.id))
                await eod(event, "Will Log Messages from this chat")
            except Exception as e:
                await parse_error(event, e)
        else:
            await parse_error(event, "Chat is not a PM.")
    else:
        await parse_error(event, "`PM_LOG_ID` is not configured.", False)


@danger_cat_cmd(pattern="nlog$")
async def _(event):
    if lg_id:
        chat = await event.get_chat()
        if event.is_private:
            if is_nolog(str(chat.id)):
                return await eod(event, "Already logging is disabled for this chat.")
            add_nolog(str(chat.id))
            await eod(event, "Won't Log Messages from this chat")
        else:
            await parse_error(event, "Chat is not a PM.")
    else:
        await parse_error(event, "`PM_LOG_ID` is not configured.", False)


@danger_cat_cmd(pattern="allnolog$")
async def _(event):
    text = "**Not logging messages from:**\n"
    all_nolog = get_all_nolog()
    for i in all_nolog:
        chat = i.chat_id
        text += f"\n•  `{chat}`"
    await eor(event, text)


CmdHelp("pm_logger").add_command(
    "save", "<reply>", "Saves the replied message to your pm logger group/channel"
).add_command(
    "elog", None, "Enables logging pm messages from the selected chat."
).add_command(
    "nlog", None, f"Disables logging pm messages from the selected chat. Use {hl}elog to enable it again."
).add_command(
    "allnolog", None, "Get the list of all groups with pm logging disabled."
).add_info(
    "PM logging."
).add_warning(
    "✅ Harmless Module."
).add()
