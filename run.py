import logging

import keyboard
import mouse

FORMAT = "%(asctime)s | %(levelname)s | %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger("D2Simplified")

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


def simplify(skill: dict):
    mouse.click(skill["binding"])
    logger.info(f"Simplifying: {skill['key']}, {skill['binding']}")


if __name__ in "__main__":
    setup_key_bindings()
    keyboard.wait()
