from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

stat_cb_data = "stat"
clan_cb_data = "clan"
cmem_cb_data = "cmem"
wallp_cb_data = "wallp"


def build_help_kb() -> InlineKeyboardMarkup:
    stat_btn = InlineKeyboardButton(
        text="👤 Статистику гравця",
        callback_data=stat_cb_data,
    )
    clan_btn = InlineKeyboardButton(
        text="🏰 Інформацію про клан",
        callback_data=clan_cb_data,
    )
    clan_members_btn = InlineKeyboardButton(
        text="👥 Список гравців клану",
        callback_data=cmem_cb_data,
    )
    wallpapers_btn = InlineKeyboardButton(
        text="🏞 Фотокарточкі з танчіками",
        callback_data=wallp_cb_data,
    )
    row1 = [stat_btn]
    row2 = [clan_btn]
    row3 = [clan_members_btn]
    row4 = [wallpapers_btn]
    rows = [row1, row2, row3, row4]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup
