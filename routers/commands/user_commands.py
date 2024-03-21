import requests
from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config

router = Router()


# Handlers
@router.message(Command("stat"))
async def handle_player_stats(message: types.Message):
    command, *arguments = message.text.split()

    if arguments:
        await message.reply(f'{get_stats(arguments[0])}',
                            parse_mode=ParseMode.HTML
                            )
    else:
        await message.reply("❗️ /stat [ім'я гравця] ❗️️")


# Logic
@router.message(Command("clan"))
async def handle_clan_info(message: types.Message):
    command, *arguments = message.text.split()

    if arguments:
        await message.reply(
            f'{get_clan(arguments[0])}',
            parse_mode=ParseMode.HTML
        )
    else:
        await message.reply("❗️ /clan [назва клану] ❗️️")


def get_stats(username):
    try:
        username_response = requests.get(
            f'https://api.worldoftanks.eu/wot/account/list/?application_id={config.WG_TOKEN}&search={username}'
        )
        username_data = username_response.json()
        account_id = username_data['data'][0]['account_id']

        stats_response = requests.get(
            f'https://api.worldoftanks.eu/wot/account/info/?application_id={config.WG_TOKEN}&account_id={account_id}'
        )
        stats_data = stats_response.json()
        stats = stats_data['data'][str(account_id)]['statistics']['all']

        clan_response = requests.get(
            f'https://api.worldoftanks.eu/wot/clans/accountinfo/?application_id={config.WG_TOKEN}&account_id={account_id}'
        )
        clan_data = clan_response.json()
        try:
            clan_name = clan_data['data'][str(account_id)]['clan']['tag']
        except (KeyError, TypeError):
            clan_name = "не в клані"

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
        return "Такого гравця не існує :/"


def get_clan(clan_name):
    try:
        clan_data_response = requests.get(
            f'https://api.worldoftanks.eu/wot/clans/list/?application_id={config.WG_TOKEN}&search={clan_name}'
        )
        clan_data = clan_data_response.json()
        clan_info = clan_data['data'][0]

        message = (f"<b>Інформація про клан</b> <i>{clan_name}</i>\n"
                   f"<b>Тег клану:</b> {clan_info['tag']}\n"
                   f"<b>Назва клану:</b> {clan_info['name']}\n"
                   f"<b>Учасники клану:</b> {clan_info['members_count']}\n"
                   )

        return message

    except:
        return "Такого клану не існує :/"


@router.message(Command("cmembers"))
async def get_clan_members(message: types.Message):
    split_text = message.text.split()
    clan_name = split_text[-1]
    clan_data_response = requests.get(
        f'https://api.worldoftanks.eu/wot/clans/list/?application_id={config.WG_TOKEN}&search={clan_name}'
    )
    clan_data = clan_data_response.json()
    if clan_data.get('data') and clan_data['data'] and clan_data['data'][0]:
        await message.reply('Зачекайте...')
    else:
        await message.reply('Такого клану не існує =/')

    clan_info = clan_data['data'][0]
    clan_id = clan_info['clan_id']

    clan_members_response = requests.get(
        f'https://api.worldoftanks.eu/wot/clans/info/?application_id={config.WG_TOKEN}&clan_id={clan_id}&fields=members'
    )
    clan_members_data = clan_members_response.json()
    clan_members = clan_members_data['data'][str(clan_id)]["members"]
    total_members = len(clan_members)

    if total_members == 0:
        return "В клані немає учасників"

    leaderboard = (
        f"<b>Клан \"{clan_name}\"</b>\n\n"
        f"Кількість гравців у клані: {total_members}\n\n"
        f"<b><u>| Нік-нейм | роль | % перемог | середня шкода |</u></b>"
    )

    for index, member_info in enumerate(clan_members[:100], start=1):
        player_name = member_info['account_name']
        member_id = member_info['account_id']

        player_stats_response = requests.get(
            f'https://api.worldoftanks.eu/wot/account/info/?application_id={config.WG_TOKEN}&account_id={member_id}&fields=statistics.all'
        )
        player_stats_data = player_stats_response.json()

        stats = player_stats_data['data'][str(member_id)]['statistics']['all']
        battles = stats['battles']

        wins_percent = (stats['wins'] / battles * 100) if battles > 0 else 0.0
        avg_damage = (stats['damage_dealt'] / battles) if battles > 0 else 0.0

        leaderboard += (
            f"\n<b>{player_name}</b> - <i>{member_info['role']}</i>  -  <b>{wins_percent:.2f}%</b>  -  <b>{avg_damage:.2f}</b>"
        )

        if index % 10 == 0 or index == len(clan_members):
            await message.reply(
                text=leaderboard,
                parse_mode=ParseMode.HTML,
            )
            leaderboard = ""


