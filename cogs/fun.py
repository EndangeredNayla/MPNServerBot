import aiohttp
import discord
import random
import requests
import time

from dadjokes import Dadjoke
from discord.ext import commands
from discord import emoji, SlashCommandGroup

class Fun(commands.Cog):

    """Cog for Fun commands"""

    def __init__(self, bot):
        self.bot = bot

    game = SlashCommandGroup("game", "Game related commands")

    global n64MPList
    n64MPList=["Mario Party 1", "Mario Party 2", "Mario Party 3"]
    
    global gcMPList
    gcMPList=["Mario Party 4", "Mario Party 5", "Mario Party 6", "Mario Party 7"]
    
    global wiiMPList
    wiiMPList=["Mario Party 8", "Mario Party 9"]
    
    global mp8List
    mp8List=["Mario Party 8"]

    global DSMPList
    DSMPList=["Mario Party DS"]
    
    global AdvanceMPList
    AdvanceMPList=["Mario Party Advance", "Mario Party e"]
    
    global threeDSMPList
    threeDSMPList=["Mario Party: Island Tour", "Mario Party: Star Rush", "Mario Party: The Top 100", "Mario Party Advance", "Mario Party e"]
    
    global switchMPList
    handheldMPList=["Mario Party Superstars", "Super Mario Party"]

    global n64List
    n64List = n64MPList + ["Rugrats Scavenger Hunt", "1080 Snowboarding", "Banjo-Tooie", "Conker's Bad Fur Day", "Diddy Kong Racing", "Donkey Kong 64", "Dr. Mario 64", "F-Zero X", "GoldenEye 007", "Kirby 64", "Lego Racers", "Mario Golf", "Mario Kart 64", "Mickey's Speedway USA", "Pokemon Stadium", "Pokemon Stadium 2", "Rakuga Kids", "Super Smash Bros (N64)", "Snowboard Kids", "Snowboard Kids 2", "Star Wars Episode I Pod Racer", "Wave Race 64", "Super Smash Bros 199XTE", "Smash Remix", "South Park World Rally", "Monopoly", "Cruis'n USA", "Hotwheels: Turbo Racing", "Bomberman 64", "Pokemon Puzzle League", "Tony Hawk's Pro Skater", "Tony Hawk's Pro Skater 2", "Tony Hawk's Pro Skater 3", "NFL Blitz 2000", "NFL Blitz 2001", "Stunt Racer", "The New Tetris", "Cruis'n Exotica", "WWF No Mercy", "Superman 64", "Mundial Ronaldinho Soccer 64", "International Superstar Soccer 64", "ClayFighter: Sculptor's Cut", "Rush 2: Extreme Racing USA", "ClayFighter 63 1/3", "007: The World is Not Enough", "Killer Instinct Gold", "Mortal Kombat 4", "Mortal Kombat Trilogy", "Mario Tennis"]
    
    global gcList
    gcList = gcMPList + ["Mario Party 4", "Mario Party 5", "Mario Party 6", "Mario Party 7", "Billy Hatcher and the Giant Egg", "DDR Mario Mix", "Dragon Ball Z Budokai 2", "F-Zero GX", "Harvest Moon: Magical Melody", "Kirby Air Ride", "Mario Golf: Toadstool Tour", "Mario Kart: Double Dash!!", "Mario Power Tennis", "Mario Superstar Baseball", "Metroid Prime 2: Echoes", "Pikmin 2", "Sonic Adventure 2: Battle", "Soul Calibur II", "Star Fox Assault", "Star Wars: Clone Wars", "Super Mario Strikers", "Super Monkey Ball", "Super Monkey Ball 2", "Super Smash Bros Melee", "Super Smash Bros Melee 20XX", "WarioWare: Mega Party Games", "The Simpsons: Hit & Run", "F-Zero GX-Treme", "Super Monkey Ball Deluxe (patch for 2)", "Monkeyed Ball 2: Witty Subtitle", "Super Monkey Ball: Community Workshop Level Pack", "Donkey Konga", "Donkey Konga 2", "Tony Hawk's American Wasteland", "Shrek Super Party", "Spongebob: Lights, Camera, Pants!", "Super Monkey Ball Adventure", "SSX On Tour", "NBA Street V3", "Tiger Woods PGA Tour 2003", "Sonic Gems Collection", "Namco Museum: 50th Anniversary", "007 Nightfire", "007 Everything Or Nothing", "All Star Baseball 2004", "Shrek 2", "Shrek Smash and Crash Racing", "Nicktoons Unite!", "The Legend of Zelda: Four Swords Adventures", "Sonic Riders", "Digimon Rumble Arena 2", "Digimon World 4", "Tony Hawk's Underground", "Tony Hawk's Underground 2", "Godzilla: Destroy All Monsters Melee", "Burnout 2", "Need For Speed: Hot Pursuit", "Namco Museum: Battle Collection", "some WWE game idk", "Sonic the Fighters", "Smashing Drive", "Sonic Heroes", "Madagascar", "Pac-Man World Rally", "Rayman Arena", "SSX Tricky", "Nintendo Puzzle Collection", "Mega Man 2: The Power Fighters", "Black & Bruised", "Capcom vs SNK 2", "Viewtiful Joe: Red-Hot Rumble", "Pokemon Colosseum", "Pokemon XD: Gale of Darkness", "NHL Hitz 20-02", "Need For Speed: Carbon", "Mary-Kate and Ashley: Sweet 16 – Licensed to Drive", "Pac-Man Fever", "Timesplitters 2", "Timesplitters: Future Perfect", "Lego Star Wars: The Video Game"]
    
    global wiiList    
    wiiList = wiiMPList + ["Mario Kart Wii", "Super Smash Bros Brawl", "Project M", "Dragon Ball Z Budokai 3", "Wii Sports", "Wii Play", "Wii Sports Resort", "Wii Music", "Wii Play Motion", "Wii Party", "Mario Kart Fun", "Mario Kart Fusion", "Super Monkey Ball Banana Blitz", "Super Monkey Ball Step & Roll", "Mario Super Sluggers", "Mario Strikers Charged", "Fortune Street", "Punch-Out!!", "Mario Sports Mix", "Donkey Kong Country Returns", "Kirby's Epic Yarn", "Kirby's Return To Dream Land", "WarioWare: Smooth Moves", "Mario & Sonic at the Olympic Games", "Mario & Sonic at the Olympic Winter Games", "Mario & Sonic at the London 2012 Olympic Games", "Rhythm Heaven Fever", "Donkey Kong Barrel Blast", "Namco Museum Remix", "Rayman Raving Rabbids", "Rayman Raving Rabbids 2", "Rabbids TV Party", "Rabbids Go Home", "Rayman Origins", "New Super Mario Bros Wii", "Newer Super Mario Bros Wii", "Another Super Mario Bros Wii", "New Summer Sun Bros Wii", "M&M's Kart Racing", "Deca Sports", "GoldenEye Wii", "some call of duty game idk", "Brawl Minus", "Hasbro Family Game Night 3", "Guilty Gear XX Accent Core +", "Tatsunoko vs Capcom", "Chicken Little: Ace in Action", "Trauma Center: New Blood", "Boom Blox", "Pokemon Battle Revolution"]
    
    #Roll Command
    @commands.slash_command(aliases=["party"])
    async def roll(self, ctx, min: int, max:int, count:int):
        
        """Roll a dice, default is rolling 1d6. (minNumber, maxNumber, diceCount)"""
        if count <= 20:
            for _ in range(count):
                await ctx.respond(random.randint(min, max))
        if count > 20:
            await ctx.respond('Invalid number of rolls')
    
    #Random Command
    @commands.slash_command(aliases=["random"])
    async def random_player (self, ctx):
        """Spits out 1, 2, or 3"""
        await ctx.respond(random.randint(1, 3))

    #Dadjoke Command
    @commands.slash_command(aliases=["dadjoke"])
    async def dadjoke(self, ctx):
        """Sends a dadjoke."""
        await ctx.respond(Dadjoke().joke)
    
    #Piracy Command
    @commands.slash_command(aliases=["piracy"])
    async def piracy(self, ctx):
        """Sends a piracy notice."""
        await ctx.respond("Piracy is no party. Wondering how to get the games? It is against our rules and Discord ToS to link to ROM sharing sites, so users here cannot help you. We encourage users to rip their own games using this guide: https://wii.guide/dump-games.html")
            
    #Coin Flip Command
    @commands.slash_command(aliases=["flip"])
    async def toss(self, ctx):
        """Flip a coin, heads or tails, your fate"""
        ch = ["Heads", "Tails"]
        rch = random.choice(ch)
        await ctx.respond(f"You got **{rch}**")


    #Reverse Text Command
    @commands.slash_command()
    async def reverse(self, ctx, *, text):
        """Reverse the given text"""
        await ctx.respond("".join(list(reversed(str(text)))))


    #Meme Command
    @commands.slash_command()
    async def meme(self, ctx):
        """Sends you random meme"""
        r = await aiohttp.ClientSession().get(
            "https://www.reddit.com/r/dankmemes/top.json?sort=new&t=day&limit=100")
        r = await r.json()
        r = box.Box(r)
        data = random.choice(r.data.children).data
        img = data.url
        title = data.title
        url_base = data.permalink
        url = "https://reddit.com" + url_base
        embed = discord.Embed(title=title, url=url, color=discord.Color.blurple())
        embed.set_image(url=img)
        await ctx.respond(embed=embed)

    #Game Subcommand
    @game.command(name='marioparty')
    async def marioparty(self, ctx, amount):
        """Pick a Mario Party in general"""
        if amount == None:
            amount = 1
        box=random.sample(n64MPList + gcMPList + wiiMPList + AdvanceMPList + threeDSMPList + DSMPList + switchMPList, amount)
        boxMain = str(box).replace("[", "")
        boxMain = boxMain.replace("]", "")
        boxMain = boxMain.replace("'", "")
        boxMain = boxMain.replace(",", "")
        await ctx.respond(gameSelect)

    #Game Subcommand
    @game.command(name='marioparty-n64')
    async def marioparty(self, ctx):
        """Pick a Mario Party from the N64"""
        gameSelect=random.choice(n64MPList)
        await ctx.respond(gameSelect)
    
    #Game Subcommand
    @game.command(name='marioparty-gc')
    async def marioparty(self, ctx):
        """Pick a Mario Party form the GameCube"""
        gameSelect=random.choice(gcMPList)
        await ctx.respond(gameSelect)
    
    #Game Subcommand
    @game.command(name='marioparty-gc8')
    async def marioparty(self, ctx):
        """Pick a Mario Party from 4-8"""
        gameSelect=random.choice(mp8List)
        await ctx.respond(gameSelect)
    
    #Game Subcommand
    @game.command(name='marioparty-wii')
    async def marioparty(self, ctx):
        """Pick a Mario Party"""
        gameSelect=random.choice(wiiMPList)
        await ctx.respond(gameSelect)

    #Game Subcommand
    @game.command(name='marioparty-netplayable')
    async def marioparty(self, ctx):
        """Pick a Mario Party that you can play over Netplay"""
        gameSelect=random.choice(n64MPList + gcMPList + wiiMPList)
        await ctx.respond(gameSelect)

    @game.command(name='nintendo-64')
    async def n64(self, ctx):
        """Pick a N64 Game"""
        gameSelect=random.choice(n64List)
        await ctx.respond(gameSelect)
        
    @game.command()
    async def gamecube(self, ctx):
        """Pick a GameCube Game"""
        gameSelect=random.choice(gcList)
        await ctx.respond(gameSelect)    

    @game.command()
    async def wii(self, ctx):
        """Pick a Wii Game"""
        gameSelect=random.choice(wiiList)
        await ctx.respond(gameSelect)

    @game.command()
    async def all(self, ctx):
        """Pick any Game"""
        gameSelect=random.choice(wiiList + gcList + n64List)
        await ctx.respond(gameSelect)

    
def setup(bot):
    bot.add_cog(Fun(bot))
