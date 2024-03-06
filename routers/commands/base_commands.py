from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.utils import markdown
from aiogram.enums import ParseMode

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message):
    url = "https://eu-wotp.wgcdn.co/dcont/fb/image/leopard-1-wallpaper-1920x1280.jpg"
    await message.answer(
        text=f'{markdown.hide_link(url)}{message.from_user.first_name}, you are <b>BLACK!</b> btw send nickname to get statistics in WoT',
        parse_mode=ParseMode.HTML,
    )
