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


class MapleStory(Cog_Extension):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list = {}
        # print(self.list)

    @commands.command(pass_context=True)
    async def character(self, ctx,):
        await ctx.channel.send("")

    @commands.command()
    async def charterSave(self, ctx, message):
        print(ctx.author.id, message)
        if str(ctx.author.id) in self.list:
            self.list[str(ctx.author.id)]["name"] = message
        else:
            self.list[str(ctx.author.id)] = {}
            self.list[str(ctx.author.id)]["name"] = message

        with open('mapleStory.json', 'w')as f:
            json.dump(self.list, f)
        # await ctx.channel.send("")

    @commands.command()
    async def getAll(self, ctx):
        if any(self.list) == False:
            with open('mapleStory.json', 'r') as f:
                self.list = json.load(f)
        await ctx.channel.send(self.list)

    @commands.command()
    async def 楓谷名子(self, ctx, message):

        if any(self.list) == False:
            with open('mapleStory.json', 'r') as f:
                self.list = json.load(f)
        userid = ''.join([x for x in message if x.isdigit()])
        userdata = {}
        guild = self.bot.get_guild(int("920702260911144971"))
        for user in guild.members:
            if str(user.id) == userid:
                print(user)
                userdata = user
        if str(userid) in self.list:

            embed = discord.Embed(title="楓之谷資訊", color=0x3d1e4d)
            embed.set_author(name=userdata.name)
            embed.add_field(
                name="角色名稱", value=self.list[str(userid)]["name"], inline=True)
            embed.add_field(
                name="職業", value=self.list[str(userid)]["class"], inline=True)
            embed.add_field(name="伺服器", value=self.list[str(
                userid)]["service"], inline=True)
            embed.add_field(
                name="介紹", value=self.list[str(userid)]["about"], inline=True)
            await ctx.send(embed=embed)
        else:
            await ctx.channel.send(f'該{userdata.name}尚未設定名稱')


def setup(bot):
    bot.add_cog(MapleStory(bot))
