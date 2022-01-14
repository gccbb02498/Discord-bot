from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.any import Cog_Extension
import json


class Embeds(Cog_Extension):
    @commands.command(pass_context=True)
    async def helping(self, ctx):
        sms = discord.Embed(title="指令",
                            description="'忘記了嗎? 來看一下吧~~", color=0x4599)
        sms.set_thumbnail(
            url="https://www.formula-ai.com/wp-content/uploads/2020/09/python_or_java_meme.jpg")
        await ctx.send(embed=sms)


def setup(bot):
    bot.add_cog(Embeds(bot))
