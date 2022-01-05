import os
from dotenv import load_dotenv
from PIL import Image
from discord.ext import commands
from emojify import emojify_image
import requests

bot = commands.Bot(command_prefix="e>")


@bot.command()
async def emojify(ctx, url, size: int = 14):
    def get_emojified_image():
        r = requests.get(url, stream=True)
        image = Image.open(r.raw).convert("RGB")
        res = emojify_image(image, size)

        if size > 15:
            res = f"```{res}```"
        return res

    result = await bot.loop.run_in_executor(None, get_emojified_image)
    await ctx.send(result)


load_dotenv()
bot.run(os.environ["TOKEN"])
