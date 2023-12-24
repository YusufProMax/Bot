from aiogram import Bot
from data.config import channel
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types
from keyboards.inline.user import check_inline

async def check(user_id, channel_id):
    bot = Bot.get_current()
    member = await bot.get_chat_member(user_id=user_id, chat_id=channel_id)
    return member.is_chat_member()


class CheckSub(BaseMiddleware):
    async def on_pre_process_update(self, update: types.update, data: dict):
        user_id = 0
        if update.message:
            if update.message.text == "/start":
                return
            user_id = update.message.chat.id
        elif update.callback_query:
            if update.callback_query.data == "check":
                return
            user_id = update.callback_query.message.chat.id

        checker = await check(user_id=user_id, channel_id=-1001937623255)


        if not checker:
            text = "Kanalga a'zo bo'ling"
            await update.message.answer(text=text, reply_markup=check_inline)
            raise CancelHandler()
