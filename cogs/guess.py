import random
from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.any import Cog_Extension


class Guess(Cog_Extension):
    @commands.command()
    async def guess(self, ctx):
        def check(number):
            return number.channel == ctx.message.channel
        global lowernumber
        global highernumber

        lowernumber = 1
        highernumber = 100

        number = random.randint(lowernumber, highernumber)
        # print(number)

        await ctx.send('1-100，任意選一個數字，六次猜中機會而已喔')
        count = 1
        while True:
            response = await self.bot.wait_for('message', check=check)

            try:
                guess = int(response.content)
                if guess == number:
                    await ctx.send("猜對了")
                    break
                if guess > 100:
                    await ctx.send("超過100，格式錯誤")
                if guess < number:
                    lowernumber = guess
                    await ctx.send(f"第{count}回 比 {lowernumber}大，比 {highernumber} 小")
                if guess > number:
                    highernumber = guess
                    await ctx.send(f"第{count}回 比 {lowernumber}大，比 {highernumber} 小")
                count += 1
            except:
                await ctx.send("請輸入數字")


def setup(bot):
    bot.add_cog(Guess(bot))
