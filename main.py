import asyncio
import logging
from aiogram import Bot

from bot_config import bot, dp
from handlers.start_handler import start_router
from handlers.joke_handler import joke_router
from handlers.weather_handler import weather_router
from handlers.currency_handler import currency_router
from handlers.movies_handler import movies_router
from handlers.poll_handler import poll_router

async def main():
    # Подключение всех роутеров
    dp.include_router(start_router)
    dp.include_router(joke_router)
    dp.include_router(weather_router)
    dp.include_router(currency_router)
    dp.include_router(movies_router)
    dp.include_router(poll_router)

    # Запуск бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())