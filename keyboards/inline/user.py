from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


check_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardMarkup(text="Kanalga a'zo bo'lish ➕", url='https://t.me/asd6099')
        ],
        [
            InlineKeyboardButton(text="Tekshirish ✅", callback_data='check')
        ]
    ]
)