from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    sex = State()
    age = State()
    growth = State()
    weight = State()



@dp.message_handler(commands=['start'])
async def start_message(message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler(text=["калории"])
async def set_age(message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_sex(message, state):
    await state.update_data(age=message.text)
    await message.answer("Укажите свой пол(м или ж):")
    await UserState.sex.set()


@dp.message_handler(state=UserState.sex)
async def set_growth(message, state):
    await state.update_data(sex=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    global calories
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    growth = float(data['growth'])
    weight = float(data['weight'])
    sex = data.get('sex').lower()
    if sex == 'м':
        calories = (10 * weight) + (6.25 * growth) - (5 * age) + 5
    elif sex == 'ж':
        calories = (10 * weight) + (6.25 * growth) - (5 * age) - 161
    else:
        await message.answer('Некоректно указан пол,пожалуйста повторите попытку!')
    await message.answer(f'Ваша норма каллорий: {calories} ккал')
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
