from aiogram import Router, F, types
from aiogram.types import CallbackQuery
from aiogram.utils import markdown
from aiogram.enums import ParseMode

from keyboards.inline_keyboards.wallpapers_kb import (
    prev_wp_callback,
    next_wp_callback,
    build_wallpapers_kb,
    build_wallpapers_kb_blank_prev,
    build_wallpapers_kb_blank_next,
)


router = Router(name=__name__)


links = [
    "https://eu-wotp.wgcdn.co/dcont/fb/image/leopard-1-wallpaper-2560x1440.jpg",
    "https://eu-wotp.wgcdn.co/dcont/fb/image/chi-nu-kai-wallpaper-2560x1440.jpg",
    "https://eu-wotp.wgcdn.co/dcont/fb/image/stb-1-wallpaper-2560x1440.jpg",
    "https://eu-wotp.wgcdn.co/dcont/fb/image/lowe-wallpaper-2560x1440.jpg",
    "https://eu-wotp.wgcdn.co/dcont/fb/image/sherman-wallpaper-2560x1440.jpg",
    "https://eu-wotp.wgcdn.co/dcont/fb/image/t95-2560x1440.jpg",
]

photos_on_disk = [
    "/Users/po4ta/Робочий стіл/photos_tg_bot/leopard-1-wallpaper-2560x1440.jpg",
    "/Users/po4ta/Робочий стіл/photos_tg_bot/chi-nu-kai-wallpaper-2560x1440.jpg",
    "/Users/po4ta/Робочий стіл/photos_tg_bot/stb-1-wallpaper-2560x1440.jpg",
    "/Users/po4ta/Робочий стіл/photos_tg_bot/lowe-wallpaper-2560x1440.jpg",
    "/Users/po4ta/Робочий стіл/photos_tg_bot/sherman-wallpaper-2560x1440.jpg",
    "/Users/po4ta/Робочий стіл/photos_tg_bot/t95-2560x1440.jpg",
]

tank_names = [
    "<b>Leopard 1</b>",
    "<b>Chi-Nu Kai</b>",
    "<b>STB-1</b>",
    "<b>Löwe</b>",
    "<b>Sherman</b>",
    "<b>T95</b>",
]

cur_page = 0


@router.callback_query(F.data == prev_wp_callback)
async def prev_wallpaper_callback_handler(callback_query: CallbackQuery):

    if cur_page <= 1:
        markup = build_wallpapers_kb_blank_prev()
    else:
        markup = build_wallpapers_kb()

    await callback_query.answer()
    await callback_query.message.edit_text(
        text=prev_page(),
        parse_mode=ParseMode.HTML,
        reply_markup=markup,
    )


@router.callback_query(F.data == next_wp_callback)
async def next_wallpaper_callback_handler(callback_query: CallbackQuery):

    if cur_page >= len(links) - 2:
        markup = build_wallpapers_kb_blank_next()
    else:
        markup = build_wallpapers_kb()

    await callback_query.answer()
    await callback_query.message.edit_text(
        text=next_page(),
        parse_mode=ParseMode.HTML,
        reply_markup=markup,
    )


def prev_page():
    global cur_page
    if cur_page > 0:
        cur_page -= 1
    page_text = f'{markdown.hide_link(links[cur_page])}{tank_names[cur_page]}'
    return page_text


def next_page():
    global cur_page
    if cur_page < len(links):
        cur_page += 1
    page_text = f'{markdown.hide_link(links[cur_page])}{tank_names[cur_page]}'
    return page_text


@router.callback_query(F.data == "download_pic")
async def next_wallpaper_callback_handler(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer_document(
        document=types.FSInputFile(
            path=photos_on_disk[cur_page]
        )
    )
