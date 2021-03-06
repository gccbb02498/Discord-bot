from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.any import Cog_Extension
import json


class Commons(Cog_Extension):
    @commands.command(pass_context=True)
    async def clean(slef, ctx, num: int):
        await ctx.channel.purge(limit=num+1)


def setup(bot):
    bot.add_cog(Commons(bot))
