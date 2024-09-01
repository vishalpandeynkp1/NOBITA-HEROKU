import asyncio

from pyrogram import idle
from Vivek import app, call


async def main():

    await app.start()
    await app.import_all_module()
    awaut call.start()

    await idle()

    await app.stop()
    await call.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(main())