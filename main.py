import asyncio
import logging

import config

from aiogram import Bot, Dispatcher
from routers import router as main_router

dp = Dispatcher()

dp.include_router(main_router)


# @dp.message(Command("stat"))
# async def handle_player_stats(message: types.Message):
#    await message.answer(f'{get_stats(message.text)}', parse_mode='HTML')


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.TG_TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
