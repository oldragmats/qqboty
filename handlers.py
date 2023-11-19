from aiogram import types
from aiogram.filters import CommandStart
from loader import dp

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    # Обработчик для команды /start
    await message.answer("Привет! Я бот(")

@dp.message()
async def echo(message: types.Message):
    # Обработчик для сообщений
    await message.answer(message.text)
