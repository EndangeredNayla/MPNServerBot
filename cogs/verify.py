import discord
from discord.ext import commands
import random

class Verification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def verify(self, ctx):
        # Generate a random math equation
        num1 = random.randint(1, 999)
        num2 = random.randint(1, 999)
        operator = random.choice(['+', '*'])
        equation = f"{num1} {operator} {num2}"

        # Calculate the result
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2

        # Send the equation to the user via DM
        await ctx.author.send(f"Please solve the following equation to verify: `{equation}`")

        def check(message):
            return message.author == ctx.author and message.content.isdigit()

        try:
            # Wait for the user's response
            msg = await self.bot.wait_for('message', timeout=120.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send("Verification timed out. Please try again.")
            return

        if int(msg.content) == result:
            # Get the verified role (replace 'Verified' with your actual role name)
            role = discord.utils.get(ctx.guild.roles, name="Server Member")
            if role:
                await ctx.author.add_roles(role)  # Assign the role to the user
                await ctx.author.send("Verification successful! You've been granted the Verified role.")
            else:
                await ctx.author.send("Verification successful! However, the 'Verified' role is not found. Please contact a server administrator.")
        else:
            await ctx.author.send("Incorrect answer. Please try again.")

def setup(bot):
    bot.add_cog(Verification(bot))
