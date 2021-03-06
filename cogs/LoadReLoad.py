import discord
from discord.ext import commands
from core.any import Cog_Extension
from discord.ext.commands import bot
import json
import os


class reloadCogs(Cog_Extension):
    @commands.command()
    # @commands.is_owner()
    async def load(self, ctx, extension):
        print(ctx, extension)
        try:
            self.bot.load_extension(f'cogs.{extension}')
            # await ctx.author.send(f"{extension} 蝦蝦成功上傳了，快稱讚她")
            await ctx.send(f"{extension} 蝦蝦成功上傳了，快稱讚她")
        except:
            print("except")

    @commands.command()
    async def unload(self, ctx, extension):
        self.bot.unload_extension(f"cmds.{extension}")
        # await ctx.author.send(f'{extension} 已卸載')
        await ctx.send(f"{extension} 蝦蝦成功卸載'了，快稱讚她")

    @commands.command()
    async def reload(self, ctx, extension):
        self.bot.reload_extension(f'cogs.{extension}')
        # await ctx.author.send(f'{extension} 蝦蝦已進行更新了，快來使用功能來讚嘆蝦蝦')
        await ctx.send(f'{extension} 蝦蝦已進行更新了，快來使用功能來讚嘆蝦蝦')


def setup(bot):
    bot.add_cog(reloadCogs(bot))
