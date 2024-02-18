import discord
from discord.ext import commands
import os
import requests
import io
from datetime import datetime

class RPoster(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.credentials = None

    @commands.slash_command()
    async def results(self, ctx):
        await ctx.respond("Please fill out the following info: ")
        await ctx.send("Who got first place? (Diamond Rank)")
        diamondRank = await self.bot.wait_for("message", check=lambda message: message.author == ctx.author)
        await ctx.send("Who got second place? (Gold Rank)")
        goldRank = await self.bot.wait_for("message", check=lambda message: message.author == ctx.author)
        await ctx.send("Who got third place? (Silver Rank)")
        silverRank = await self.bot.wait_for("message", check=lambda message: message.author == ctx.author)
        await ctx.send("Who got last place? (Bronze Rank)")
        bronzeRank = await self.bot.wait_for("message", check=lambda message: message.author == ctx.author)

        await ctx.send("Upload the screenshots now")
        attachments = []
        # Wait for messages with attachments
        while True:
            attachment_message = await self.bot.wait_for("message", check=lambda message: message.author == ctx.author and len(message.attachments) > 0)
            attachments.extend(attachment_message.attachments)
            for attachment in attachments:
                response = requests.get(attachment.url)
                image_data = response.content
                await ctx.send(f"Received screenshot: {attachment.filename}")
                # Save the attachment locally
                file_path = os.path.join("attachments", attachment.filename)  # Assuming there's a directory named "attachments"
                with open(file_path, "wb") as f:
                    f.write(image_data)
               	    # Send the saved image file to the channel
                    channel = self.bot.get_channel(1208879897200828427)  # Replace with your channel ID
                    embed = discord.Embed(title="Results from " + datetime.today().strftime('%m/%d/%y'), colour=0x98FB98)
                    embed.description='{0}'.format(f"Player 1: {diamondRank.content}\nPlayer 2: {goldRank.content}\nPlayer 3: {silverRank.content}\nPlayer 4: {bronzeRank.content}")
                    file = discord.File("attachments/" + attachment.filename, filename="image.png")
                    embed.set_image(url="attachment://image.png")
                    embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Doopliss")
                    await channel.send(embed=embed, file=file)
		    # Remove the saved file
                    os.remove(file_path)
            await ctx.send(f"Upload Succedded: Moderation Pending")
def setup(bot):
    bot.add_cog(RPoster(bot))
