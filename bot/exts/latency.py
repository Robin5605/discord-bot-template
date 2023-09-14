import discord
from discord.ext import commands
from discord.ext.commands import Cog, Context
from bot.bot import Bot


class Latency(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @commands.command(aliases=("ping",))
    async def latency(self, ctx: Context) -> None:
        embed = discord.Embed(
            title="Latency",
            description=f"{self.bot.latency*1000:.0f} ms",
            color=discord.Color.blurple(),
        )

        await ctx.send(embed=embed)


async def setup(bot: Bot) -> None:
    cog = Latency(bot)
    await bot.add_cog(cog)
