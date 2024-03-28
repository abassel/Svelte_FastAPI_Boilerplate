import logging
import os

logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class DevConfig:
    DEBUG = True

    # WEATHER API CONFIG
    WEATHER_API_KEY = os.getenv('WEATHER_API_KEY').strip()
    CACHE_TTL_SECONDS = 10

    # LOG
    LOG_LEVEL = logging.DEBUG
    LOG_FORMAT = f"%(asctime)s [%(process)d] [%(levelname)s] [%(filename)s:%(lineno)d] -> %(message)s"
    LOG_DATEFMT = "[%y-%m-%d %H:%M:%S %z]"


class ProdConfig(DevConfig):
    DEBUG = False

    # WEATHER API CONFIG
    CACHE_TTL_SECONDS = 900


def auto_config():
    log = logging.getLogger()

    cfg = ProdConfig()

    # if running on a mac, use
    if os.getenv('DEV', None):
        cfg = DevConfig()

    log.warning(f">>>> Using configuration {cfg.__class__.__name__}")
    return cfg


app_config = auto_config()

logging.basicConfig(datefmt=app_config.LOG_DATEFMT, format=app_config.LOG_FORMAT, level=app_config.LOG_LEVEL)
LOG = logging.getLogger()
