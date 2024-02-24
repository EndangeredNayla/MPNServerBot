import discord
import platform
from datetime import datetime
from discord.ext import commands

#Variables
class Moderation(commands.Cog):

    """Cog for Base commands"""

    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        # Check if the author has the "Moderator" role
        moderator_role = discord.utils.get(ctx.guild.roles, name="Millennium Star (Mod)")
        return moderator_role in ctx.author.roles

    @commands.slash_command(pass_context=True)
    async def ban(self, ctx, user, message):
        if not await self.cog_check(ctx):
            return
        author = ctx.author
        reason = message
        server = ctx.guild.name
        data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        staff_log = self.bot.get_channel(1208522732602662972)
        embed = discord.Embed(
            title="MEMBER_BANNED",
            description="------------------------------------------------------",
            color=0x00ff00)
        embed.set_author(name="Member Banned:\nMember Banned Successfully")
        embed.add_field(
            title="Banned by: ", value="{}".format(author.mention), inline=False)
        embed.add_field(
            title="Banned: ", value="<@{}>".format(user.id), inline=False)
        embed.add_field(
            title="Reason: ",
            value="{}\n------------------------------------------------------".
            format(message),
            inline=False)
        embed.set_footer(
            text="Requested by {} \a {}".format(author, data),
            icon_url=author.avatar_url)
        await ctx.send(embed=embed)
        embed = discord.Embed(
            title="MEMBER_BANNED",
            description="------------------------------------------------------",
            color=0xff0000)
        embed.set_author(title="Member Banned:")
        embed.add_field(
            title="Banned by: ", value="{}".format(author.mention), inline=False)
        embed.add_field(
            title="Banned: ", value="<@{}>".format(user.id), inline=False)
        embed.add_field(
            title="Reason: ",
            value="{}\n------------------------------------------------------".
            format(message),
            inline=False)
        embed.set_footer(text="Banned at {}".format(data))
        await staff_log.send(embed=embed)
        embed = discord.Embed(
            title="BANNED",
            description="------------------------------------------------------",
            color=0xff0000)
        embed.set_author(title="Member Banned:\nYou've been Banned")
        embed.add_field(
            title="Banned by: ", value="{}".format(author.mention), inline=False)
        embed.add_field(
            title="Banned in: ", value="{}".format(server), inline=False)
        embed.add_field(
            title="Reason: ",
            value="{}\n------------------------------------------------------".
            format(message),
            inline=False)
        embed.set_footer(text="Banned at {}".format(data))
        await ctx.author.send(user, embed=embed)
        await ctx.guild.ban(user, reason=reason)
    
    @commands.slash_command(pass_context=True)
    async def kick(self, ctx, user, message):
        if not await self.cog_check(ctx):
            return
        author = ctx.author
        reason = message
        server = ctx.guild.name
        data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        staff_log = self.bot.get_channel(1208522732602662972)
        embed = discord.Embed(
            title="MEMBER_KICKED",
            description="------------------------------------------------------",
            color=0x00ff00)
        embed.set_author(title="Member Kicked:\nMember Kicked Successfully")
        embed.add_field(
            title="Kicked by: ", value="{}".format(author.mention), inline=False)
        embed.add_field(
            title="Kicked: ", value="<@{}>".format(user.id), inline=False)
        embed.add_field(
            title="Kicked: ",
            value="{}\n------------------------------------------------------".
            format(message),
            inline=False)
        embed.set_footer(
            text="Requested by {} \a {}".format(author, data),
            icon_url=author.avatar_url)
        await ctx.send(embed=embed)
        embed = discord.Embed(
            title="MEMBER_KICKED",
            description="------------------------------------------------------",
            color=0xff0000)
        embed.set_author(title="Member Kicked:")
        embed.add_field(
            title="Kicked by: ", value="{}".format(author.mention), inline=False)
        embed.add_field(
            title="Kicked: ", value="<@{}>".format(user.id), inline=False)
        embed.add_field(
            title="Reason: ",
            value="{}\n------------------------------------------------------".
            format(message),
            inline=False)
        embed.set_footer(text="Kicked at {}".format(data))
        await staff_log.send(embed=embed)
        embed = discord.Embed(
            title="KICKED",
            description="------------------------------------------------------",
            color=0xff0000)
        embed.set_author(name="Member Kicked:\nYou've been Kicked")
        embed.add_field(
            title="Kicked by: ", value="{}".format(author.mention), inline=False)
        embed.add_field(
            title="Kicked in: ", value="{}".format(server), inline=False)
        embed.add_field(
            title="Reason: ",
            value="{}\n------------------------------------------------------".
            format(message),
            inline=False)
        embed.set_footer(text="Kicked at {}".format(data))
        await ctx.author.send(user, embed=embed)
        await ctx.guild.kick(user, reason=reason)

def setup(bot):
    bot.add_cog(Moderation(bot))
