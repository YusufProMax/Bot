from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterState(StatesGroup):
    modme_id = State()
    login = State()


class SpaceProduct(StatesGroup):
    product_name = State()
    product_price = State()
    product_photo = State()
    description = State()
    contact = State()