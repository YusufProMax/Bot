from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


check_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardMarkup(text="Kanalga a'zo bo'lish ➕", url='https://t.me/asd603309')
        ],
        [
            InlineKeyboardButton(text="Tekshirish ✅", callback_data='check')
        ]
    ]
)



async def product_pagination(index, total_products):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Ortga", callback_data="back"),
                InlineKeyboardButton(text=f"{index + 1}/{total_products}", callback_data="show"),
                InlineKeyboardButton(text="Keyingi", callback_data="next")
            ]
        ]
    )
    return markup