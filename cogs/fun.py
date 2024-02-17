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
        
    global whatsInBoxList
    whatsInBoxList=["<a:BowserDance:687668560193126428>", "<a:BabyBowserFast:687678432045170689>", "<a:BabyBowser:404197234436079618>", "<a:BabyBowser:404197234436079618>", "<a:ToadBoat:739621939894550600>", "<a:ToadBoat:739621939894550600>", "<a:ToadDance2Fast:690633607382827069>", "<a:DKWave:902392049347739669>"]
    
    global raceList
    raceList=["<:datrBobomb:682698795686953011>", "<:datrBoo:682698795951325213>", "<:datrThwomp:682698795477368834>", "<:datrWhomp:682698795980423266>"]

    #Roll Command
    @commands.slash_command(aliases=["party"])
    async def roll(self, ctx, min: int, max:int, count:int):
        
        """Roll a dice, default is rolling 1d6. (minNumber, maxNumber, diceCount)"""
        if count <= 20:
            for _ in range(count):
                await ctx.respond(random.randint(min, max))
        if count > 20:
            await ctx.respond('Invalid number of rolls')

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

    @commands.slash_command()
    async def drama(self, ctx):
        """Sends you drama"""
        drama = requests.get('http://staff.toonisland.online:3002/raw')
        await ctx.respond(drama.text)

    @commands.slash_command()
    async def mpfont(self, ctx, text: str):
        """Sends given text in MP font"""
        text = text.lower()
        text = text.replace("a", "<:MPA:705586267324285021>")
        text = text.replace("b", "<:MPB:705586281463414816>")
        text = text.replace("c", "<:MPC:705586292301496320>")
        text = text.replace("d", "<:MPD:705586303139446784>")
        text = text.replace("e", "<:MPE:705586313042329730>")
        text = text.replace("f", "<:MPF:705586322689228891>")
        text = text.replace("g", "<:MPG:836775866738016307>")
        text = text.replace("h", "<:MPH:705586341450219560>")
        text = text.replace("i", "<:MPI:705586351122284574>")
        text = text.replace("j", "<:MPJ:705586360538628237>")
        text = text.replace("k", "<:MPK:705586374228705311>")
        text = text.replace("l", "<:MPL:705586383019966545>")
        text = text.replace("m", "<:MPM:827397829538349099>")
        text = text.replace("n", "<:MPN:705586402632401018>")
        text = text.replace("o", "<:MPO:836775888066314290>")
        text = text.replace("p", "<:MPP:836775916091736105>")
        text = text.replace("q", "<:MPQ:705586443493310564>")
        text = text.replace("r", "<:MPR:705586460136439819>")
        text = text.replace("s", "<:MPS:705586606370848778>")
        text = text.replace("t", "<:MPT:705586620186886184>")
        text = text.replace("u", "<:MPU:705587057510318162>")
        text = text.replace("v", "<:MPV:705587070734958603>")
        text = text.replace("w", "<:MPW:705587083393368135>")
        text = text.replace("x", "<:MPX:705587097150685225>")
        text = text.replace("y", "<:MPY:705587108584095784>")
        text = text.replace("z", "<:MPZ:705587120370352198>")
        text = text.replace("!", "<:MPExclamation:705594132181287022") 
        text = text.replace(" ", "          ")    
        await ctx.respond(text)

    @commands.slash_command()
    async def mpfontshake(self, ctx, text: str):
        """Sends given text in MP font"""
        text = text.upper()
        text = text.replace("A", "<a:mp1a:706974442160521287>")
        text = text.replace("B", "<a:mp1b:706974442328424482>")
        text = text.replace("C", "<a:mp1c:706974441976102932>")
        text = text.replace("D", "<a:mp1d:706974442215047178>")
        text = text.replace("E", "<a:mp1e:706974442219241472>")
        text = text.replace("F", "<a:mp1f:706974441762193420>")
        text = text.replace("G", "<a:mp1g:706974441929965648>")
        text = text.replace("H", "<a:mp1h:706974441946480650>")
        text = text.replace("I", "<a:mp1i:706974441699278880>")
        text = text.replace("J", "<a:mp1j:706974441791291515>")
        text = text.replace("K", "<a:mp1k:706974441850273913>")
        text = text.replace("L", "<a:mp1l:706974441850011698>")
        text = text.replace("M", "<a:mp1m:827400882713919488>")
        text = text.replace("N", "<a:mp1n:706974441833496646>")
        text = text.replace("O", "<a:mp1o:706974441560604707>")
        text = text.replace("P", "<a:mp1p:706974441636233336>")
        text = text.replace("Q", "<a:mp1q:706974441208545352>")
        text = text.replace("R", "<a:mp1r:706974441791291522>")
        text = text.replace("S", "<a:mp1s:706974441241837622>")
        text = text.replace("T", "<a:mp1t:706974440633663601>")
        text = text.replace("U", "<a:mp1u:706974441686433802>")
        text = text.replace("V", "<a:mp1v:706974440864612362>")
        text = text.replace("W", "<a:mp1w:706974440847573102>")
        text = text.replace("X", "<a:mp1x:706974440738521195>")
        text = text.replace("Y", "<a:mp1y:706974440587788361>")
        text = text.replace("Z", "<a:mp1z:706974440864481321>")
        text = text.replace("!", "<a:mp1ex:706974440663154749>") 
        text = text.replace("?", "<a:mp1qu:706974440210038928>") 
        text = text.replace(" ", "          ")    
        await ctx.respond(text)

    @commands.slash_command()
    async def mpfontflash(self, ctx, text: str):
        """Sends given text in MP font"""
        text = text.upper()
        text = text.replace("A", "<a:mp2a:706974441854205982>")
        text = text.replace("B", "<a:mp2b:706974442311385200>")
        text = text.replace("C", "<a:mp2c:706974442353590312>")
        text = text.replace("D", "<a:mp2d:706974442403790948>")
        text = text.replace("E", "<a:mp2e:706974441955000440>")
        text = text.replace("F", "<a:mp2f:706974444270387301>")
        text = text.replace("G", "<a:mp2g:706974442055532648>")
        text = text.replace("H", "<a:mp2h:706974441984360500>")
        text = text.replace("I", "<a:mp2i:706974441816457277>")
        text = text.replace("J", "<a:mp2j:706974442026434660>")
        text = text.replace("K", "<a:mp2k:706974441099493454>")
        text = text.replace("L", "<a:mp2l:706974441804005499>")
        text = text.replace("M", "<a:mp2m:827400882013339669>")
        text = text.replace("N", "<a:mp2n:706974441850273912>")
        text = text.replace("O", "<a:mp2o:706974442248471051>")
        text = text.replace("P", "<a:mp2p:706974441430712329>")
        text = text.replace("Q", "<a:mp2q:706974441434775583>")
        text = text.replace("R", "<a:mp2r:706974440994504755>")
        text = text.replace("S", "<a:mp2s:706974440688451627>")
        text = text.replace("T", "<a:mp2t:706974441128591442>")
        text = text.replace("U", "<a:mp2u:706974440873001020>")
        text = text.replace("V", "<a:mp2v:706974440914812958>")
        text = text.replace("W", "<a:mp2w:706974440847835206>")
        text = text.replace("X", "<a:mp2x:706974440684257283>")
        text = text.replace("Y", "<a:mp2y:706974440805630024>")
        text = text.replace("Z", "<a:mp2z:706974440252244041>")
        text = text.replace("!", "<a:mp2ex:706974440591720548>") 
        text = text.replace("?", "<a:mp2qu:706974440478736384>") 
        text = text.replace(" ", "          ")    
        await ctx.respond(text)

    #Box Command
    @commands.slash_command()
    async def whatsinthebox(self, ctx):
        """Who is in the box"""
        box=random.choice(whatsInBoxList)
        await ctx.respond(box + " is in the box!")
    
    #Day at the Races Command
    @commands.slash_command()
    async def dayattheraces(self, ctx):
        """Mock day at the races"""
        box=random.sample(raceList, 4)
        boxMain = str(box).replace("[", "")
        boxMain = boxMain.replace("]", "")
        boxMain = boxMain.replace("'", "")
        boxMain = boxMain.replace(",", "")
        await ctx.respond("Day At The Races: Results\n\n" + boxMain)

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
        gameSelect=random.choice(gcMPList + "Mario Party 8")
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

    @commands.slash_command()
    async def mpiq(self, ctx, id=None):
        """Mario Party IQ"""
        await ctx.respond("Quiz Starting...")
        if id == None:
            Decider = str(random.randint(1,100))
        else:
            Decider = id
        mylines = []
        with open ('mpiq/Q' + Decider + '.txt', 'rt') as myfile:
            for myline in myfile:
                mylines.append(myline)
            Difficulty = (mylines[0]) 
            Game = (mylines[1]) 
            Question = (mylines[2]) 
            AnswerList = (mylines[3])
            ExactAnswer = (mylines[4])

        await ctx.respond("#" + str(Decider) + " | " + Difficulty + Game)
        await ctx.send(Question)
        def check(m):
            return ctx.author == m.author
        msg = await self.bot.wait_for('message', timeout=60.0, check=check)
        AnswerList = AnswerList.replace(" ", "#")
        if msg.content.lower() in AnswerList:
            await ctx.send("**Correct Answer!**")
        else:
            await ctx.send("**Wrong Answer!** <:Thwomp:266840621149454348> Correct Answer was *" + ExactAnswer + "*")

def setup(bot):
    bot.add_cog(Fun(bot))