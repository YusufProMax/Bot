from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from loader import dp
from aiogram import types
from utils.db_api.user_command import *
from keyboards.default.user_default import *
from states.user import *

@dp.message_handler(text="⚜️ Mahsulotni o'chirish")
async def product_delete_handler(message: types.Message, state: FSMContext):
    text = "Mahsulot id sini kiriting"
    await message.answer(text=text)
    await state.set_state("user-product-delete-state")


@dp.message_handler(state="user-product-delete-state")
async def product_delete_handler2(message: types.Message, state: FSMContext):
    product_id = message.text
    chat_id = message.chat.id
    deleted = await delete_product(chat_id=chat_id, product_id=product_id)
    if deleted:
        text = "Mahsulot muvaffaqiyatli o'chirildi ✅"
    else:
        text = "Botda muammo mavjud ❌"
    await message.answer(text=text, reply_markup=user_main_menu)
    await state.finish()


