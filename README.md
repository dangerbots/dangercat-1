<h1 align="center">
  <b>The DangerCat UserBot</b>
</h1>

<p align="center">
  <img src="https://telegra.ph/file/078df46ef8b32f89aef40.jpg" alt="The-DangerCat-UserBot">
</p>

<h6 align="center">
  <b>⚡ Danger Cat Userbot ⚡</b>
</h6>

<h3 align="center">
  <b>A Smooth & Fast Telegram Userbot Based On Telethon Bot Library.</b>
</h3>

------
![GitHub forks](https://img.shields.io/github/forks/Dangerprobots/dangercat?style=social)
![GitHub Repo stars](https://img.shields.io/github/stars/Dangerprobots/dangercat?style=social)

![Repo Size](https://img.shields.io/github/repo-size/Dangerprobots/dangercat?&style=social&logo=github)
![Branch](https://img.shields.io/badge/Branch-Master-white?&style=social&logo=github)

![Maintenance](https://img.shields.io/badge/Maintained%3F-Yes-white?&style=social&logo=hugo)
![GitHub license](https://img.shields.io/github/license/Dangerprobots/dangercat?&style=social&logo=github)

![Python](https://img.shields.io/badge/Python-v3.10-white?style=social&logo=python)
![GitHub language count](https://img.shields.io/github/languages/count/Dangerprobots/dangercat?&style=social&logo=hyper)

[![Telegram Group](https://img.shields.io/badge/Telegram-Group-white?&style=social&logo=telegram)](https://t.me/danger_bots)
[![Telegram Channel](https://img.shields.io/badge/Telegram-Channel-white?&style=social&logo=telegram)](https://t.me/dangerbots)

------
## Deploy 🚀
- [![Heroku](https://img.shields.io/badge/DangerCatBot-Deploy%20To%20Heroku-black?style=for-the-badge&logo=heroku)](#Deploy-To-Heroku)

### Deploy on Railway
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/4C897t)

- [![Locally](https://img.shields.io/badge/DangerCatBot-Deploy%20Locally-black?style=for-the-badge&logo=linux)](#Deploy-Locally)

------

<h1 align="center">
  <b>Follow this format to make your own plugin for DangerCatBot</b>
</h1>

```python3
"""
A sample code to display hello without taking input.
"""
# this is a mandatory import
from . import *

# assigning command
@danger_cat_cmd(pattern="hii$")
async def hi(event):
    # command body
    await eor(event, "Hello!")


# to display in help menu
CmdHelp("hii").add_command(
  "hii", None, "Says Hello!"
).add()
```
----
```python3
"""
A sample code to display hello with input.
"""
# this is a mandatory import
from . import *

# assigning command
@danger_cat_cmd(pattern="hii(?:\s|$)([\s\S]*)")
async def hi(event):
    # command body
    _input = event.pattern_match.group(1)
    if _input:
        await eor(event, f"Hello! {_input}")
    else:
        await eor(event, "Hello!")


# to display in help menu
CmdHelp("hii").add_command(
    "hii", "<text>", "Display Hello with a input!"
).add()
```


### To get more functions read codes in repo.

------

## Disclaimer
- We won't be responsible for any kind of ban due to this bot.
- DangerCatBot was made for fun purpose and to make group management easier.
- It's your concern if you spam and gets your account banned.
- Also, Forks won't be entertained.
- If you fork this repo and edit plugins, it's your concern for further updates.
- Forking Repo is fine. But if you edit something we will not provide any help.
- In short, Fork At Your Own Risk.

------
# License

![](https://www.gnu.org/graphics/gplv3-or-later.png)

<h4 align="center">Copyright (C) 2022 <a href="https://github.com/Dangerprobots">The-DangerProBots</a></h4>

Project [DangerCat](https://github.com/Dangerprobots/dangercat) is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.

------
## Credits

- 💖 [Telethon](https://github.com/LonamiWebs/Telethon)
- 💖 Hell bot
- 💖 Team DangerBot

------
