from aiogram import Router, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

# Создание роутера
start_router = Router()

# Обработчик команды /start
@start_router.message(Command('start'))
async def send_welcome(message: types.Message):
    name = message.from_user.first_name
    keyboard = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton(text="Картинка", callback_data="picture"),
        InlineKeyboardButton(text="Погода", callback_data="weather"),
        InlineKeyboardButton(text="Курс валют", callback_data="currency"),
        InlineKeyboardButton(text="Список фильмов", callback_data="movies"),
        InlineKeyboardButton(text="Шутка", callback_data="joke"),
        InlineKeyboardButton(text="Опрос", callback_data="poll")
    ]
    keyboard.add(*buttons)
    await message.reply(f"Привет, {name}! Выбери что-нибудь:", reply_markup=keyboard)