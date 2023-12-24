from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from loader import dp
from aiogram import types
from utils.db_api.user_command import get_user, add_product, get_my_products, get_all_products, delete_product
from keyboards.default.user_default import *
from states.user import SpaceProduct


@dp.message_handler(text="👤 Profil")
async def profile_handler(message: types.Message):
    user_info = await get_user(chat_id=message.chat.id)
    text_user = f"""
⚜️ Ism: {user_info['first_name']} \n
⚜️ Familiya: {user_info['last_name']} \n
⚜️ Modme_id: {user_info['modme_id']}
"""
    await message.answer(text=text_user)


@dp.message_handler(text="⏏️ Mening mahsulotlarim")
async def my_products_handler(message: types.Message):
    my_products = await get_my_products(chat_id=message.chat.id)
    if my_products:
        for product in my_products:
            text = (f"Id | {product['id']} \n"
                    f"⚜️ Nomi: {product['product_name']} \n"
                    f"⚜️ Narxi: {product['product_price']} \n"
                    f"⚜️ About: {product['description']} \n"
                    f"⚜️ Status: {product['status']}")
            await message.answer_photo(photo=product['product_photo'], caption=text, reply_markup=user_product_menu)
    else:
        text = "Siz xali beri mahsulot qo'shmagansiz"
        await message.answer(text=text, reply_markup=user_product_menu)


# ADD PRODUCT



@dp.message_handler(text="⚜️ Mahsulot qo'shish")
async def add_product_handler(message: types.Message):
    text = "Mahsulot nomini kiriting: "
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await SpaceProduct.product_name.set()


@dp.message_handler(state=SpaceProduct.product_name)
async def get_product_handler(message: types.Message, state: FSMContext):
    await state.update_data(product_name=message.text)
    text = "Mahsulot narxini kiriting: "
    await message.answer(text=text)
    await SpaceProduct.product_price.set()


@dp.message_handler(state=SpaceProduct.product_price)
async def get_product_handler(message: types.Message, state: FSMContext):
    await state.update_data(product_price=message.text)
    text = "Mahsulot rasmini kiriting: "
    await message.answer(text=text)
    await SpaceProduct.product_photo.set()


@dp.message_handler(state=SpaceProduct.product_photo, content_types=types.ContentType.PHOTO)
async def get_product_handler(message: types.Message, state: FSMContext):
    await state.update_data(product_photo=message.photo[-1].file_id)
    text = "Mahsulot xaqida biror narsa kiriting: "
    await message.answer(text=text)
    await SpaceProduct.description.set()

@dp.message_handler(state=SpaceProduct.description)
async def get_product_handler(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    text = "Siz bilan bog'lanish uchun telefon raqamingizni jo'nating: \n(Pastdagi tugamadan foydalaning) "
    await message.answer(text=text, reply_markup=user_phone_share)
    await SpaceProduct.contact.set()

@dp.message_handler(state=SpaceProduct.contact, content_types=types.ContentType.CONTACT)
async def get_number_handler(message: types.Message, state: FSMContext):
    await state.update_data(contact=message.contact.phone_number)
    text = "Mahsulot statusini kiriting:"
    await message.answer(text=text, reply_markup=product_status)
    await SpaceProduct.status.set()

@dp.message_handler(state=SpaceProduct.status)
async def get_product_handler(message: types.Message, state: FSMContext):
    await state.update_data(status=message.text, chat_id=message.chat.id)
    product_data = await state.get_data()
    new_product = await add_product(product_data)
    if new_product:
        text = "Mahsulot muvaffaqiyatli qo'shildi ✅"
    else:
        text = "Botda muammo mavjud ❌"
    await message.answer(text=text, reply_markup=user_product_menu)
    await state.finish()


# BACK

@dp.message_handler(text="⬅️ Asosiy menyuga qaytish")
async def back_handler(message: types.Message):
    text = "Asosiy menyu"
    await message.answer(text=text, reply_markup=user_main_menu)
    

@dp.message_handler(text="🚀 Space Shop")
async def my_products_handler(message: types.Message):
    all_products = await get_all_products()
    if all_products:
        for product in all_products:
            text = (f"⚜️ Nomi: {product['product_name']} \n"
                    f"⚜️ Narxi: {product['product_price']} \n"
                    f"⚜️ About: {product['description']} \n"
                    f"⚜️ Aloqa uchun: {product['contact']}")
            await message.answer_photo(photo=product['product_photo'], caption=text, reply_markup=user_main_menu)
    else:
        text = "Space Shopda xali tovarlar mavjud emas"
        await message.answer(text=text, reply_markup=user_main_menu)



