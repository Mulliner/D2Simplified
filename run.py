import logging
import time

import keyboard
import mouse

from state import state

FORMAT = "%(asctime)s | %(levelname)s | %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger("D2Simplified")

last_clicked = None

keybinds = [
    {"key": "F1", "binding": mouse.RIGHT},
    {"key": "F2", "binding": mouse.LEFT},
    {"key": "F3", "binding": mouse.RIGHT},
    {"key": "F4", "binding": mouse.RIGHT},
    {"key": "F5", "binding": mouse.RIGHT},
    {"key": "F6", "binding": mouse.RIGHT},
    {"key": "F7", "binding": mouse.RIGHT},
    {"key": "F8", "binding": mouse.RIGHT},
]


def setup_key_bindings():
    for keybinding in keybinds:
        keyboard.add_hotkey(keybinding["key"], simplify, args=(keybinding,))
        logger.info(f"Hotkey `{keybinding['key']}` bound to `{keybinding['binding']}`")


def simplify(binding: dict):
    if state.last_clicked == binding["key"]:
        state.last_clicked = binding["key"]
        time.sleep(0.01)
    state.last_clicked = binding["key"]
    mouse.click(binding["binding"])
    logger.info(f"Simplifying: {binding['key']}, {binding['binding']}")


if __name__ in "__main__":
    setup_key_bindings()
    keyboard.wait()
