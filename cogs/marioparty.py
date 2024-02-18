import discord
import random
import urllib
import requests
import re

from bs4 import BeautifulSoup
from discord.ext import commands
from discord import SlashCommandGroup

class MarioParty(commands.Cog):

    """Cog for Mario Party commands"""

    def __init__(self, bot):
        self.bot = bot

    board = SlashCommandGroup("board", "MP Board related commands")


    #1 Subcommand
    @board.command(name='1')
    async def one(self, ctx):
    
        boardList=["DK's Jungle Adventure", "Peach's Birthday Cake", "Yoshi's Tropical Island", "Mario's Rainbow Castle", "Wario's Battle Canyon", "Luigi's Engine Room", "Eternal Star", "Bowser's Magma Mountain"]
        board=random.choice(boardList)
        boardParsed = urllib.parse.quote(board)
    
        embed = discord.Embed(title=board,
                              colour=0x98FB98)
    
        embed.set_image(url="https://raw.githubusercontent.com/EndangeredNayla/Doopliss/master/boards/1/" + boardParsed + ".png")
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Doopliss")
     
        await ctx.respond(embed=embed)
    
    #2 Subcommand
    @board.command(name='2')
    async def two(self, ctx):
    
        boardList=["Western Land", "Space Land", "Mystery Land", "Pirate Land", "Horror Land", "Bowser Land"]
        board=random.choice(boardList)
        boardParsed = urllib.parse.quote(board)
    
        embed = discord.Embed(title=board,
                              colour=0x98FB98)
    
        embed.set_image(url="https://raw.githubusercontent.com/EndangeredNayla/Doopliss/master/boards/2/" + boardParsed + ".png")
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Doopliss")
     
        await ctx.respond(embed=embed)
    
    #3 Subcommand
    @board.command(name='3')
    async def three(self, ctx):
    
        boardList=["Chilly Waters", "Deep Bloober Sea", "Woody Woods", "Creepy Cavern", "Spiny Desert", "Waluigi's Island"]
        board=random.choice(boardList)
        boardParsed = urllib.parse.quote(board)
    
        embed = discord.Embed(title=board,
                              colour=0x98FB98)
    
        embed.set_image(url="https://raw.githubusercontent.com/EndangeredNayla/Doopliss/master/boards/3/" + boardParsed + ".png")
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Doopliss")
     
        await ctx.respond(embed=embed)
        
    
    #4 Subcommand
    @board.command(name='4')
    async def four(self, ctx):
    
        boardList=["Toad's Midway Madness", "Boo's Haunted Bash", "Koopa's Seaside Soiree", "Goomba's Greedy Gala", "Shy Guy's Jungle Jam", "Bowser's Gnarly Party"]
        board=random.choice(boardList)
        boardParsed = urllib.parse.quote(board)
    
        embed = discord.Embed(title=board,
                              colour=0x98FB98)
    
        embed.set_image(url="https://raw.githubusercontent.com/EndangeredNayla/Doopliss/master/boards/4/" + boardParsed + ".png")
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Doopliss")
     
        await ctx.respond(embed=embed)
    
    #5 Subcommand
    @board.command(name='5')
    async def five(self, ctx):
    
        boardList=["Toy Dream", "Rainbow Dream", "Pirate Dream", "Future Dream", "Undersea Dream", "Sweet Dream", "Bowser's Nightmare"]
        board=random.choice(boardList)
        boardParsed = urllib.parse.quote(board)
    
        embed = discord.Embed(title=board,
                              colour=0x98FB98)
    
        embed.set_image(url="https://raw.githubusercontent.com/EndangeredNayla/Doopliss/master/boards/5/" + boardParsed + ".png")
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Doopliss")
     
        await ctx.respond(embed=embed)
    
    #6 Subcommand
    @board.command(name='6')
    async def six(self, ctx):
    
        boardList=["Towering Treetop", "E Gadd's Garage", "Faire Square", "Snowflake Lake", "Castaway Bay", "Clockwork Castle"]
        board=random.choice(boardList)
        boardParsed = urllib.parse.quote(board)
    
        embed = discord.Embed(title=board,
                              colour=0x98FB98)
    
        embed.set_image(url="https://raw.githubusercontent.com/EndangeredNayla/Doopliss/master/boards/6/" + boardParsed + ".png")
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Doopliss")
     
        await ctx.respond(embed=embed)
    
    #7 Subcommand
    @board.command(name='7')
    async def seven(self, ctx):
    
        boardList=["Grand Canal", "Pagoda Peak", "Pyramid Park", "Neon Heights", "Windmillville", "Bowser's Enchanted Inferno"]
        board=random.choice(boardList)
        boardParsed = urllib.parse.quote(board)
    
        embed = discord.Embed(title=board,
                              colour=0x98FB98)
    
        embed.set_image(url="https://raw.githubusercontent.com/EndangeredNayla/Doopliss/master/boards/7/" + boardParsed + ".png")
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Doopliss")
     
        await ctx.respond(embed=embed)
    
    #8 Subcommand
    @board.command(name='8')
    async def eight(self, ctx):
    
        boardList=["DK's Treetop Temple", "Goomba's Booty Boardwalk", "King Boo's Haunted Hideaway", "Shy Guy's Perplex Express", "Koopa's Tycoon Town", "Bowser's Warped Orbit"]
        board=random.choice(boardList)
        boardParsed = urllib.parse.quote(board)
    
        embed = discord.Embed(title=board,
                              colour=0x98FB98)
    
        embed.set_image(url="https://raw.githubusercontent.com/EndangeredNayla/Doopliss/master/boards/8/" + boardParsed + ".png")
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Doopliss")
     
        await ctx.respond(embed=embed)
    
    #9 Subcommand
    @board.command(name='9')
    async def nine(self, ctx):
    
        boardList=["Toad Road", "Blooper Beach", "Boo's Horror Castle", "DK's Jungle Ruins", "Bowser's Station", "Magma Mine", "Bob-omb Factory"]
        board=random.choice(boardList)
        boardParsed = urllib.parse.quote(board)
    
        embed = discord.Embed(title=board,
                              colour=0x98FB98)
    
        embed.set_image(url="https://raw.githubusercontent.com/EndangeredNayla/Doopliss/master/boards/9/" + boardParsed + ".png")
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Doopliss")
     
        await ctx.respond(embed=embed)
    
    #10 Subcommand
    @board.command(name='10')
    async def ten(self, ctx):
    
        boardList=["Mushroom Park", "Whimsical Waters", "Chaos Castle", "Airship Central", "Haunted Trail"]
        board=random.choice(boardList)
        boardParsed = urllib.parse.quote(board)
    
        embed = discord.Embed(title=board,
                              colour=0x98FB98)
    
        embed.set_image(url="https://raw.githubusercontent.com/EndangeredNayla/Doopliss/master/boards/10/" + boardParsed + ".png")
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Doopliss")
     
        await ctx.respond(embed=embed)
    
    #DS Subcommand
    @board.command()
    async def ds(self, ctx):
    
        boardList=["Wiggler's Garden", "Kamek's Library", "Bowser's Pinball Machine", "Toadette's Music Room", "DK's Stone Statue"]
        board=random.choice(boardList)
        boardParsed = urllib.parse.quote(board)
    
        embed = discord.Embed(title=board,
                              colour=0x98FB98)
    
        embed.set_image(url="https://raw.githubusercontent.com/EndangeredNayla/Doopliss/master/boards/DS/" + boardParsed + ".png")
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Doopliss")
     
        await ctx.respond(embed=embed)
    
    #Super Subcommand
    @board.command(name='s')
    async def super(self, ctx):
    
        boardList=["Whomp's Domino Ruins", "King Bob-omb's Powderkeg Mine", "Megafruit Paradise", "Kamek's Tantalizing Tower"]
        board=random.choice(boardList)
        boardParsed = urllib.parse.quote(board)
    
        embed = discord.Embed(title=board,
                              colour=0x98FB98)
    
        embed.set_image(url="https://raw.githubusercontent.com/EndangeredNayla/Doopliss/master/boards/Super/" + boardParsed + ".png")
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Doopliss")
     
        await ctx.respond(embed=embed)
    
    #Superstars Subcommand
    @board.command(name='ss')
    async def superstars(self, ctx):
    
        boardList=["Yoshi's Tropical Island", "Peach's Birthday Cake", 'Space Land', 'Horror Land', 'Woody Woods']
        board=random.choice(boardList)
        boardParsed = urllib.parse.quote(board)
    
        embed = discord.Embed(title=board,
                              colour=0x98FB98)
    
        embed.set_image(url="https://raw.githubusercontent.com/EndangeredNayla/Doopliss/master/boards/Superstars/" + boardParsed + ".png")
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Doopliss")
     
        await ctx.respond(embed=embed)
    

def setup(bot):
    bot.add_cog(MarioParty(bot))
