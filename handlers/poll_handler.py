from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

# Создание роутера
poll_router = Router()


# Состояния опроса
class PollStates(StatesGroup):
    question1 = State()
    question2 = State()
    question3 = State()
    question4 = State()
    question5 = State()
    question6 = State()
    question7 = State()
    question8 = State()


# Обработчик команды /poll (начало опроса)
@poll_router.message(Command("poll"))
async def start_poll(message: types.Message, state: FSMContext):
    await message.answer("Опрос: Как вас зовут?")
    await state.set_state(PollStates.question1)


# Вопрос 1
@poll_router.message(PollStates.question1)
async def ask_question2(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("2) Сколько вам лет?")
    await state.set_state(PollStates.question2)


# Вопрос 2
@poll_router.message(PollStates.question2)
async def ask_question3(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("3) Какой ваш любимый школьный предмет?")
    await state.set_state(PollStates.question3)


# Вопрос 3
@poll_router.message(PollStates.question3)
async def ask_question4(message: types.Message, state: FSMContext):
    await state.update_data(subject=message.text)
    await message.answer("4) Какой ваш любимый цвет?")
    await state.set_state(PollStates.question4)


# Вопрос 4
@poll_router.message(PollStates.question4)
async def ask_question5(message: types.Message, state: FSMContext):
    await state.update_data(color=message.text)
    await message.answer("5) Какой ваш любимый фильм?")
    await state.set_state(PollStates.question5)


# Вопрос 5
@poll_router.message(PollStates.question5)
async def ask_question6(message: types.Message, state: FSMContext):
    await state.update_data(movie=message.text)
    await message.answer("6) Какой ваш любимый вид спорта?")
    await state.set_state(PollStates.question6)


# Вопрос 6
@poll_router.message(PollStates.question6)
async def ask_question7(message: types.Message, state: FSMContext):
    await state.update_data(sport=message.text)
    await message.answer("7) Какой ваш любимый жанр музыки?")
    await state.set_state(PollStates.question7)


# Вопрос 7
@poll_router.message(PollStates.question7)
async def ask_question8(message: types.Message, state: FSMContext):
    await state.update_data(music=message.text)
    await message.answer("8) Какой ваш любимый сезон года?")
    await state.set_state(PollStates.question8)


# Вопрос 8 (завершение опроса)
@poll_router.message(PollStates.question8)
async def finish_poll(message: types.Message, state: FSMContext):
    await state.update_data(season=message.text)
    data = await state.get_data()

    # Формируем итоговое сообщение
    result_text = (
        f"Ваши ответы:\n"
        f"1) Имя: {data.get('name')}\n"
        f"2) Возраст: {data.get('age')}\n"
        f"3) Любимый предмет: {data.get('subject')}\n"
        f"4) Любимый цвет: {data.get('color')}\n"
        f"5) Любимый фильм: {data.get('movie')}\n"
        f"6) Любимый вид спорта: {data.get('sport')}\n"
        f"7) Любимый жанр музыки: {data.get('music')}\n"
        f"8) Любимый сезон года: {data.get('season')}"
    )

    await message.answer(result_text)
    await state.clear()  # Сбрасываем состояние
