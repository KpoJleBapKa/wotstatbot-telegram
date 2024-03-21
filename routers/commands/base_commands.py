from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import markdown
from aiogram.enums import ParseMode

from keyboards.inline_keyboards.wallpapers_kb import build_wallpapers_kb_blank_prev

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message):
    url = "https://eu-wotp.wgcdn.co/dcont/fb/image/leopard-1-wallpaper-1920x1280.jpg"
    await message.answer(
        text=f'{markdown.hide_link(url)}Вітаю {message.from_user.first_name}! '
             f'Скористайся наступними командами щоб дізнатись інформацію про гравця чи клан:\n\n'
             f'/stat [ім\'я гравця] - Основна інформація про гравця\n'
             f'/clan [назва клану] - Основна інформація про клан\n'
             f'/cmembers [назва клану] - Список учасників клану',
        parse_mode=ParseMode.HTML,
    )


@router.message(Command("help"))
async def handle_info(message: types.Message):
    stat_btn = InlineKeyboardButton(
        text="👤 Статистика гравця",
        text_to_insert="/stat ",

    )
    clan_btn = InlineKeyboardButton(
        text="🏰 Інформація про клан",
        switch_inline_query_current_chat="/clan ",
    )
    clan_members_btn = InlineKeyboardButton(
        text="👥 Список гравців клану",
        switch_inline_query_current_chat="/cmembers ",
    )
    row = [stat_btn, clan_btn, clan_members_btn]
    rows = [row]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await message.answer(
        text="Список команд:",
        reply_markup=markup,
    )


@router.message(Command("wallpapers"))
async def handle_wallpapers(message: types.Message):
    tank_url = "https://eu-wotp.wgcdn.co/dcont/fb/image/leopard-1-wallpaper-1920x1280.jpg"
    markup = build_wallpapers_kb_blank_prev()
    await message.answer(
        text=f'{markdown.hide_link(tank_url)}<b>Leopard 1</b>',
        reply_markup=markup,
        parse_mode=ParseMode.HTML,
    )

