# Домашнее задание по теме "Хендлеры обработки сообщений".
# Задача "Бот поддержки (Начало)":
import os
import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import  MemoryStorage
import asyncio
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

api = os.environ.get('API_KEY')

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

@dp.message_handler()
async def all_message(message):
    await message.answer("Введите команду /start чтобы начать общение.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


