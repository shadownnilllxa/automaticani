#    This file is part of the AutoAnime distribution.
#    Copyright (c) 2024 Kaif_00z
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/kaif-00z/AutoAnimeBot/blob/main/LICENSE > .

# if you are using this following code then don't forgot to give proper
# credit to t.me/kAiF_00z (github.com/kaif-00z)

from decouple import config


class Var:
    # Telegram Credentials

    API_ID = config("API_ID", default="7713526")
    API_HASH = config("API_HASH", default="6f87b351ddf6c8c56999f8ba5b19cc7c")
    BOT_TOKEN = config("BOT_TOKEN", default="7019818679:AAEHKGQLk6HeDyc9UauwnHxqM8yudHZatoM")
    SESSION = config("SESSION", default=None)

    # Database Credentials

    FIREBASE_URL = config("FIREBASE_URL", default="https://aniwrld-b8fc4-default-rtdb.firebaseio.com/")
    FIREBASE_SERVICE_ACCOUNT_FILE = config(
        "FIREBASE_SERVICE_ACCOUNT_FILE", default="https://gist.githubusercontent.com/shadownnilllxa/2dc70da59003f3e4d8855e0b9f830880/raw/24186eadf4e725c794a4573165b54f5dce8dd548/service.json"
    )

    # Channels Ids

    BACKUP_CHANNEL = config("BACKUP_CHANNEL", default="-1002156623370")
    MAIN_CHANNEL = config("MAIN_CHANNEL", default="-1001580437794")
    LOG_CHANNEL = config("LOG_CHANNEL", default="-1002221502583")
    CLOUD_CHANNEL = config("CLOUD_CHANNEL", default="-1002187386927")
    FORCESUB_CHANNEL = config("FORCESUB_CHANNEL", default=0, cast=int)
    OWNER = config("OWNER", default="5071463525")

    # Other Configs

    THUMB = config(
        "THUMBNAIL", default="https://graph.org/file/ad1b25807b81cdf1dff65.jpg"
    )
    FFMPEG = config("FFMPEG", default="ffmpeg")
    CRF = config("CRF", default="27")
    SEND_SCHEDULE = config("SEND_SCHEDULE", default=False, cast=bool)
    RESTART_EVERDAY = config("RESTART_EVERDAY", default=True, cast=bool)
    FORCESUB_CHANNEL_LINK = config("FORCESUB_CHANNEL_LINK", default="", cast=str)
