
from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.any import Cog_Extension
from dotenv import load_dotenv
import os

load_dotenv()


class Ahoy(Cog_Extension):

    @commands.command(pass_context=True)
    async def ahoy(self, ctx):
        await ctx.send(file=discord.File(os.getenv("自訂")))


def setup(bot):
    bot.add_cog(Ahoy(bot))
