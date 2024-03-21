from aiogram import Router

from .wallpapers_kb_handler import router as wallpapers_kb_router

router = Router(name=__name__)

router.include_routers(
    wallpapers_kb_router,
)

