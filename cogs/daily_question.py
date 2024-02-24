import discord
import random
import asyncio
from discord.ext import commands, tasks
from datetime import datetime, timedelta
import pytz

icebreaker_questions = [
    "If video game characters were real, which one do you think would make the best roommate and why?",
    "If you could create a video game based on your life, what would the title be and what would the objective be?",
    "If you were a character in a video game, what special power or ability would you have and how would you use it to your advantage?",
    "If you could live inside any computer program or software, which one would it be and why?",
    "If you were trapped in a virtual reality game for a week, which era or setting would you choose for the game to take place in?",
    "If you had to assemble a team of three fictional AI companions from different video games to help you solve real-world problems, who would you choose and why?",
    "If you could enhance any piece of technology from a video game and make it a reality, what would it be and how would it improve your daily life?",
    "If you could transport yourself into the world of any classic arcade game, which one would you choose and how would you fare in its challenges?",
    "If your life was a point-and-click adventure game, what would be the first puzzle you'd encounter and how would you solve it?",
    "If you could design your own virtual reality game, what would the central theme or concept be and why?",
    "If you could upload your consciousness into a computer like in a science fiction game, what would be the first thing you'd do in your new digital form?",
    "If you had to survive a zombie apocalypse using only items found in computer games, what would be your go-to weapon and why?",
    "If you could bring one piece of futuristic technology from a video game into the present day, what would it be and how would it revolutionize society?"
]

class DailyQ(commands.Cog):

    """Cog for Toontown commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def daily_question(self, ctx):
        now = datetime.now(pytz.timezone('US/Eastern'))
        if now.hour == 14 and now.minute == 41:  # Check if it's 5:00 AM EST
            embed = discord.Embed(
                title='Daily Question',
                description=random.choice(icebreaker_questions),
                colour=0x98FB98
            )
            embed.set_footer(text=f"Ran by: {ctx.author}")
            embed.set_author(name=ctx.author, icon_url=self.bot.user.avatar.url)
            channel = self.bot.get_channel(1211032887114342510)  # Replace YOUR_CHANNEL_ID with the actual channel ID
            await channel.send(content=None, embed=embed)

def setup(bot):
    bot.add_cog(DailyQ(bot))