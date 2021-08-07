import importlib
import logging
import os
import sys
from pathlib import Path

from userbot.var import Var

from .. import *
from ..config import *
from ..helpers import *
from ..helpers.progress import *
from . import *
from .assistant_load import *
from .decorators import *
from .errors import *
from .extras import *
from .funcs import *

# ENV
ENV = bool(os.environ.get("ENV", False))
if ENV:
    from userbot.config import Config
else:
    if os.path.exists("Config.py"):
        from userbot.AndencentoConfig import Development as Config


# load plugins
def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import userbot.utils

        path = Path(f"plugins/{shortname}.py")
        name = "plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("Successfully imported " + shortname)
    else:
        import userbot.utils

        path = Path(f"plugins/{shortname}.py")
        name = "plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.Andencento = Andencento
        mod.bot = Andencento
        mod.delete_hell = delete
        mod.eod = delete
        mod.admin_cmd = admin_cmd
        mod.Var = Var
        mod.Var = Config
        mod.andencento_cmd = andencento_cmd
        mod.command = command
        mod.logger = logging.getLogger(shortname)
        mod.extremepro_cmd = admin_cmd
        mod.amanpandey_cmd = sudo_cmd
        mod.asst = asst
        mod.asstcmd = Andencento.tgbot
        mod.LOGS = LOGS
        mod.tgbot = Andencento.tgbot
        mod.sudo_cmd = sudo_cmd
        sys.modules["userbot"] = userbot
        sys.modules["var"] = userbot.var
        sys.modules["config"] = userbot.config
        sys.modules["Config"] = userbot.AndencentoConfig
        sys.modules["userbot.utils"] = userbot.utils
        sys.modules["Extre.events"] = userbot.utils
        sys.modules["userbot.events"] = userbot.utils
        sys.modules["ULTRA.utils"] = userbot.utils
        sys.modules["userbot.Config"] = userbot.config
        sys.modules["userbot.uniborConfig"] = userbot.config
        sys.modules["ub"] = userbot
        sys.modules["jarvis"] = userbot
        sys.modules["support"] = userbot
        sys.modules["userbot"] = userbot
        sys.modules["telebot"] = userbot
        sys.modules["fridaybot"] = userbot
        sys.modules["jarvis.utils"] = userbot.utils
        sys.modules["uniborg.util"] = userbot.utils
        sys.modules["teleAndencento.utils"] = userbot.utils
        sys.modules["userbot.utils"] = userbot.utils
        sys.modules["userbot.events"] = userbot.utils
        sys.modules["jarvis.jconfig"] = userbot.config
        sys.modules["userbot.config"] = userbot.config
        sys.modules["fridayAndencento.utils"] = userbot.utils
        sys.modules["fridayAndencento.Config"] = userbot.config
        sys.modules["userbot.uniborgConfig"] = userbot.config
        mod.edit_or_reply = edit_or_reply
        mod.logger = logging.getLogger(shortname)
        # support for uniborg
        sys.modules["uniborg.util"] = userbot.utils
        mod.Config = Config
        mod.borg = Andencento
        mod.edit_or_reply = edit_or_reply
        mod.eor = edit_or_reply
        # support for paperplaneextended
        sys.modules["userbot.mainfiles.events"] = userbot.utils
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["plugins." + shortname] = mod
        LOGS.info("ANDENCENTO imported " + shortname)

def extra(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import userbot.utils

        path = Path(f"Addons-Andencento/{shortname}.py")
        name = "Addons-Andencento.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("Successfully imported " + shortname)
    else:
        import userbot.utils

        path = Path(f"Addons-Andencento/{shortname}.py")
        name = "Addons-Andencento.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.Andencento = Andencento
        mod.bot = Andencento
        mod.delete_hell = delete
        mod.eod = delete
        mod.admin_cmd = admin_cmd
        mod.Var = Var
        mod.command = command
        mod.logger = logging.getLogger(shortname)
        mod.extremepro_cmd = admin_cmd
        mod.amanpandey_cmd = sudo_cmd
        mod.LOGS = LOGS
        mod.tgbot = Andencento.tgbot
        mod.sudo_cmd = sudo_cmd
        sys.modules["userbot"] = userbot
        sys.modules["userbot.utils"] = userbot.utils
        sys.modules["Extre.events"] = userbot.utils
        sys.modules["userbot.events"] = userbot.utils
        sys.modules["ULTRA.utils"] = userbot.utils
        sys.modules["userbot.Config"] = userbot.config
        sys.modules["userbot.uniborConfig"] = userbot.config
        sys.modules["ub"] = userbot
        sys.modules["jarvis"] = userbot
        sys.modules["support"] = userbot
        sys.modules["userbot"] = userbot
        sys.modules["teleAndencento"] = userbot
        sys.modules["fridayAndencento"] = userbot
        sys.modules["jarvis.utils"] = userbot.utils
        sys.modules["uniborg.util"] = userbot.utils
        sys.modules["teleAndencento.utils"] = userbot.utils
        sys.modules["userbot.utils"] = userbot.utils
        sys.modules["userbot.events"] = userbot.utils
        sys.modules["jarvis.jconfig"] = userbot.config
        sys.modules["userbot.config"] = userbot.config
        sys.modules["fridayAndencento.utils"] = userbot.utils
        sys.modules["fridayAndencento.Config"] = userbot.config
        sys.modules["userbot.uniborgConfig"] = userbot.config
        mod.edit_or_reply = edit_or_reply
        mod.logger = logging.getLogger(shortname)
        # support for uniborg
        sys.modules["uniborg.util"] = userbot.utils
        mod.Config = Config
        mod.borg = Andencento
        mod.edit_or_reply = edit_or_reply
        mod.eor = edit_or_reply
        # support for paperplaneextended
        sys.modules["userbot.mainfiles.events"] = userbot.utils
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["Addons-Andencento." + shortname] = mod
        LOGS.info("Addons-Andencento imported " + shortname)


def remove_plugin(shortname):
    try:
        try:
            for i in LOAD_PLUG[shortname]:
                Andencento.remove_event_handler(i)
            del LOAD_PLUG[shortname]

        except BaseException:
            name = f"plugins.{shortname}"

            for i in reversed(range(len(Andencento._event_builders))):
                ev, cb = Andencento._event_builders[i]
                if cb.__module__ == name:
                    del Andencento._event_builders[i]
    except BaseException:
        raise ValueError
