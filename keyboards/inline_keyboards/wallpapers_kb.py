from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

prev_wp_callback = "prev_page"
next_wp_callback = "next_page"


def build_wallpapers_kb() -> InlineKeyboardMarkup:
    previous_btn = InlineKeyboardButton(
        text="Назад",
        callback_data=prev_wp_callback,
    )
    download_btn = InlineKeyboardButton(
        text="Завантажити",
        callback_data="download_pic",
    )
    next_btn = InlineKeyboardButton(
        text="Вперед",
        callback_data=next_wp_callback,
    )
    first_row = [previous_btn, next_btn]
    second_row = [download_btn]
    rows = [first_row, second_row]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def build_wallpapers_kb_blank_prev() -> InlineKeyboardMarkup:
    previous_btn = InlineKeyboardButton(
        text=" ",
        callback_data="no_data",
    )
    download_btn = InlineKeyboardButton(
        text="Завантажити",
        callback_data="download_pic",
    )
    next_btn = InlineKeyboardButton(
        text="Вперед",
        callback_data=next_wp_callback,
    )
    first_row = [previous_btn, next_btn]
    second_row = [download_btn]
    rows = [first_row, second_row]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def build_wallpapers_kb_blank_next() -> InlineKeyboardMarkup:
    previous_btn = InlineKeyboardButton(
        text="Назад",
        callback_data=prev_wp_callback,
    )
    download_btn = InlineKeyboardButton(
        text="Завантажити",
        callback_data="download_pic",
    )
    next_btn = InlineKeyboardButton(
        text=" ",
        callback_data="no_data",
    )
    first_row = [previous_btn, next_btn]
    second_row = [download_btn]
    rows = [first_row, second_row]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup
