import asyncio
from asyncio.windows_events import NULL
from contextlib import nullcontext
from multiprocessing import context
from random import choice
from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.any import Cog_Extension
import json


class Music(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @commands.command()
    async def join(self, ctx):

        destination = ctx.author.voice.channel
        await destination.connect()

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()


def setup(bot):
    bot.add_cog(Music(bot))
