from aiogram import Router, types
from aiogram.filters import Command

# Создание роутера
movies_router = Router()

# Обработчик команды /movies
@movies_router.message(Command("movies"))
async def process_command_movies(message: types.Message):
    await message.answer("Список фильмов: ...")
