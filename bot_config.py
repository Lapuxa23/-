from aiogram import Bot, Dispatcher
from dotenv import dotenv_values
from database import create_tables, save_poll_result

# Загружаем токен бота из .env
config = dotenv_values(".env")

bot = Bot(token=config["BOT_TOKEN"])
dp = Dispatcher()

async def on_startup():
    """Функция запуска: создаем таблицы в БД"""
    await create_tables()
