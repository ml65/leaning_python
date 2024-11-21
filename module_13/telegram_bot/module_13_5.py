# Домашнее задание по теме "Инлайн клавиатуры".

# Задача "Ещё больше выбора":

import os
import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import  MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from dotenv import load_dotenv

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

api = os.environ.get('API_KEY')

bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton( text = "Рассчитать" )
button2 = KeyboardButton( text = "Информация" )
kb.add(button, button2)

inline_kb = InlineKeyboardMarkup(resize_keyboard=True )
button3 = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data='calories')
button4 = InlineKeyboardButton(text="Формулы расчёта", callback_data='formulas')
inline_kb.add(button3, button4)

@dp.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=inline_kb )
    await message.answer()

@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb )

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer("1. Упрощенный вариант формулы Миффлина-Сан Жеора:\n\nдля мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;")

@dp.message_handler(text = 'Информация')
async def set_age(message):
    await message.answer("Информация о боте:")

@dp.callback_query_handler(text = 'calories')
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    await message.answer(callories_calculate(data))

def callories_calculate(data):
    if not isint(data['age'] or not isint(data['growth']) or not isint(data['weight'])):
        return f"Введены ошибочные данные. возраст={data['age']} рост={data['growth']} вес={data['weight']}"
    else:
        age    = int(data['age'])
        growth = int(data['growth'])
        weight = int(data['weight'])
        return f"Ваша норма калорий {10 * weight + 6.25 * growth - 5 * age + 5}"

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

