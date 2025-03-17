from aiogram import Router, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile
from aiogram.filters import Command
from aiogram import Dispatcher, Bot
import asyncio
import os

# Импортируем роутеры из файла routers.py (если они есть)
# from routers import currency_router, movies_router, joke_router

# Создание роутера для команды /start
start_router = Router()

# Путь к папке с изображениями
IMAGES_DIR = "images"

# Обработчик команды /start
@start_router.message(Command('start'))
async def send_welcome(message: types.Message):
    name = message.from_user.first_name

    # Создание inline-клавиатуры
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Картинка", callback_data="picture"),
         InlineKeyboardButton(text="Погода", callback_data="weather")],
        [InlineKeyboardButton(text="Курс валют", callback_data="currency"),
         InlineKeyboardButton(text="Список фильмов", callback_data="movies")],
        [InlineKeyboardButton(text="Шутка", callback_data="joke"),
         InlineKeyboardButton(text="Опрос", callback_data="poll")]
    ])

    await message.reply(f"Привет, {name}! Выбери что-нибудь:", reply_markup=keyboard)

# Обработчик для кнопки "Картинка"
@start_router.callback_query(F.data == "picture")
async def send_picture(callback: types.CallbackQuery):
    # Получаем список файлов в папке images
    images = os.listdir(IMAGES_DIR)
    if images:
        # Выбираем случайное изображение
        random_image = os.path.join(IMAGES_DIR, random.choice(images))
        # Отправляем изображение
        photo = FSInputFile(random_image)
        await callback.message.answer_photo(photo, caption="Вот тебе картинка! 🖼️")
    else:
        await callback.message.answer("Картинки не найдены 😢")
    await callback.answer()  # Завершаем callback

# Обработчик для кнопки "Погода"
@start_router.callback_query(F.data == "weather")
async def send_weather(callback: types.CallbackQuery):
    await callback.message.answer("Погода сегодня: солнечно! ☀️")
    await callback.answer()

# Обработчик для кнопки "Курс валют"
@start_router.callback_query(F.data == "currency")
async def send_currency(callback: types.CallbackQuery):
    await callback.message.answer("Текущий курс валют: 1 USD = 90 RUB, 1 EUR = 100 RUB")
    await callback.answer()

# Обработчик для кнопки "Список фильмов"
@start_router.callback_query(F.data == "movies")
async def send_movies(callback: types.CallbackQuery):
    movies = [
        "1. Крестный отец (1972)",
        "2. Темный рыцарь (2008)",
        "3. Побег из Шоушенка (1994)",
        "4. Начало (2010)",
        "5. Форрест Гамп (1994)"
    ]
    await callback.message.answer("Список популярных фильмов:\n\n" + "\n".join(movies))
    await callback.answer()

# Обработчик для кнопки "Шутка"
@start_router.callback_query(F.data == "joke")
async def send_joke(callback: types.CallbackQuery):
    await callback.message.answer("Шутка: Почему программисты путают Хэллоуин и Рождество? Потому что Oct 31 == Dec 25! 😄")
    await callback.answer()

# Обработчик для кнопки "Опрос"
@start_router.callback_query(F.data == "poll")
async def send_poll(callback: types.CallbackQuery):
    await callback.message.answer_poll(
        question="Какой ваш любимый жанр фильмов?",
        options=["Комедия", "Драма", "Боевик", "Фантастика"],
        is_anonymous=False
    )
    await callback.answer()
