
import discord
from discord.ext import commands
import json
import os
from dotenv import load_dotenv


load_dotenv()


if __name__ == '__main__':
    intents = discord.Intents.all()
    intents.members = True
    bot = commands.Bot(command_prefix='!',
                       owner_ids=os.getenv('owner_id'), intents=intents)

    @bot.event
    async def on_ready():
        game = discord.Game('機器人自主學習py中')
        await bot.change_presence(status=discord.Status.idle, activity=game)
        print(f"Bot in ready")

    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            name = file[:-3]
            print(name)
            bot.load_extension(f"cogs.{name}")
    bot.run(os.getenv('token'))
