from aiogram import Router, types
from aiogram.filters import Command

# Создание роутера
poll_router = Router()


# Обработчик команды /poll
@poll_router.message(Command("poll"))
async def process_command_poll(message: types.Message):
    await message.answer("Опрос: Как вас зовут?")
