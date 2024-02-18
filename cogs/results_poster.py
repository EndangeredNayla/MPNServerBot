import discord
from discord.ext import commands
import os
import requests

class RPoster(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.credentials = None
   
    @commands.command(pass_context=True, aliases=["results"])
    async def results(self, ctx):
        await ctx.respond("Please fill out the following info: ")
        await ctx.send("Who got first place? (Diamond Rank)")
        diamondRank = await bot.wait_for("message", check=lambda message: message.author == ctx.author)
        await ctx.send("Who got second place? (Gold Rank)")
        goldRank = await bot.wait_for("message", check=lambda message: message.author == ctx.author)
        await ctx.send("Who got third place? (Silver Rank)")
        silverRank = await bot.wait_for("message", check=lambda message: message.author == ctx.author)
        await ctx.send("Who got last place? (Bronze Rank)")
        bronzeRank = await bot.wait_for("message", check=lambda message: message.author == ctx.author)
        await ctx.send("Upload the screenshots now")
        for attachment in ctx.message.attachments:
            response = requests.get(attachment.url)
            with open(attachment.filename, "wb") as f:
                f.write(response.content)
                await ctx.send(f"Thank you for your responses. Your favorite color is {response1.content}, your favorite animal is {response2.content}, and your favorite food is {response3.content}.")
                channel = bot.get_channel(1208879897200828427)
                await channel.send(f"Player 1: {diamondRank.content}\nPlayer 2: {goldRank.content}\nPlayer 3: {silverRank.content}\nPlayer 4: {silverRank.content}")
                await channel.send(file=discord.File(io.BytesIO(image_data), filename=attachment.filename))                
                os.remove(attachment.filename)

def setup(bot):
    bot.add_cog(RPoster(bot))
