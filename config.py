from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "d14e54b0791ca1f8b0f26786439e336e")
      API_ID = int(getenv("API_ID", "17627887"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "7144831299:AAFAG5xpXE2PHo2USbtIP2TL8CwaG6U7sAI")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002408213951").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
