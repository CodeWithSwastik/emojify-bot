import os
from typing import Union
import discord
from dotenv import load_dotenv
from PIL import Image
from discord.ext import commands
from emojify import emojify_image
import requests  # It's not blocking, you can use aiohttp if you want

bot = commands.Bot(command_prefix="e>")


@bot.command()
async def emojify(ctx, url: Union[discord.Member, str], size: int = 14):
    if not isinstance(url, str):
        url = url.display_avatar.url

    def get_emojified_image():
        r = requests.get(url, stream=True)
        image = Image.open(r.raw).convert("RGB")
        res = emojify_image(image, size)

        if size > 14:
            res = f"```{res}```"
        return res

    result = await bot.loop.run_in_executor(None, get_emojified_image)
    await ctx.send(result)


load_dotenv()
bot.run(os.environ["TOKEN"])
