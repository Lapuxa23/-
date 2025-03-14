from aiogram import Router, types
from aiogram.filters import Text

# Создание роутера
weather_router = Router()

# Обработчик inline-кнопки "Погода"
@weather_router.callback_query(Text('weather'))
async def process_callback_weather(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("Введите город:")