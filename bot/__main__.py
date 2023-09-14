import asyncio
import discord

from discord.ext import commands
from bot.bot import Bot
from bot.constants import bot_settings


async def main():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = Bot(
        command_prefix=commands.when_mentioned_or(bot_settings.prefix),
        intents=intents,
    )

    await bot.start(bot_settings.token)


asyncio.run(main())
