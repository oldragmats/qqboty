import asyncio
import logging
import sys

from aiogram import Bot
from aiogram.enums import ParseMode
from config import btoken
from loader import dp
from handlers import cmd_start, echo

async def main() -> None:
    dp.message.register(cmd_start)
    dp.message.register(echo)
    bot = Bot(token = btoken, parse_mode=ParseMode.HTML)
    await  dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

