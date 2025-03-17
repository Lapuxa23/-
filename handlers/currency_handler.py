from aiogram import Router, types
from aiogram.filters import Command

# Создание роутера
currency_router = Router()

# Обработчик команды /currency
@currency_router.message(Command("currency"))
async def process_command_currency(message: types.Message):
    await message.answer("Текущий курс валют: ...")
