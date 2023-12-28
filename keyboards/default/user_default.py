from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


user_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👤 Profil"),
            KeyboardButton(text="🚀 Space Shop")
        ],
        [
            KeyboardButton(text="⏏️ Mening mahsulotlarim"),
            KeyboardButton(text="☎️ Aloqa")
        ]
    ], resize_keyboard=True
)



user_product_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⚜️ Mahsulot qo'shish"),
            KeyboardButton(text="⚜️ Mahsulotni o'chirish")
        ],
        [
            KeyboardButton(text="⬅️ Asosiy menyuga qaytish")
        ]
    ], resize_keyboard=True
)


product_status = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Active"),
            KeyboardButton(text="Inactive")
        ]
    ], resize_keyboard=True
)

user_phone_share = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="☎️ Telefon raqamni yuborish", request_contact=True)
        ]
    ], resize_keyboard=True
)

back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ortga")
        ]
    ], resize_keyboard=True
)

user_change_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Nomini"),
            KeyboardButton(text="Narxini")
        ],
        [
            KeyboardButton(text="Rasimini"),
            KeyboardButton(text="Tel raqamni")
        ]
    ], resize_keyboard=True
)
