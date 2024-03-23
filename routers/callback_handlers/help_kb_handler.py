from aiogram import Router, F, types
from aiogram.types import CallbackQuery
from aiogram.utils import markdown
from aiogram.enums import ParseMode

from keyboards.inline_keyboards.help_kb import (
    stat_cb_data,
    clan_cb_data,
    cmem_cb_data,
    wallp_cb_data,
)


router = Router(name=__name__)


@router.callback_query(F.data == stat_cb_data)
async def stat_callback_handler(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(
        text="/stat [ім\'я гравця] - Основна інформація про гравця"
    )


@router.callback_query(F.data == clan_cb_data)
async def stat_callback_handler(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(
        text="/clan [назва клану] - Основна інформація про клан"
    )


@router.callback_query(F.data == cmem_cb_data)
async def stat_callback_handler(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(
        text="/cmembers [назва клану] - Список учасників клану"
    )


@router.callback_query(F.data == wallp_cb_data)
async def stat_callback_handler(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(
        text="/wallpapers"
    )

