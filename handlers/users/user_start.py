import types

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove
from utils.db_api.login_code import login_def
from utils.db_api.user_command import *
from keyboards.inline.user import *
from loader import dp
from states.user import RegisterState
from keyboards.default.user_default import *


@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    find_user = await get_user(chat_id=message.chat.id)
    if find_user:
        text = "Assalomu alaykum, xush kelibsiz"
        await message.answer(text=text, reply_markup=user_main_menu)
    else:
        text = "Assalomu alaykum, MARS SPACE ga kirish uchun modme_id ni kiritng : "
        await message.answer(text=text)
        await RegisterState.modme_id.set()


@dp.callback_query_handler(text="check")
async def check_handler(call: types.CallbackQuery):
    find_user = await get_user(chat_id=call.message.chat.id)
    if find_user:
        text = "Assalomu alaykum, xush kelibsiz"
        await call.message.answer(text=text, reply_markup=user_main_menu)
    else:
        text = "Assalomu alaykum, MARS SPACE ga kirish uchun modme_id ni kiritng : "
        await call.message.answer(text=text)


@dp.message_handler(state=RegisterState.modme_id)
async def get_full_name_handler(message: types.Message, state: FSMContext):
    await state.update_data(modme_id=message.text)
    text = "Parol ni kiriting"
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await RegisterState.login.set()


@dp.message_handler(state=RegisterState.login)
async def get_login_handler(message: types.Message, state: FSMContext):
    await state.update_data(login=message.text, chat_id=message.chat.id)
    data = await state.get_data()
    modme_id = data.get('modme_id')
    login = data.get('login')
    space_data = login_def(int(modme_id), login)
    if space_data:
        await state.update_data(first_name=space_data['first_name'], last_name=space_data['last_name'])
        data = await state.get_data()
        new_user = await add_user(data)
        if new_user:
            text = "Muvaffaqiyatli ro'yxatdan o'tdingiz ✅"
            await message.answer(text=text, reply_markup=user_main_menu)
            await state.finish()
        else:
            text = "Botda muammo mavjud ❌"
            await message.answer(text=text)
            await state.finish()
    else:
        text = "Siz kiritgan modme_id yoki parol xato. \n Qayta urinib ko'ring. \n modme_id ni kiriting: "
        await message.answer(text=text)
        await RegisterState.modme_id.set()
