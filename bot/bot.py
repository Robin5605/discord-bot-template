import logging
from discord.ext import commands
from bot import exts as extensions
from bot.utils.exts import walk_extensions

log = logging.getLogger(__name__)


class Bot(commands.Bot):
    async def setup_hook(self) -> None:
        """Asynchronous initialization method provided by discord.py"""
        await self.load_extensions()

    async def load_extensions(self) -> None:
        log.info("Loading extensions")
        for ext in walk_extensions(extensions):
            log.info("Loading %s", ext)
            await self.load_extension(ext)
        log.info("Finished loading extensions")
