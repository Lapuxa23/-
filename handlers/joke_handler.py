from aiogram import Router, types, F
from aiogram.filters import Command
import aiohttp

# Создание роутера
joke_router = Router()

# Обработчик inline-кнопки "Шутка"
@joke_router.callback_query(F.data == "joke")  # Используем фильтр данных
async def process_callback_joke(callback_query: types.CallbackQuery):
    await callback_query.answer()
    async with aiohttp.ClientSession() as session:
        async with session.get('https://v2.jokeapi.dev/joke/Any?type=single') as resp:
            if resp.status == 200:
                joke_data = await resp.json()
                joke = joke_data.get('joke', 'Шутка не найдена')
                await callback_query.message.answer(joke)
            else:
                await callback_query.message.answer("Не удалось получить шутку.")
