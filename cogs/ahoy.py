
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

    @commands.command(pass_context=True)
    async def 下午茶(self, ctx):
        await ctx.send('test 下午茶')
    @commands.command(pass_context=True)
    async def 阿翼(self, ctx):
        await ctx.send('此人不是號稱我沒有賭的那個嗎?\n聽說好像要退谷了')


def setup(bot):
    bot.add_cog(Ahoy(bot))
