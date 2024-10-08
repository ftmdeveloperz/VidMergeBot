from os import getcwd

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Vars:
    CACHE_TIME = int(config("CACHE_TIME", default=5))
    DOWN_PATH = f"{getcwd()}/vidmergebot/downloads"
    BOT_TOKEN = config("BOT_TOKEN", "8022217287:AAFjlnVSvhrGOZHHycb8GI3CZ3MkGlrny0I")
    BOT_ID = BOT_TOKEN.split(":")[0]
    APP_ID = int(config("API_ID", "28776072"))
    API_HASH = config("API_HASH", "b3a786dce1f4e7d56674b7cadfde3c9d")
    WORKERS = int(config("WORKERS", default=16))
    STREAMTAPE_API_PASS = config("STREAMTAPE_API_PASS", "2qJoVG3wLqSZwkr")
    STREAMTAPE_API_USERNAME = config("STREAMTAPE_API_USERNAME", "0a578760a5a837896f60")
    MESSAGE_DUMP = int(config("MESSAGE_DUMP"))
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/ !").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="ftmbotzsupport")
    AUTH_CHANNEL = config("AUTH_CHANNEL", default=-1002443877080)
    OWNER_ID = int(config("OWNER_ID", default=7711039923))
    CAPTION = config("CAPTION", default="By @ftmdeveloper")
    VERSION = config("VERSION", default="v1.1 - Stable")
    STREAMTAPE_DEFAULT = config("STREAMTAPE_DEFAULT", default=None, cast=config.boolean)
    BOT_USERNAME = config("BOT_USERNAME", "ftmmergerrobot")
    DB_URI = config("DB_URI", "mongodb+srv://ftmserver:ftm@cluster0.fneio.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    MAX_VIDEOS = int(config("MAX_VIDEOS", default=10))
    JOIN_CHECK = config("JOIN_CHECK", default=True, cast=config.boolean)
    MAX_NON_JOIN_USAGE = int(config("MAX_NON_JOIN_USAGE", default=2))
    MAX_JOIN_USAGE = int(config("MAX_JOIN_USAGE", default=10))
    LIMIT_USER_USAGE = config("LIMIT_USER_USAGE", default=True, cast=config.boolean)
