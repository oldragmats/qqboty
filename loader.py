from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode

from config import btoken

bot = Bot(btoken, parse_mode=ParseMode.HTML)
dp = Dispatcher(token = btoken, parse_mode=ParseMode.HTML)