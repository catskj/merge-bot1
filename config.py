import os


class Config(object):
    API_HASH = os.environ.get("ae8ba4c2910103634f2ffcbf9de9814a")
    BOT_TOKEN = os.environ.get("7681701929:AAH4tmQejPQYmJ4Os-F4o_qknMI3o0NZSZc")
    TELEGRAM_API = os.environ.get("25925269")
    OWNER = os.environ.get("7025034430")
    OWNER_USERNAME = os.environ.get("https://t.me/NeverStopI")
    PASSWORD = os.environ.get("qzeZOc0Xh43RGrhQ")
    DATABASE_URL = os.environ.get("mongodb+srv://tomdog637:<db_password>@cluster0.fg9gj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOGCHANNEL = os.environ.get("-1002674360578")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
