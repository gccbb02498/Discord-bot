import asyncio
from multiprocessing import context
from random import choice
from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.any import Cog_Extension
import json


class main(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.table = []
        self.nohokh = ["https://i.imgur.com/cZksr04.jpg",
                       "https://i.imgur.com/wH4CJLF.jpg", "https://i.imgur.com/ag0DVMT.jpg"]

    @commands.Cog.listener()
    async def on_message(self, message):
        embed = discord.Embed()
        if message.author == self.bot.user:
            return

        print(message.author, message.content)
        if message.content == '我好帥喔':
            
            await message.delete()
            
            await message.channel.send('不好意思，不要騙人啦')

        elif message.content.startswith('不可以色色'):
            if "可以色色" and "不可以色色" in self.table:
                self.table = []
                await message.reply(choice(self.nohokh))
            else:
                noh = ["https://imgur.dcard.tw/TUGMyF7h.jpg", "https://imgur.dcard.tw/ZayW5My.jpg", "https://i.imgur.com/WLbQBlT.jpg",
                       "https://i.imgur.com/nGI4pbO.jpg", "https://i.imgur.com/jrOvlgH.jpg", "https://i.imgur.com/68mqoce.jpg"]
                self.table.append('不可以色色')
                await message.reply(choice(noh))
        elif message.content.startswith('可以色色'):
            if "可以色色" and "不可以色色" in self.table:
                self.table = []
                await message.reply(choice(self.nohokh))  # 特招
            else:
                okh = ["https://i.imgur.com/UVZti2m.jpg", "https://i.imgur.com/FoGDvP7.jpg", "https://i.imgur.com/c2pDzLJ.jpg",
                       "https://i.imgur.com/0Ux7atA.jpg", "https://i.imgur.com/hnnSpzr.jpg", "https://i.imgur.com/F03Raad.jpg"]
                self.table.append("可以色色")
                await message.reply(choice(okh))  # 可以色色康特


def setup(bot):
    bot.add_cog(main(bot))
