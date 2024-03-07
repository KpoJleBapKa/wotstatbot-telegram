from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.utils import markdown
from aiogram.enums import ParseMode

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message):
    url = "https://eu-wotp.wgcdn.co/dcont/fb/image/leopard-1-wallpaper-1920x1280.jpg"
    await message.answer(
        text=f'{markdown.hide_link(url)}Вітаю {message.from_user.first_name}! Ти <b>ЧОРНИЙ!</b> '
             f'Скористайся наступними командами щоб дізнатись інформацію про гравця чи клан:\n\n'
             f'/stat [ім\'я гравця] - Основна інформація про гравця\n'
             f'/clan [назва клану] - Основна інформація про клан\n'
             f'/cmembers [назва клану] - Список учасників клану',
        parse_mode=ParseMode.HTML,
    )
