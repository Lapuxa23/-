from aiogram import Router, types
from aiogram.filters import Text

# Создание роутера
movies_router = Router()

# Обработчик inline-кнопки "Список фильмов"
@movies_router.callback_query(Text('movies'))
async def process_callback_movies(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("Список фильмов: ...")