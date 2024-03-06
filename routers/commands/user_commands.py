import requests
from aiogram import Router, types
from aiogram.filters import Command

import config

router = Router()


@router.message(Command("stat"))
async def handle_player_stats(message: types.Message):
    # Розділити текст повідомлення на слова
    command, *arguments = message.text.split()

    # Перевірити, чи є аргументи
    if arguments:
        # Викликати get_stats та передати перший аргумент (нікнейм гравця)
        result = get_stats(arguments[0])
        await message.answer(f'{result}', parse_mode='HTML')


def get_stats(username):
    try:
        username_response = requests.get(
            f'https://api.worldoftanks.eu/wot/account/list/?application_id={config.WG_TOKEN}&search={username}')
        username_data = username_response.json()
        account_id = username_data['data'][0]['account_id']

        stats_response = requests.get(
            f'https://api.worldoftanks.eu/wot/account/info/?application_id={config.WG_TOKEN}&account_id={account_id}')
        stats_data = stats_response.json()
        stats = stats_data['data'][str(account_id)]['statistics']['all']

        clan_response = requests.get(
            f'https://api.worldoftanks.eu/wot/clans/accountinfo/?application_id={config.WG_TOKEN}&account_id={account_id}')
        clan_data = clan_response.json()
        clan_name = clan_data['data'][str(account_id)]['clan']['tag']

        message = (f"<b>Статистика гравця</b> <i>{username_data['data'][0]['nickname']}</i>\n"
                   f"<b>Клан:</b> {clan_name}\n"
                   f"<b>Кількість боїв:</b> {stats['battles']}\n"
                   f"<b>% перемог:</b> {stats['wins'] / stats['battles'] * 100:.2f}%\n"
                   f"<b>% влучень:</b> {stats['hits'] / stats['shots'] * 100:.2f}%\n"
                   f"<b>Середня шкода:</b> {stats['damage_dealt'] / stats['battles']:.2f}\n"
                   f"<b>Середній досвід:</b> {stats['xp'] / stats['battles']:.2f}\n"
                   f"<b>Максимум знищено за бій:</b> {stats['max_frags']}\n"
                   f"<b>Максимальний досвід за бій:</b> {stats['max_xp']}\n")

        return message

    except:
        return "Nickname not found :/"
