from typing import Optional

from pyrogram import Client
from config import LOG_GROUP_ID

S12KK = {}
pause = {}
mute = {}
active = []


class VClient(Client):
    def __init__(self, name, *args, **kwargs):
        super().__init__(name, *args, **kwargs)


class MelodyError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def S12K(chat_id: Optional[int] = None):
    if chat_id is not None:
        S12KK[1234] = chat_id
    return S12KK.get(1234) or LOG_GROUP_ID


async def is_music_playing(chat_id: int) -> bool:
    mode = pause.get(chat_id)
    if not mode:
        return False
    return mode


async def music_on(chat_id: int):
    pause[chat_id] = True


async def music_off(chat_id: int):
    pause[chat_id] = False


async def is_muted(chat_id: int) -> bool:
    mode = mute.get(chat_id)
    if not mode:
        return False
    return mode


async def mute_on(chat_id: int):
    mute[chat_id] = True


async def mute_off(chat_id: int):
    mute[chat_id] = False


async def get_active_chats() -> list:
    return active


async def is_active_chat(chat_id: int) -> bool:
    if chat_id not in active:
        return False
    else:
        return True


async def add_active_chat(chat_id: int):
    if chat_id not in active:
        active.append(chat_id)


async def remove_active_chat(chat_id: int):
    if chat_id in active:
        active.remove(chat_id)
