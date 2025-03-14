from aiogram import Router, types
from aiogram.filters import Text

# Создание роутера
poll_router = Router()

# Обработчик inline-кнопки "Опрос"
@poll_router.callback_query(Text('poll'))
async def process_callback_poll(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("Опрос: Как вас зовут?")