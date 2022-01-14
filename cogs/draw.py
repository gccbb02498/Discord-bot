from random import choice
from discord.ext import commands
from core.any import Cog_Extension


class Draw(Cog_Extension):
    @commands.command(pass_context=True)
    async def online(self, ctx):
        member_list = []

        print(self, ctx)
        guild = self.bot.get_guild(int("920702260911144971"))
        print(guild.members)
        for user in guild.members:
            if str(user.status) != "offline" and user.bot == False:
                print(user)
                member_list.append(f'{user.name}')
        await ctx.message.reply(f'在線名單:{",".join(member_list)}')

    @ commands.command(pass_context = True)
    async def draw(self, ctx):
        member_list=[]

        print(self, ctx)
        guild=self.bot.get_guild(int("920702260911144971"))
        print(guild.members)
        for user in guild.members:
            if str(user.status) != "offline" and user.bot == False:
                print(user)
                member_list.append(f'{user.name}')
        await ctx.message.reply(choice(member_list))


def setup(bot):
    bot.add_cog(Draw(bot))
