from aiogram import Router, types
from aiogram.filters import Command
import random  # Импортируем модуль random

# Создание роутера
movies_router = Router()

# Список из 20 популярных фильмов
popular_movies = [
    "Крестный отец (1972)",
    "Крестный отец 2 (1974)",
    "Темный рыцарь (2008)",
    "Побег из Шоушенка (1994)",
    "Список Шиндлера (1993)",
    "Властелин колец: Возвращение короля (2003)",
    "Форрест Гамп (1994)",
    "Начало (2010)",
    "Матрица (1999)",
    "Звездные войны: Эпизод V — Империя наносит ответный удар (1980)",
    "Титаник (1997)",
    "Интерстеллар (2014)",
    "Бойцовский клуб (1999)",
    "Гладиатор (2000)",
    "Пираты Карибского моря: Проклятие Черной жемчужины (2003)",
    "Гарри Поттер и Дары Смерти: Часть 2 (2011)",
    "Аватар (2009)",
    "Мстители: Финал (2019)",
    "Джокер (2019)",
    "Паразиты (2019)"
]


# Обработчик команды /movies
@movies_router.message(Command("movies"))
async def process_command_movies(message: types.Message):
    # Формируем список всех фильмов
    response_text = "Список популярных фильмов:\n\n"
    for i, movie in enumerate(popular_movies, start=1):
        response_text += f"{i}. {movie}\n"

    await message.answer(response_text)


# Обработчик команды /random_movie
@movies_router.message(Command("random_movie"))
async def process_command_random_movie(message: types.Message):
    # Выбираем случайный фильм из списка
    random_movie = random.choice(popular_movies)
    response_text = f" Случайный фильм:\n\n{random_movie}"

    await message.answer(response_text)