from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    LOGGER = True

    API_ID = int(getenv("API_ID", 29568441))
    API_HASH = getenv("API_HASH", b32ec0fb66d22da6f77d355fbace4f2a)
    ARQ_API_KEY = "PMPTTD-HOMLMF-SRBHNH-RZMWXL-ARQ"
    STRING_SESSION = getenv("STRING_SESSION", BQFFQMsAUnm3rhJPnr_uPfbRf7jKVeDFri7oJfrhdg_Ivas2L9zJMG-xjEnHXGzKB3U7F2oC_B-pHPBvdk_fRD3e8lcwPi7w80UPJV8GTtkxFYe4-O8X0h9Mqew75asVbbrnR1LFpdtLF6TDHdH1SSCAQwOQLieC7HR4B0quCk7UXZ4kOMlGim3xr7Gi1MYaeyN9NN33VCXwPpc312x1nqS45-AmmiTih1POHo-FK_Rhy0LKh3K2lB5LcLrbL7xuisvij1iiTcSRbU_9zQMLNUbKO1O5qES5Gv2TT9eNDUnUOY9br-i6ReR5sFCrkvrdrDmPXASZAllCZeFQuYHN-xYzFq0-awAAAAE5wHsXAA)
    SPAMWATCH_API = None
    TOKEN = getenv("TOKEN", 6711858294:AAGJROErdJdL0TyunDI4dl-fuLKb1yK3nZc )
    OWNER_ID = int(getenv("OWNER_ID", "1668494031"))  # sᴛᴀʀᴛ @Exon_Robot ᴛʏᴘᴇ /id
    OWNER_USERNAME = getenv("OWNER_USERNAME", "prashant_sahlot")
    SUPPORT_CHAT = getenv("SUPPORT_CHAT", "AKATSUKI_OFFICIAL_0")
    LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001819078701"))
    MONGO_URI = getenv("MONGO_DB_URI")
    REDIS_URL = "redis://default:wK6ZCiclq4iQKYpgfY90v6kd6WdPfEwl@redis-10186.c263.us-east-1-2.ec2.cloud.redislabs.com:10186/default"
    DATABASE_URL = getenv("DATABASE_URL")

    # ɴᴏ ᴇᴅɪᴛ ᴢᴏɴᴇ
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
