import aiohttp
import os
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from aiogram.filters.command import Command
from dotenv import load_dotenv

load_dotenv()

# Создание роутера
weather_router = Router()


# Состояния для FSM
class WeatherState(StatesGroup):
    waiting_for_city = State()


# Обработчик inline-кнопки "Погода"
@weather_router.callback_query(Command('weather'))
async def process_callback_weather(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await callback_query.message.answer("Введите город:")
    await state.set_state(WeatherState.waiting_for_city)


# Обработчик ввода города
@weather_router.message(WeatherState.waiting_for_city)
async def get_weather(message: Message, state: FSMContext):
    city = message.text
    api_key = os.getenv("WEATHER_API_KEY")  # API-ключ из переменных окружения

    if not api_key:
        await message.answer("Ошибка: API-ключ для погоды не найден.")
        await state.clear()
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
                temp = data["main"]["temp"]
                description = data["weather"][0]["description"]
                await message.answer(f"Погода в {city}: {temp}°C, {description.capitalize()}")
            else:
                await message.answer("Город не найден. Попробуйте снова.")

    await state.clear()  # Сбрасываем состояние
