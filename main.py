import asyncio
import logging
import requests

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TG_TOKEN = 'none'
WG_TOKEN = 'none'

bot = Bot(token=TG_TOKEN, parse_mode='HTML')
dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(
        f'{message.from_user.first_name}, you are <b>BLACK!</b> btw send nickname to get statistics in WoT')


@dp.message()
async def send_stats(message: types.Message):
    await message.answer(f'{get_stats(message.text)}')


def get_stats(username):
    try:
        username_response = requests.get(
            f'https://api.worldoftanks.eu/wot/account/list/?application_id={WG_TOKEN}&search={username}')
        username_data = username_response.json()
        account_id = username_data['data'][0]['account_id']

        stats_response = requests.get(
            f'https://api.worldoftanks.eu/wot/account/info/?application_id={WG_TOKEN}&account_id={account_id}')
        stats_data = stats_response.json()
        stats = stats_data['data'][str(account_id)]['statistics']['all']

        clan_response = requests.get(
            f'https://api.worldoftanks.eu/wot/clans/accountinfo/?application_id={WG_TOKEN}&account_id={account_id}')
        clan_data = clan_response.json()
        clan_name = clan_data['data'][str(account_id)]['clan']['tag']

        if stats['wins'] / stats['battles'] * 100 >= 50:
            message = (f"<b>Статистика гравця</b> <i>{username_data['data'][0]['nickname']}</i>\n"
                       f"<b>Клан:</b> {clan_name}\n"
                       f"<b>Кількість боїв:</b> {stats['battles']}\n"
                       f"<b>% перемог:</b> {stats['wins'] / stats['battles'] * 100:.2f}%\n"
                       f"<b>% влучень:</b> {stats['hits'] / stats['shots'] * 100:.2f}%\n"
                       f"<b>Середня шкода:</b> {stats['damage_dealt'] / stats['battles']:.2f}\n"
                       f"<b>Середній досвід:</b> {stats['xp'] / stats['battles']:.2f}\n"
                       f"<b>Максимум знищено за бій:</b> {stats['max_frags']}\n"
                       f"<b>Максимальний досвід за бій:</b> {stats['max_xp']}\n")

        else:
            message = 'YOU ARE RAK!🤣🤣🤣 low winrate'

        return message

    except:
        return "This is SHIT!"


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
