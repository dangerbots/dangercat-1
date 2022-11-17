
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_peer_id

from .session import H2, H3, H4, H5, DangetCat


async def clients_list():
    user_ids = []
    if gvarstat("SUDO_USERS"):
        a = gvarstat("SUDO_USERS").split(" ")
        for b in a:
            c = int(b)
            user_ids.append(c)
    main_id = await DangetCat.get_me()
    user_ids.append(main_id.id)

    try:
        if H2 is not None:
            id2 = await H2.get_me()
            user_ids.append(id2.id)
    except:
        pass

    try:
        if H3 is not None:
            id3 = await H3.get_me()
            user_ids.append(id3.id)
    except:
        pass

    try:
        if H4 is not None:
            id4 = await H4.get_me()
            user_ids.append(id4.id)
    except:
        pass

    try:
        if H5 is not None:
            id5 = await H5.get_me()
            user_ids.append(id5.id)
    except:
        pass

    return user_ids


async def client_id(event, botid=None):
    if botid is not None:
        uid = await event.client(GetFullUserRequest(botid))
        DANGERCATUSERID = uid.user.id
        DANGERCATUSER = uid.user.first_name
        dangerbot_mention = f"[{DANGERCATUSER}](tg://user?id={DANGERCATUSERID})"
    else:
        client = await event.client.get_me()
        uid = get_peer_id(client)
        DANGERCATUSERID = uid
        DANGERCATUSER = client.first_name
        dangerbot_mention = f"[{DANGERCATUSER}](tg://user?id={DANGERCATUSERID})"
    return DANGERCATUSERID, DANGERCATUSER, dangerbot_mention
