from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown
from aiogram.enums import ParseMode

from keyboards.inline_keyboards.wallpapers_kb import build_wallpapers_kb_blank_prev
from keyboards.inline_keyboards.help_kb import build_help_kb

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message):
    url = "https://i.redd.it/2owoxvatv0161.jpg"
    await message.answer(
        text=f'{markdown.hide_link(url)}Вітаю {message.from_user.first_name}! '
             f'Тут можна дізнатись інформацію про гравця чи клан.\n\n'
             f'Дізнатися команди - /help',
        parse_mode=ParseMode.HTML,
    )


@router.message(Command("help"))
async def handle_info(message: types.Message):
    markup = build_help_kb()
    await message.answer(
        text="Потрібно дізнатися:",
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

