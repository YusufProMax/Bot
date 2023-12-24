from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterState(StatesGroup):
    modme_id = State()
    login = State()


class SpaceProduct(StatesGroup):
    product_name = State()
    product_price = State()
    product_photo = State()
    description = State()
    status = State()
    contact = State()



class ChangeName(StatesGroup):
    id = State()
    chat_id = State()
    new_name = State()

class ChangePrice(StatesGroup):
    id = State()
    chat_id = State()
    new_price = State()

class ChangePhoto(StatesGroup):
    id = State()
    chat_id = State()
    new_photo = State()

class ChangeContact(StatesGroup):
    id = State()
    chat_id = State()
    new_contact = State()