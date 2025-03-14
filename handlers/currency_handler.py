from aiogram import Router, types
from aiogram.filters import Text

# Создание роутера
currency_router = Router()

# Обработчик inline-кнопки "Курс валют"
@currency_router.callback_query(Text('currency'))
async def process_callback_currency(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("Текущий курс валют: ...")