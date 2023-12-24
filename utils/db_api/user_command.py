from main.database_set import database
from main.models import *

async def get_user(chat_id: int):
    try:
        query = users.select().where(users.c.chat_id == chat_id)
        user = await database.fetch_one(query=query)
        return user
    except Exception as exc:
        print(exc)
        return False


async def add_user(data: dict):
    try:
        query = users.insert().values(
            modme_id=int(data.get('modme_id')),
            login=data.get('login'),
            first_name=data.get('last_name'),
            last_name=data.get('first_name'),
            chat_id=data.get('chat_id')
        )
        new_user = await database.execute(query=query)
        return new_user
    except Exception as exc:
        print(exc)
        return False



async def add_product(product_data: dict):
    try:
        query = space_shop.insert().values(
            product_name=product_data.get('product_name'),
            product_price=int(product_data.get('product_price')),
            product_photo=product_data.get('product_photo'),
            description=product_data.get('description'),
            contact=product_data.get('contact'),
            status=product_data.get('status'),
            chat_id=product_data.get('chat_id')
        )
        new_product = await database.execute(query=query)
        return new_product
    except Exception as exc:
        print(exc)
        return False



async def get_my_products(chat_id: int):
    try:
        query = space_shop.select().where(space_shop.c.chat_id==chat_id)
        product = await database.fetch_all(query=query)
        return product
    except Exception as exc:
        print(exc)
        return False


async def get_all_products():
    try:
        query = space_shop.select().where(space_shop.c.status=="Active")
        products = await database.fetch_all(query=query)
        return products
    except Exception as exc:
        print(exc)
        return False


async def delete_product(chat_id: int, product_id: int):
    try:
        query = space_shop.delete().where(space_shop.c.id == int(product_id), space_shop.c.chat_id == chat_id)
        await database.execute(query=query)
        return True
    except Exception as exc:
        print(exc)
        return False

async def product_change_name(data: dict):
    try:
        query = space_shop.update().values(
            space_shop.c.product_name == data.get('new_name')).where(
            space_shop.c.id == int(data.get('product_id')), space_shop.c.chat_id == int(data.get('chat_id'))
        )
        await database.execute(query=query)
        return True
    except Exception as exc:
        print(exc)
        return False


async def product_change_price(data: dict):
    try:
        query = space_shop.update().values(
            space_shop.c.product_price == int(data.get('new_price'))).where(
            space_shop.c.id == int(data.get('product_id')), space_shop.c.chat_id == int(data.get('chat_id'))
        )
        await database.execute(query=query)
        return True
    except Exception as exc:
        print(exc)
        return False


async def product_change_photo(data: dict):
    try:
        query = space_shop.update().values(
            space_shop.c.product_photo == data.get('new_photo')).where(
            space_shop.c.id == int(data.get('product_id')), space_shop.c.chat_id == int(data.get('chat_id'))
        )
        await database.execute(query=query)
        return True
    except Exception as exc:
        print(exc)
        return False


async def product_change_contact(data: dict):
    try:
        query = space_shop.update().values(
            space_shop.c.contact == data.get('new_contact')).where(
            space_shop.c.id == int(data.get('product_id')), space_shop.c.chat_id == int(data.get('chat_id'))
        )
        await database.execute(query=query)
        return True
    except Exception as exc:
        print(exc)
        return False