class script(object):
    START_TXT = """ð·ðīðŧðū {},
ðžð ð―ð°ðžðī ðļð <a href=https://t.me/{}>{}</a>, ðļ ðēð°ð― ðŋððūððļðģðī ðžðūððļðīð, ðđððð ð°ðģðģ ðžðī ððū ððūðð ðķððūððŋ ð°ð―ðģ ðžð°ðšðī ðžðī ð°ðģðžðļð―.. ðð·ðīð― ððīðī ðžð ðŋðūððīðð âĨïļâĨïļðĨ"""
    HELP_TXT = """ð·ðīð {}
ð·ðīððī ðļð ðžð ð·ðīðŧðŋ ðēðūðžðžð°ð―ðģð."""
    ABOUT_TXT = """ð§ðððĶ  ð ðĶð

âĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩ

ââââââ° ęŠáĨęŠŪęŠð― ęŠðīá§ âąâââąâÛŠÛŠ

ââ­ââââââââââââââââĢ 

ââĢâŠž ðð ððžðð - <a href="https://t.me/Prv_35Bot"> ððĻð§ððē ððĻðŽð </a>

ââĢâŠž ððððð - <a href="https://t.me/KL_2335"> Prv </a>

ââĢâŠž ððððĄðĄðð - <a href="https://t.me/kmtz_channel_v3"> ðððð ððððððð </a>

ââĢâŠž ððēðŦðŧðŠðŧðŧð - UK ááá·ááĐááĐ(United Kollam)

ââĢâŠž ððŠð·ð°ðūðŠð°ðŪ - Manglish

ââĢâŠž ððŠð―ðŠ ððŠðžðŪ - āīāīĻāĩāīąāĩ āīŦāīŊāĩ―āīļāĩāīāĩū

āīāīĻāĩāīąāĩ āīļāĩāīĩāīūāīŊāīāīūāī°āĩāīŊāīĪāīŊāīūāīĢāĩ

ââĢâŠž ððļð― ðžðŪðŧðŋðŪðŧ -  KERALA

ââĢâŠž ððūðēðĩð­ ðĒð―ðŠð―ðūðž - v1.0.1 [ ðąðīðð° ]

ââ°ââââââââââââââââĢ âââââââââââââââââââââąâÛŠÛŠ"""
    DONATION_TXT = """<b>ððĻð§ðð­ðĒðĻð§ & ðððĒð ððŦðĻðĶðĻð­ðĒðĻð§</b> 

âšâš <b>ððĻð§ðð­ðĒðĻð§</b>

âŠž <b>ððĻðŪ ððð§ ððĻð§ðð­ð ðð§ðē ððĶðĻðŪð§ð­ ððĻðŪ ðððŊð ðģ. 
<b>âââââââââá Payment Methods áâââââââââ
âŪ ððžðžðīðđðēðĢðŪð
âŪ ðĢðŪðððš
âŪ ðĢðĩðžðŧðēðĢðē
âŪ ðĢðŪððĢðŪðđ
_ððĻð§ð­ððð­ ðð ððĻðŦ ðð§ðĻð° ðððĻðŪð­ ððĄð ðððēðĶðð§ð­ ðð§ððĻ_
ââââââââââââá <a href=https://t.me/sources_cods><b>ððūðĄðū</b></a> áââââââââââââ

âšâš <b>ðððĒð ððŦðĻðĶðĻð­ðĒðĻð§</b>

âŠž <b>ððĻð§ð­ððð­ ðð ððĒð­ðĄ ððĻðŪ ððĻð§ð­ðð§ð­ ððĄðĒððĄ ððĻðŪ ððð§ð­ ððĻ ððŦðĻðĶðĻð­ð . 
<b>âââââââââá Payment Methods áâââââââââ
âŪ ððžðžðīðđðēðĢðŪð
âŪ ðĢðŪðððš
âŪ ðĢðĩðžðŧðēðĢðē
âŪ ðĢðŪððĢðŪðđ
_ððĻð§ð­ððð­ ðð ððĒð­ðĄ ððĻðŪðŦ ððĻð§ð­ðð§ð­ ðð§ð ðð§ðĻð° ðððĻðŪð­ ððĄð ðððēðĶðð§ð­ ðð§ððĻ_
ââââââââââââá <a href=https://t.me/sources_cods><b>ððūðĄðū</b></a> áââââââââââââ"""
    PROMOTION_TXT = """<b>ã ðððĒð ððŦðĻðĶðĻð­ðĒðĻð§ ã</b>

âŠž <b>ððĻð§ð­ððð­ ðð ððĒð­ðĄ ððĻðŪ ððĻð§ð­ðð§ð­ ððĄðĒððĄ ððĻðŪ ððð§ð­ ððĻ ððŦðĻðĶðĻð­ð . 
<b>âââââââââá Payment Methods áâââââââââ
âŪ ððžðžðīðđðēðĢðŪð
âŪ ðĢðŪðððš
âŪ ðĢðĩðžðŧðēðĢðē
âŪ ðĢðŪððĢðŪðđ
_ððĻð§ð­ððð­ ðð ððĒð­ðĄ ððĻðŪðŦ ððĻð§ð­ðð§ð­ ðð§ð ðð§ðĻð° ðððĻðŪð­ ððĄð ðððēðĶðð§ð­ ðð§ððĻ_
ââââââââââââá <a href=https://t.me/sources_cods><b>ððūðĄðū</b></a> áââââââââââââ""" 
    FILE_TXT = """âĪ ðððĨðĐ: ððĒðĨð ðð­ðĻðŦð ððĻððŪðĨð../

<b>ðąð ðððļð―ðķ ðð·ðļð ðžðūðģððŧðī ððūð ðēð°ð― ðððūððī ðĩðļðŧðīð ðļð― ðžð ðģð°ðð°ðąð°ððī ð°ð―ðģ ðļ ððļðŧðŧ ðķðļððī ððūð ð° ðŋðīððžð°ð―ðīð―ð ðŧðļð―ðš  ððū ð°ðēðēðīðð ðð·ðī ðð°ððīðģ ðĩðļðŧðīð.ðļðĩ ððūð ðð°ð―ð ððū ð°ðģðģ ðĩðļðŧðīð ðĩððūðž ð° ðŋððąðŧðļðē ðēð·ð°ð―ð―ðīðŧ ððīð―ðģ ðð·ðī ðĩðļðŧð ðŧðļð―ðš ðūð―ðŧð  ðūð ððūð ðð°ð―ð ððū ð°ðģðģ ðĩðļðŧðīð ðĩððūðž ð°  ðŋððļðð°ððī ðēð·ð°ð―ð―ðīðŧ ððūð ðžððð ðžð°ðšðī ðžðī ð°ðģðžðļð― ðūð― ðð·ðī ðēð·ð°ð―ð―ðīðŧ ððū ð°ðēðēðīðð ðĩðļðŧðīð...//</b>

âŠž ððĻðĶðĶðð§ððŽ ðð§ð ððŽðð ð âš

âŠ /plink âšâš <b>ððīðŋðŧð ððū ð°ð―ð ðžðīðģðļð° ððū ðķðīð ðŧðļð―ðš.</b>
âŠ /pbatch âšâš <b>ðððī ððūðð ðžðīðģðļð° ðŧðļð―ðš ððļðð· ðð·ðļð ðēðūðžðžð°ð―ðģ.</b>
âŠ /batch âšâš <b>ððū ðēððīð°ððī ðŧðļð―ðš ðĩðūð ðžððŧððļðŋðŧðī ðĩðļðŧðīð.</b>

âŠž ððąððĶðĐðĨð âš

<code>/batch https://t.me/Prv_35/3 https://t.me/Prv_35/8</code>

ðēððīðģðļðð âšâš <a href=https://t.me/Prv_35><b>PranavâĨïļ</b></a>"""
    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- Give a user details
âĒ/whois :-give a user full details"""
    FUN_TXT ="""<b>Gáīáīáīs</b> 
    
<b>âĄ ðđððð ððūðžðī ðšðļð―ðģ ðūðĩ ðĩðð― ðð·ðļð―ðķ'ð âĄ</b>
 
ðĢ. /dice - ððūðŧðī ðð·ðī ðģðļðēðī 
ðĪ. /Throw ðð /Dart - ððū ðžð°ðšðī ðģð°ðð 
3. /Runs - ððūðžðī ðð°ð―ðģðūðž ðģðļð°ðŧðūðķððīð 
4. /Goal or /Shoot - ððū ðžð°ðšðī ð° ðķðūð°ðŧ ðūð ðð·ðūðūð
5. /luck or /cownd - ððŋðļð― ð°ð―ðģ ððð ððūðð ðŧððēðš"""
    DEPLOY_TXT = """<b>ð·ðūð ððū ðģðīðŋðŧðūð..?</b> 
  
<b>âŪ Deploy Tutorial âšâš</b> <i><b>https://t.me/kmtz_channel_v3</b></i>

<b>ðļðĩ ððūð ðð°ð―ð ðð·ðī áŊâUâáŊáķ-ðŋððū-ðžð°ð ððīðŋðū ðēðūð―ðð°ðēð <a href=https://t.me/KL_2335>Pranav</a></b>

<b>ðð·ð°ððī ð°ð―ðģ ðððąððēððļðąðī</b>
ðēððīðģðļðð âšâš <a href=https://t.me/Prv_35><b>áŊâUâáŊáķâĨïļ</b></a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and áŊâUâáŊáķ will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Prana should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
âĒ /filter - <code>add a filter in chat</code>
âĒ /filters - <code>list all the filters of a chat</code>
âĒ /del - <code>delete a specific filter in chat</code>
âĒ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    SONG_TXT = """<b>ððūð―ðķ ðģðūðð―ðŧðūð°ðģ ðžðūðģððŧðī</b>

<b>ððūð―ðķ ðģðūðð―ðŧðūð°ðģ ðžðūðģððŧðī, ðĩðūð ðð·ðūððī ðð·ðū ðŧðūððī ðžðððļðē. ððūð ðēð°ð― ðððī ðð·ðļð ðĩðīð°ðððī ðĩðūð ðģðūðð―ðŧðūð°ðģ ð°ð―ð ððūð―ðķ ððļðð· ðððŋðīð ðĩð°ðð ððŋðīðīðģ.ððūððšð ðūð―ðŧð ðūð― ðķððūððŋð../</b>

<b>ðēðūðžðžð°ð―ðģð</b>

âšâš  /song ððūð―ðķ ð―ð°ðžðī 

ððūððšð ðūð―ðŧð ðūð― ðķððūððŋ

ðēððīðģðļðð :- <a href=https://t.me/KL_2335>Prnav</a>"""
    PIN_TXT ="""<b>PIN MODULE</b>
<b>ðŋðļð― ð° ðžðīððð°ðķðī../</b>

<b>ð°ðŧðŧ ðð·ðī ðŋðļð― ððīðŧð°ððīðģ ðēðūðžðžð°ð―ðģð ðēð°ð― ðąðī ðĩðūðð―ðģ ð·ðīððī::</b>

<b>ððēðūðžðžð°ð―ðģð ð°ð―ðģ ððð°ðķðīð</b>

â /pin :- ððū ðŋðļð― ðð·ðī ðžðīððð°ðķðī ðūð― ððūðð ðēð·ð°ðð
â /unpin :- ððū ðð―ðŋðļð― ðð·ðī ðēððððīðīð―ð ðŋðļð―ð―ðīðģ ðžðīðð°ð°ðķðī"""
    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>

âĒ /paste [text] - paste the given text on Pasty

<b>NOTE:</b>

âĒ These commands works on both pm and group.
âĒ These commands can be used by any group member."""
    TTS_TXT = """Help: <b> TTS ðĪ module:</b>

Translate text to speech

<b>Commands and Usage:</b>

âĒ /tts <text> : convert text to speech

<b>NOTE:</b>

âĒ IMDb should have admin privillage.
âĒ These commands works on both pm and group.
âĒ IMDb can translate texts to 200+ languages."""
    PINGS_TXT ="""<b>ð Ping:</b>

Helps you to know your ping ðķðžââïļ

<b>Commands:</b>

âĒ /alive - To check you are alive.
âĒ /help - To get help.
âĒ /ping - To get your ping.
âĒ /repo - Source Code.
âĒ /channel - Channel Details.
âĒ /anurag - Bot Link.
<b>ðđUsageðđ :</b>

âĒ This commands can be used in pms and groups
âĒ This commands can be used buy everyone in the groups and bots pm
âĒ Share us for more features"""
    TELE_TXT = """<b>âŦïļHELP: TelegraphâŠïļ</b>

Do as you wish with telegra.ph module!

</b>USAGE:</b>

ðĪ§ /telegraph - Send me Picture or Vide Under (5MB)

<b>NOTE:</b>

âĒ This Command Is Available in goups and pms
âĒ This Command Can be used by everyone"""

    PRIVATEBOT_TXT = """<b>ðŋððļðð°ððī ðąðūð ðĩðūð ððūð</b>
<b>âšâš ðģðū ððūð ðð°ð―ð ð° ðąðūð ðð°ðžðī ðŧðļðšðī ðð·ðļð</b>
<b>âšâš ððļðð· ð°ðŧðŧ ððūðð ðēððīðģðļðð</b>
<b>âšâš ððļðð· ððūðð ðūðð―ðīððð·ðļðŋ</b>
<b>âšâš ðēðūð―ðð°ðēð ðžðī <a href=https://t.me/KL_2335>Prv_35</a></b>"""

    JSON_TXT ="""<b>JSON:</b>

Bot returns json for all replied messages with /json

<b>Features:</b>

Message Editting JSON
Pm Support
Group Support

<b>Note:</b>

Everyone can use this command , if spaming happens bot will automatically ban you from the group."""
    PURGE_TXT = """<b>Purge</b>
    
Delete A Lot Of Messages From Groups! 
    
 <b>ADMIN</b> 

â /purge :- Delete All Messages From The Replied To Message, To The Current Message"""
    BUTTON_TXT = """Help: <b>Buttons</b>

-Pranav  Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Pranav supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Prv_35)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """<b>ð°ðððū ðĩðļðŧððīð ðūð―/ðūðĩðĩ ðžðūðģððŧðī..</b>

<b>ð°ðððū ðĩðļðŧððīð ðļð ðð·ðī ðĩðīð°ððððī ððū ðĩðļðŧððīð ð°ð―ðģ ðð°ððī  ðð·ðī ðĩðļðŧðīð ð°ðððūðžð°ððļðēð°ðŧðŧð ðĩððūðž ðēð·ð°ð―ð―ðīðŧ ððū ðķððūððŋ. ððūð ðēð°ð― ðððī ðð·ðī ðĩðūðŧðŧðūððļð―ðķ ðēðūðžðžð°ð―ðģð ððū ðūð― ð°ð―ðģ ðūðĩðĩ ðð·ðī ð°ðððūðĩðļðŧððīð ðļð― ððūðð ðķððūððŋ.../</b>

<b>ðēðūðžðžð°ð―ðģð :-
<b>âšâš /autofilter on - ðīð―ð°ðąðŧðī ð°ðððū ðĩðļðŧððīð ðļð― ðð·ðī ðķððūððŋð.</b>
<b>âšâš /autofilter off - ðģðļðð°ðąðŧðīðģ ð°ðððū ðĩðļðŧððīð ðļð― ðð·ðī ðķððūððŋð.</b>
<b>âšâš /set_template - ððīð ðēððððūðž ðļðžðģðą ððīðžðŋðŧð°ððī ðĩðūð ð°ðððū ðĩðļðŧððīð.</b>
<b>âšâš /get_template - ðķðīð ðēððððīð―ð ðļðžðģðą ððīðžðŋðŧð°ððī ðūðĩ ð°ðððū ðĩðļðŧððīð.</b>

<b>ðēððīðģðļðð :- <a href=https://t.me/sources_cods>ððūðĄðū</a></b>"""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
âĒ /connect  - <code>connect a particular chat to your PM</code>
âĒ /disconnect  - <code>disconnect from a chat</code>
âĒ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Pranav

<b>Commands and Usage:</b>
âĒ /id - <code>get id of a specifed user.</code>
âĒ /info  - <code>get information about a user.</code>
âĒ /imdb  - <code>get the film information from IMDb source.</code>
âĒ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
âĒ /logs - <code>to get the rescent errors</code>
âĒ /stats - <code>to get status of files in db.</code>
âĒ /delete - <code>to delete a specific file from db.</code>
âĒ /users - <code>to get list of my users and ids.</code>
âĒ /chats - <code>to get list of the my chats and ids </code>
âĒ /leave  - <code>to leave from a chat.</code>
âĒ /disable  -  <code>do disable a chat.</code>
âĒ /ban_user  - <code>to ban a user.</code>
âĒ /unban_user  - <code>to unban a user.</code>
âĒ /channel - <code>to get list of total connected channels</code>
âĒ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b>áâš ððūðð°ðŧ ðĩðļðŧðīð: <code>{}</code></b>
<b>áâš ððūðð°ðŧ ðððīðð: <code>{}</code></b>
<b>áâš ððūðð°ðŧ ðēð·ð°ðð: <code>{}</code></b>
<b>áâš ðððīðģ ðððūðð°ðķðī: <code>{}</code> ðžðą</b>
<b>áâš ðĩððīðī ðððūðð°ðķðī: <code>{}</code> ðžðą</b>"""
    LOG_TEXT_G = """#ððð°ððŦðĻðŪðĐ
    
<b>áâš ððŦðĻðŪðĐ âŠž {}(<code>{}</code>)</b>
<b>áâš ððĻð­ððĨ ðððĶðððŦðŽ âŠž <code>{}</code></b>
<b>áâš ððððð ððē âŠž {}</b>
"""
    LOG_TEXT_P = """#ððð°ððŽððŦ
    
<b>áâš ðð - <code>{}</code></b>
<b>áâš ðððĶð - {}</b>
"""
    REPORT_TXT = """âĪ ðððĨðĐ: RáīáīáīĘáī â ïļ

ðððð ððððððð ððððð ðĒðð ðð ðððððð ð ððððððð ðð ð ðððð ðð ððð ðððððð ðð ððð ðððððððððð ððððð. ðģðð'ð ðððððð ðððð ððððððð.

âĪ ððĻðĶðĶðð§ððŽ ðð§ð ððŽðð ð:

âŠ/report ðð @admins - ðģð ððūðððð ðš ðððūð ðð ðððū ðšð―ðððð (ððūððð ðð ðš ððūðððšððū)."""

    CORONA_TXT = """âĪ ðððĨðĐ: ðĒðððð―

ðððð ðēðððððð ððððð ðĒðð ðð ðððð  ðððððĒ ððððððððððð ððððð ððððð 

âĪ ððĻðĶðĶðð§ððŽ ðð§ð ððŽðð ð:

âŠ /covid - ðððū ðððð ðžððððšðð― ðððð ðððð ðžðððððð ððšððū ðð ððūð ðžðððð―ðū ðððŋððððšðððð

âðĪððšððððū:
<code>/covid ðĻðð―ððš</code>"""

    URLSHORT_TXT = """âĪ ðððĨðĐ: ðīðð ðððððððūð

ðððð ððððððð ððððð ðĒðð ðð ððððð ð ððð 

âĪ ððĻðĶðĶðð§ððŽ ðð§ð ððŽðð ð:

âŠ /short: ðððū ðððð ðžððððšðð― ðððð ðððð ðððð ðð ððūð ððððððūð― ððððð

âðĪððšððððū:
<code>/short https://youtu.be/s_1VHL-SbEM</code>"""

    VIDEO_TXT ="""ð·ðīðŧðŋ ððūð ððū ðģðūðð―ðŧðūð°ðģ ððļðģðīðū ðĩððūðž ððūððððąðī.

âĒ ððīðĒðĻðĶ
ð ð°ðķ ððĒðŊ ðð°ðļðŊð­ð°ðĒðĨ ððŊðš ððŠðĨðĶð° ððģð°ðŪ ð ð°ðķðĩðķðĢðĶ

ððĪðŽ ððĪ ððĻð
âĒ ððšðąðĶ /video or /mp4 ððŊðĨ (https://youtu.be/s_1VHL-SbEM)
âĒ ððđðĒðŪðąð­ðĶ:
<code>/mp4 https://youtu.be/s_1VHL-SbEM</code>
<code>/video https://youtu.be/s_1VHL-SbEM</code>"""

    ZOMBIES_TXT = """ð·ðīðŧðŋ ððūð ððū ðšðļðēðš ðððīðð

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
âĒ /inkick - command with required arguments and i will kick members from group.
âĒ /instatus - to check current status of chat member from group.
âĒ /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
âĒ /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
âĒ /dkick - to kick deleted accounts."""

    IMAGE_TXT = """âĪ ðððĨðĐ: IáīáīÉĒáī

ðððð ððððððð ððððð ðĒðð ðð ðððð ððððð ððððĒ ððððððĒ 

âĪ ððĻðĶðĶðð§ððŽ ðð§ð ððŽðð ð:

âŠ ðĐððð ððūðð― ððū ðš ðððšððū ðð ðūð―ðð âĻ

ðŽðšð―ðū ðŧð <a href=https://t.me/KL_2335>Pranav</a>"""

    STICKER_TXT = """ððūð ðēð°ð― ðððī ðð·ðļð ðžðūðģððŧðī ððū ðĩðļð―ðģ ð°ð―ð ðððļðēðšðīðð ðļðģ.
âĒ ððððð
To Get Sticker ID
 
  â­ ððĪðŽ ððĪ ððĻð
 
â Reply To Any Sticker [/stickerid]"""

    YTTHUMB_TXT = """ð·ðīðŧðŋð ððū ðģðūðð―ðŧðūð°ðģ ð°ð―ð ððūððððąðī ððļðģðīðū ðð·ððžðąð―ð°ðļðŧ
    
â­ððĪðŽ ððĪ ððĻð
ððšðąðĶ /ytthumb ððŊðĨ ððŠðĨðĶð° ððŠðŊðŽ

âĒ ððđðĒðŪðąð­ðĶ
<code>/ytthumb https://youtu.be/s_1VHL-SbEM</code>"""

    ABOOK_TXT = """âĪ ðððĨðĐ: ð ðð―ðððŧððð

ððð ððð ððððððð ð ðŋðģðĩ ðððð ðð ð ððððð ðððð ð ððð ðððð ððððððð âŊ

âĪ ððĻðĶðĶðð§ððŽ ðð§ð ððŽðð ð:

âŠ /audiobook: ðąðūððð ðððð ðžððððšðð― ðð ðšðð ðŊðĢðĨ ðð ððūððūððšððū ðððū ðšðð―ðð"""

    GTRANS_TXT = """âĪ ðððĨðĐ: ðĶðððððū ðģððšððððšððūð

ðððð ððððððð ððððð ðĒðð ðð ððððððððð ð ðððĄð ðð ðšðð ððððððððð ðĒðð ð ððð. ðððð ððððððð ð ðððð ðð ðððð ðð ððð ððððð âŊ

âĪ ððĻðĶðĶðð§ððŽ ðð§ð ððŽðð ð:

âŠ/tr - ðģð ðððšððððšððūð ððūððð ðð ðš ðððūðžððŋðž ððšððððšððū

âĪ ð­ðððū:
ðķððððū ððððð /tr ððð ðððððð― ðððūðžððŋð ðððū ððšððððšððū ðžðð―ðū

âðĪððšððððū: /ðð ðð
âĒ ðūð = ðĪðððððð
âĒ ðð = ðŽðšððšððšððšð
âĒ ðð = ð§ððð―ð"""

    RESTRIC_TXT = """âĪ ðððĨðĐ: Máīáīáī ðŦ

ððððð ððð ððð ðððððððð ð ððððð ððððð ððð ððð ðð ðððððð ððððð ððððð ðððð ðððððððððððĒ.

âŠ/ban: ðģð ðŧðšð ðš ðððūð ðŋððð ðððū ððððð.
âŠ/unban: ðģð ðððŧðšð ðš ðððūð ðð ðððū ððððð.
âŠ/tban: ðģð ððūðððððšðððð ðŧðšð ðš ðððūð.
âŠ/mute: ðģð ððððū ðš ðððūð ðð ðððū ððððð.
âŠ/unmute: ðģð ððððððū ðš ðððūð ðð ðððū ððððð.
âŠ/tmute: ðģð ððūðððððšðððð ððððū ðš ðððūð.

âĪ ð­ðððū:
ðķððððū ððððð /tmute ðð /tban ððð ðððððð― ðððūðžððŋð ðððū ððððū ððððð.

âðĪððšððððū: /ððŧðšð 2ð― ðð /ðððððū 2ð―.
ðļðð ðžðšð ðððū ððšðððūð: ð/ð/ð―. 
 âĒ ð = ððððððūð
 âĒ ð = ððððð
 âĒ ð― = ð―ðšðð"""
    CREATOR_REQUIRED = """â<b>You have To Be The Group Creator To Do That.</b>"""
      
    INPUT_REQUIRED = "â **Arguments Required**"
      
    KICKED = """âïļ Successfully Kicked {} Members According To The Arguments Provided."""
      
    START_KICK = """ðŪ Removing Inactive Members This May Take A While..."""
      
    ADMIN_REQUIRED = """â<b>āīāīĻāĩāīĻāĩ Admin āīāīāĩāīāīĪāĩāīĪ āīļāĩāīĨāīēāīĪāĩāīĪāĩ āīāīūāĩŧ āīĻāīŋāīāĩāīāīŋāīēāĩāīē āīŠāĩāīāĩāīĩāīū Bii..Add Me Again with all admin rights.</b>"""
      
    DKICK = """âïļ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """<b>āīāīŠāĩāīŠāĩ āīāīēāĩāīēāīūāī āīāīāīŋāīāĩāīāĩāīŪāīūāīąāĩāīąāīŋ āīĪāī°āīūāī...</b>"""
      
    STATUS = """{}\n<b>Chat Member Status</b>**\n\n```<i>Recently``` - {}\n```Within Week``` - {}\n```Within Month``` - {}\n```Long Time Ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}</i>
"""
