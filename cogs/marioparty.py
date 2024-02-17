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
    partyplanner = SlashCommandGroup("partyplanner", "Party Planner related commands")


    #1 Subcommand
    @board.command(name='1')
    async def one(self, ctx):
    
        boardList=["DK's Jungle Adventure", "Peach's Birthday Cake", "Yoshi's Tropical Island", "Mario's Rainbow Castle", "Wario's Battle Canyon", "Luigi's Engine Room", "Eternal Star", "Bowser's Magma Mountain"]
        board=random.choice(boardList)
        boardParsed = urllib.parse.quote(board)
    
        embed = discord.Embed(title=board,
                              colour=0x98FB98)
    
        embed.set_image(url="https://raw.githubusercontent.com/EndangeredNayla/Doopliss/master/boards/1/" + boardParsed + ".png")
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Poggers")
     
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
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Poggers")
     
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
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Poggers")
     
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
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Poggers")
     
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
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Poggers")
     
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
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Poggers")
     
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
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Poggers")
     
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
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Poggers")
     
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
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Poggers")
     
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
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Poggers")
     
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
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Poggers")
     
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
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Poggers")
     
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
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Poggers")
     
        await ctx.respond(embed=embed)

    
    
    # Party Planner Board Get
    @partyplanner.command(pass_context=True, aliases=["cf"])
    async def curseforge(self, ctx, search: str=None):
        if search == None:
            params = {
            'gameId': '6351',
            'searchFilter': search
            }
        else:
            params = {
            'gameId': '6351',
            'searchFilter': search
            }
        url = "https://api.curse.tools/v1/cf/mods/search"
        responce = requests.get(url, params=params)
        json = responce.json()
        packList = []
        embed = discord.Embed(
            title=f"PartyPlanner64 Board Lookup",
            description="\uFEFF",
            colour=0x98FB98        )
        for pack in json["data"]:
            url2 = "https://api.curse.tools/v1/cf/mods/" + str(pack["id"]) + "/files/" + str(pack["mainFileId"])
            responce = requests.get(url2)
            json2 = responce.json()
            embed.add_field(name=pack["name"], value="https://" + urllib.parse.quote(json2["data"]["downloadUrl"][8:]), inline=True)

        if json["data"] == []:
            embed.add_field(name="No Results", value="")
        else:
            pass
        try:
            embed.set_thumbnail(
                url="https://i.ibb.co/k8tXpy4/ZNV4-Eki3-400x400.jpg"
            )
        except:
            pass
        embed.set_footer(
            text=f"Ran by: {ctx.author} • Yours truly, Poggers"
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        await ctx.respond(content=None, embed=embed)

    # Party Planner Board Get
    @partyplanner.command(pass_context=True, aliases=["legacy", "mpl"])
    async def mariopartylegacy(self, ctx, search: str=None):
        embed = discord.Embed(
            title=f"PartyPlanner64 Board Lookup",
            description="\uFEFF",
            colour=0x98FB98        )
        boardNameList = []
        boardURLList = []
        if search == None:
            urlHack = "https://www.mariopartylegacy.com/forum/index.php?action=downloads;cat=3;sortby=mostview;orderby=desc;start=0"
        else:
            urlHack = "https://www.mariopartylegacy.com/forum/index.php?action=downloads;cat=3;sortby=mostview;orderby=desc;start=0;sa=search2;searchfor=" + search
        response = requests.get(urlHack)
        soup = BeautifulSoup(response.content, 'html.parser')
        boardTitles = soup.find_all('tr', class_=["windowbg", "windowbg2"])
        for title in boardTitles:
            boardName = title.get_text()
            boardName = boardName.split("(None)")[0]
            boardName = boardName.strip()
            boardName = ' '.join([word for word in boardName.split() if not re.search(r'[123459789()]', word)])
            boardNameList.append(boardName)
        for url in boardTitles:
            link_element = url.find('a')
            if link_element:
                boardID = re.findall(r'\d+', link_element['href'])[-1]
                downloadURL = "https://www.mariopartylegacy.com/forum/index.php?action=downloads;sa=downfile&id=" + boardID
                boardURLList.append(downloadURL)

        for name, url in zip(boardNameList, boardURLList):
            embed.add_field(name=name, value=url, inline=True)
        try:
            embed.set_thumbnail(
                url="https://i.ibb.co/k8tXpy4/ZNV4-Eki3-400x400.jpg"
            )
        except:
            pass
        embed.set_footer(
            text=f"Ran by: {ctx.author} • Yours truly, Poggers"
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        await ctx.respond(content=None, embed=embed)

    


def setup(bot):
    bot.add_cog(MarioParty(bot))
