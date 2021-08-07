import os

ENV = bool(os.environ.get("ENV", False))

if ENV:
    from .config import Config
else:
    if os.path.exists("config.py"):
        from userbot.config import Development as Config
