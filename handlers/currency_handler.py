from aiogram import Router, types
from aiogram.filters import Command
import aiohttp
import json

# Создание роутера
currency_router = Router()


# Функция для получения курса валют
async def get_currency_rates():
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.text()
                return json.loads(data)
            else:
                return None


# Обработчик команды /currency
@currency_router.message(Command("currency"))
async def process_command_currency(message: types.Message):
    rates = await get_currency_rates()
    if rates:
        usd_rate = rates['Valute']['USD']['Value']
        eur_rate = rates['Valute']['EUR']['Value']
        response_text = f"Текущий курс валют:\nUSD: {usd_rate} RUB\nEUR: {eur_rate} RUB"
    else:
        response_text = "Не удалось получить курс валют. Попробуйте позже."

    await message.answer(response_text)