from async_timeout  import timeout

from telethon.errors.rpcerrorlist import YouBlockedUserError

from . import *


@danger_cat_cmd(pattern="history(?:\s|$)([\s\S]*)")
async def _(dangercat_event):
    if not dangercat_event.reply_to_msg_id:
        await parse_error(dangercat_event, "No user mentioned!")
        return
    in_chat = dangercat_event.chat_id
    reply_message = await dangercat_event.get_reply_message()
    chat = "Sangmatainfo_bot"
    victim = reply_message.sender.id
    if reply_message.sender.bot:
        await eod(dangercat_event, "Need actual users. Not Bots")
        return
    hell = await eor(dangercat_event, "Checking...")
    success = False
    async with dangercat_event.client.conversation(chat) as conv:
        try:
            first = await conv.send_message(f"/search_id {victim}")
            try:
                await hell.delete()
                response1 = await conv.get_response()
                if response1 and response1.text.startswith("🔗"):
                    success = False
                else:
                    await dangercat_event.client.send_message(in_chat, response1.text, reply_to=reply_message)
                    success = True
                await dangercat_event.client.delete_messages(conv.chat_id, [response1.id])

                response2 = await conv.get_response()
                if response2 and response2.text.startswith("🔗"):
                    success = False
                else:
                    await dangercat_event.client.send_message(in_chat, response2.text, reply_to=reply_message)
                    success = True
                await dangercat_event.client.delete_messages(conv.chat_id, [response2.id])

                response3 = await conv.get_response()
                if response3 and response3.text.startswith("🔗"):
                    success = False
                else:
                    await dangercat_event.client.send_message(in_chat, response3.text, reply_to=reply_message)
                    success = True
                await dangercat_event.client.delete_messages(conv.chat_id, [response3.id])
            except TimeoutError:
                pass
            if success == False:
                hell = await dangercat_event.client.send_message(in_chat, "**ERROR**", reply_to=reply_message)
                await parse_error(hell, "Unexpected Error Occured !!")
            await dangercat_event.client.delete_messages(conv.chat_id, [first.id])
        except YouBlockedUserError:
            return await parse_error(hell, "__Unblock @Sangmatainfo_bot and try again.__", False)

CmdHelp("history").add_command(
    "history", "<reply to a user>", "Fetches the name history of replied user."
# ).add_command(
#     "unh", "<reply to user>", "Fetches the Username History of replied users."
).add_info(
    "Telegram Name History"
).add_warning(
    "✅ Harmless Module."
).add()
