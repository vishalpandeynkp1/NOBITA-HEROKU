import asyncio

from pyrogram import idle
#from Vivek import app
from Vivek.core.clients import Vivek
from Vivek.core.pytgcall import call, app

async def main():

    await app.start()
    await Vivek().import_all_module()

    await idle()

    await app.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(main())