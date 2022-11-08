import datetime
import time

from DangerCat_config import Config, db_config, os_config
from DangerCatHub import *
from DangerCatHub.clients import *
from DangerCatHub.DB.gvar_sql import gvarstat
from DangerCatHub.helpers import *
from DangerCatHub.strings import *
from DangerCatHub.utils import *
from DangerCatHub.version import __dangerbotver__, __telever__

danger_logo = "./DangerCat_config/resources/pics/hellbot_logo.jpg"
cjb = "./DangerCat_config/resources/pics/cjb.jpg"
restlo = "./DangerCat_config/resources/pics/rest.jpeg"
shuru = "./DangerCat_config/resources/pics/shuru.jpg"
shhh = "./DangerCat_config/resources/pics/chup_madarchod.jpeg"
hl = Config.HANDLER
shl = Config.SUDO_HANDLER
hell_ver = __dangerbotver__
tel_ver = __telever__


async def get_user_id(ids):
    if str(ids).isdigit():
        userid = int(ids)
    else:
        userid = (await bot.get_entity(ids)).id
    return userid


is_sudo = "True" if gvarstat("SUDO_USERS") else "False"

abus = Config.ABUSE
if abus == "ON":
    abuse_m = "Enabled"
else:
    abuse_m = "Disabled"


my_channel = Config.MY_CHANNEL or "danger_bots"
my_group = Config.MY_GROUP or "dangerbots"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

chnl_link = "https://t.me/danger_bots"
dangercat_channel = f"[Danger Bot ]({chnl_link})"
grp_link = "https://t.me/dangerbots"
danger_grp = f"[DangerBot Group]({grp_link})"

WELCOME_FORMAT = """**Use these fomats in your welcome note to make them attractive.**
  {mention} :  To mention the user
  {title} : To get chat name in message
  {count} : To get group members
  {first} : To use user first name
  {last} : To use user last name
  {fullname} : To use user full name
  {userid} : To use userid
  {username} : To use user username
  {my_first} : To use my first name
  {my_fullname} : To use my full name
  {my_last} : To use my last name
  {my_mention} : To mention myself
  {my_username} : To use my username
"""

# DangerCatHub
