import discord
import platform
import random

from discord.ext import commands
from random import randint

#Variables
ownerID = 543576276108181506
class Base(commands.Cog):

    """Cog for Base commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        ctx = await self.bot.get_context(msg)
       
        if msg.content == "fuck me":
            await ctx.send("<:BetaBuzz:807778656683425833>")

        elif "pick me" in msg.content:
            listGet=["I, Doopliss, do not concern myself with such trifles", "Absolutely", "Maybe", "The opposite is true", "Phrase your quesry with eloquence please!", "Ask the opposite question", "Not likely", "Reply hazy, try again", "Ask again later", "What was the question?", "Don't count on it"]
            listChoose=random.choice(listGet)
            await ctx.send(listChoose)
    
        elif msg.content == "pog":
            await msg.add_reaction("<:ToadPOG:1055627241398206524>")
        
        elif msg.content == "bluey":
            await msg.add_reaction("<:BLUEY:857417269901787187>")

        elif msg.content == "bingo":
            await msg.add_reaction("<:BINGO:857416286900322355>")
        
        elif msg.content == "dad":
            await msg.add_reaction("<:BLUEY:857416289802387457>")

        elif msg.content == "mum":
            await msg.add_reaction("<:MUM:857416287957549106>")

        elif msg.content == "gotta be done":
            await msg.add_reaction("<:BanditDanceMode:681984948282064904>")

        elif msg.content == "gregg rul":
            await msg.add_reaction("<:GregRulzOk:527614081369112578>")

        elif "love me" in msg.content or "loves me" in msg.content:
            listGet=["<:LovesMe:682711728924262536>" "<:LovesMeNot:682711728756097042>", "<:ReallyLovesMe:682711780874518528>", "<:ReallyLovesMeNot:682711729116938266>"]
            listChoose=random.choice(listGet)
            await msg.add_reaction(listChoose)
    
    #Ping Command
    @commands.slash_command(description="Ping pong")
    async def ping(self, ctx):
        await ctx.respond("Pong")

    #Poll Command
    @commands.slash_command(description="Starts a poll")
    async def poll(self, ctx, question: str):
        mesg = ' '.join({question})
        embed = discord.Embed(
            title='A Poll has Started!',
            description='{0}'.format(mesg),
            color=0x00FF00)
        embed.set_footer(text=f"Poll created by: {ctx.author} • React to vote! • Yours truly, Doopliss")
        embed_message = await ctx.respond(embed=embed)

        await embed_message.add_reaction('👍')
        await embed_message.add_reaction('👎')
        await embed_message.add_reaction('🤷')
    
    #Server Command
    @commands.slash_command(descriptin="Shows server info")
    async def server(self, ctx):
        server = ctx.guild
        icon = ("\uFEFF")
        embed = discord.Embed(
            title=f"Server info for {server.name}",
            description='\uFEFF',
            colour=0x98FB98)
        try:
            embed.set_thumbnail(url=server.icon(size=512))
        except:
            pass
        embed.add_field(name="Name", value=server.name, inline=True)
        embed.add_field(name="Member Count", value=server.member_count, inline=True)
        embed.add_field(name="Owner", value="<@" + f"{server.owner_id}" + ">", inline=True)
        embed.add_field(name="ID", value=server.id, inline=True)
        embed.add_field(name="Creation Date", value=f"{server.created_at}", inline=True)
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Doopliss")
        await ctx.respond(content=None, embed=embed)

    #Stats Command
    @commands.slash_command()
    async def stats(self, ctx):

        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        serverCount = len(self.bot.guilds)
        memberCount = len(set(self.bot.get_all_members()))

        embed = discord.Embed(
            title=f'Doopliss Stats',
            description='\uFEFF',
            colour=0x98FB98)

        embed.add_field(
            name='Python Version:', value=f"{pythonVersion}", inline=False)
        embed.add_field(
            name='Py-Cord Version', value=f"{dpyVersion}", inline=False)
        embed.add_field(name='Total Guilds:', value=f"{serverCount}", inline=False)
        embed.add_field(name='Total Users:', value=f"{memberCount}", inline=False)
        embed.add_field(name='Bot Developer:', value="<@" + f"{ownerID}" + ">", inline=False)
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Doopliss")
        await ctx.respond(embed=embed)

    @commands.slash_command()
    async def channelid(self, ctx):
        await ctx.respond(str(ctx.channel.id))

    @commands.slash_command(brief="Get the ID of a member")
    async def userid(self, ctx, member : discord.Member=0):
      if member == 0:
        await ctx.respond(str(ctx.author.id))
      else:
        await ctx.respond(str(member.id))

def setup(bot):
    bot.add_cog(Base(bot))