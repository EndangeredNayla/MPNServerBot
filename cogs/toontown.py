import discord
import json
import re
import requests

from discord.ext import commands

class Toontown(commands.Cog):

    """Cog for Toontown commands"""

    def __init__(self, bot):
        self.bot = bot

    #TTR Invasions Command
    @commands.slash_command(pass_context=True, aliases=["ttr_invasions"])
    async def ttrinvasions(self, ctx):
        ttr_invasions_api = "https://www.toontownrewritten.com/api/invasions"
        ttr_invasions_response = requests.get(ttr_invasions_api, verify=True)
        ttr_invasions_json = ttr_invasions_response.json()
        ttr_invasions = ttr_invasions_json["invasions"]
        invasions = []
        try:
            for invasion in list(ttr_invasions.keys()):
                districtName = invasion
                cogType = ttr_invasions[invasion]["type"]
                cogType = cogType.replace("\u0003", "")
                cogProgress = ttr_invasions[invasion]["progress"]
                cogProgress = cogProgress.replace("0/1000000", "MEGA Invasion!")
                invasions.append("{}: {} ({})".format(districtName, cogType, cogProgress))

            ttr_invasions = "\n".join(sorted(invasions))
        except:
            ttr_invasions = "No Invasions"
        embed = discord.Embed(
            title=f'Toontown Rewritten Invasions',
            description='\uFEFF',
            colour=0x98FB98)
        embed.set_thumbnail(url="https://i.ibb.co/RzrzDVh/TTR.png")
        embed.add_field(name="Invasions:", value=ttr_invasions, inline=True)
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, {ctx.author}")
        embed.set_author(name=ctx.author, icon_url=self.bot.user.avatar.url)
        await channel.send(embed=embed)

    #TTCC Invasions Command
    @commands.slash_command(pass_context=True, aliases=["ttcc_invasions"])
    async def ttccinvasions(self, ctx):
        ttcc_invasions_api = "https://corporateclash.net/api/v1/districts.js"
        ttcc_invasions_response = requests.get(ttcc_invasions_api, verify=True)
        ttcc_invasions = ttcc_invasions_response.json()
        invasions = []

        try:
          for invasion in ttcc_invasions:
              if "None" == invasion['cogs_attacking']:
                  pass
              else:
                  districtName = invasion['name']
                  cogType = invasion['cogs_attacking']
                  countDefeated = invasion['count_defeated']
                  countTotal = invasion['count_total']
                  invasions.append("{}: {} ({}/{})".format(districtName, cogType, countDefeated, countTotal))

          ttcc_invasions = "\n".join(sorted(invasions))
        except:
            ttcc_invasions = "No Invasions"

        embed = discord.Embed(
            title=f'Corporate Clash Invasions',
            description='\uFEFF',
            colour=0x98FB98,
            timestamp=ctx.message.created_at)
        embed.set_thumbnail(url="https://sitecdn.corporateclash.net/logo1.1/icon-focused-300x300.png")
        embed.add_field(name="Invasions:", value=ttcc_invasions, inline=True)
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, {ctx.author}")
        embed.set_author(name=ctx.author, icon_url=self.bot.user.avatar.url)
        await ctx.send(content=None, embed=embed)

    #TVS Invasions Command
    @commands.slash_command(pass_context=True, aliases=["tvs_invasions"])
    async def tvsinvasions(self, ctx):
        tvs_invasions_api = "https://tooniversal.com/api/districts"
        tvs_invasions_response = requests.get(tvs_invasions_api, verify=True)
        tvs_invasions_json = tvs_invasions_response.json()
        tvs_invasions = tvs_invasions_json["districts"]
        invasions = []

        try:
          for invasion in list(tvs_invasions.keys()):
              if 'invasion' in tvs_invasions[invasion]:
                  districtName = invasion
                  cogType = tvs_invasions[invasion]['invasion']['type']
                  countRemaining = tvs_invasions[invasion]['invasion']['remaining']
                  countTotal = tvs_invasions[invasion]['invasion']['total']
                  countDefeated = int(countTotal) - int(countRemaining)
                  invasions.append("{}: {} ({}/{})".format(districtName, cogType, countDefeated, countTotal))
              else:
                  pass
        except:
            tvs_invasions = "No Invasions"

        embed = discord.Embed(
            title=f'Tooniversal Invasions',
            description='\uFEFF',
            colour=0x98FB98,
            timestamp=ctx.message.created_at)
        embed.set_thumbnail(url="https://tooniversal.com/static/fav/android-icon-192x192.png")
        embed.add_field(name="Invasions:", value=tvs_invasions, inline=True)
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, {ctx.author}")
        embed.set_author(name=ctx.author, icon_url=self.bot.user.avatar.url)
        await ctx.send(content=None, embed=embed)

    #ODS Invasions Command
    @commands.slash_command(pass_context=True, aliases=["ods_invasions"])
    async def odsinvasions(self, ctx):
        ods_invasions_api = "https://opdessertstorm.com/api/districts"
        ods_invasions_response = requests.get(ods_invasions_api, verify=True)
        ods_invasions_json = ods_invasions_response.json()
        ods_invasions = ods_invasions_json["districts"]
        invasions = []

        for invasion in list(ods_invasions.keys()):
            if 'invasion' in ods_invasions[invasion]:
                districtName = invasion
                cogType = ods_invasions[invasion]['invasion']['type']
                invasions.append("{}: {}".format(districtName, cogType))
            else:
                pass
            
        ods_invasions = "\n".join(sorted(invasions))

        embed = discord.Embed(
            title=f'Operation: Dessert Storm Invasions',
            description='\uFEFF',
            colour=0x98FB98,
            timestamp=ctx.message.created_at)
        embed.set_thumbnail(url="https://opdessertstorm.com/static/assets/img/favicon.ico")
        embed.add_field(name="Invasions:", value=ods_invasions, inline=True)
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, {ctx.author}")
        embed.set_author(name=ctx.author, icon_url=self.bot.user.avatar.url)
        await ctx.send(content=None, embed=embed)

    #TTF Invasions Command
    @commands.slash_command(pass_context=True, aliases=["ttf_invasions"])
    async def ttfinvasions(self, ctx):
        ttf_invasions_api = "https://reg.toontownfellowship.com/api/invasions"
        ttf_invasions_response = requests.get(ttf_invasions_api, verify=True)
        ttf_invasions_json = ttf_invasions_response.json()
        ttf_invasions = ttf_invasions_json["invasions"]
        invasions = []
        try:
          for invasion in ttf_invasions:
              districtName = invasion["districtName"]
              cogType = invasion["cogName"]
              cogType = cogType.replace("\u0003", "")
              countRemaining = invasion["remaining"]
              countTotal = invasion['total']
              countDefeated = int(countTotal) - int(countRemaining)
              invasions.append("{}: {} ({}/{})".format(districtName, cogType, countDefeated, countTotal))
        except:
            ttf_invasions = "No Invasions"

        ttf_invasions = "\n".join(sorted(invasions))

        embed = discord.Embed(
            title=f'Toontown Fellowship Invasions',
            description='\uFEFF',
            colour=0x98FB98,
            timestamp=ctx.message.created_at)
        embed.set_thumbnail(url="https://i.ibb.co/NtStS9V/Icon5.png")
        embed.add_field(name="Invasions:", value=ttf_invasions, inline=True)
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, {ctx.author}")
        embed.set_author(name=ctx.author, icon_url=self.bot.user.avatar.url)
        await ctx.send(content=None, embed=embed)

    #TTR Districts Command
    @commands.slash_command(pass_context=True, aliases=["ttr_districts", "ttr"])
    async def ttrdistricts(self, ctx):
        ttr_districts_api = "https://www.toontownrewritten.com/api/population"
        ttr_districts_response = requests.get(ttr_districts_api, verify=True)
        ttr_districts_json = ttr_districts_response.json()
        total_pop = ttr_districts_json["totalPopulation"]

        ttr_districts = ttr_districts_json["populationByDistrict"]
        districts = []

        for district in list(ttr_districts.keys()):
            districtName = district
            popNumber = ttr_districts[district]
            districts.append("{}: {}".format(districtName, popNumber))
       
        ttr_districts = "\n".join(sorted(districts))

        ttr_districts = "Total Population: " + str(total_pop) + "\n\n" + ttr_districts
        embed = discord.Embed(
            title=f'Toontown Rewritten Population',
            description='\uFEFF',
            colour=0x98FB98,
            timestamp=ctx.message.created_at)
        embed.set_thumbnail(url="https://i.ibb.co/RzrzDVh/TTR.png")
        embed.add_field(name="Population:", value=ttr_districts, inline=True)
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, {ctx.author}")
        embed.set_author(name=ctx.author, icon_url=self.bot.user.avatar.url)
        await ctx.send(content=None, embed=embed)

    #TTCC Districts Command
    @commands.slash_command(pass_context=True, aliases=["ttcc_districts", "ttcc"])
    async def ttccdistricts(self, ctx):
        ttcc_totalpop_api = "https://corporateclash.net/api/v1/game_info.js"
        ttcc_totalpop_response = requests.get(ttcc_totalpop_api, verify=True)
        ttcc_totalpop_json = ttcc_totalpop_response.json()
        
        ttcc_total_pop = ttcc_totalpop_json["num_toons"]
        
        ttcc_districts_api = "https://corporateclash.net/api/v1/districts.js"
        ttcc_districts_response = requests.get(ttcc_districts_api, verify=True)
        ttcc_districts = ttcc_districts_response.json()
        
        districts = []
        populationCount = []
        
        for district in ttcc_districts:
            districts.append("{}: {}".format(district['name'], district['population']))
        
        ttcc_districts = "\n".join(sorted(districts))
        ttcc_districts = "Total Population: " + str(ttcc_total_pop) + "\n\n" + ttcc_districts


        embed = discord.Embed(
            title=f'Corporate Clash Population',
            description='\uFEFF',
            colour=0x98FB98,
            timestamp=ctx.message.created_at)
        embed.set_thumbnail(url="https://sitecdn.corporateclash.net/logo1.1/icon-focused-300x300.png")
        embed.add_field(name="Population:", value=ttcc_districts, inline=True)
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, {ctx.author}")
        embed.set_author(name=ctx.author, icon_url=self.bot.user.avatar.url)
        await ctx.send(content=None, embed=embed)

    #TVS Districts Command
    @commands.slash_command(pass_context=True, aliases=["tvs_districts", "tvs"])
    async def tvsdistricts(self, ctx):
        tvs_districts_api = "https://tooniversal.com/api/districts"
        tvs_districts_response = requests.get(tvs_districts_api, verify=True)
        tvs_districts_json = tvs_districts_response.json()
        tvs_districts = tvs_districts_json["districts"]

        districts = []
        populationCount = []

        for district in list(tvs_districts.keys()):
            districtName = district
            popNumber = tvs_districts[district]['population']
            districts.append("{}: {}".format(districtName, popNumber))
            populationCount.append("{}".format(popNumber))


        populationCount = " ".join(populationCount)
        populationCount = list(populationCount.split(" "))
        populationCount = [ int(x) for x in populationCount ]
        total_pop = sum(populationCount)

        tvs_districts = "\n".join(sorted(districts))
        tvs_districts2 = "Total Population: " + str(total_pop) + "\n\n" + tvs_districts

        embed = discord.Embed(
            title=f'Tooniversal Studios Population',
            description='\uFEFF',
            colour=0x98FB98,
            timestamp=ctx.message.created_at)
        embed.set_thumbnail(url="https://tooniversal.com/static/fav/android-icon-192x192.png")
        embed.add_field(name="Population:", value=tvs_districts2, inline=True)
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, {ctx.author}")
        embed.set_author(name=ctx.author, icon_url=self.bot.user.avatar.url)
        await ctx.send(content=None, embed=embed)

    #ODS Districts Command
    @commands.slash_command(pass_context=True, aliases=["ods_districts", "ods"])
    async def odsdistricts(self, ctx):
        ods_districts_api = "https://opdessertstorm.com/api/districts"
        ods_districts_response = requests.get(ods_districts_api, verify=True)
        ods_districts_json = ods_districts_response.json()
        ods_districts = ods_districts_json["districts"]
        
        districts = []
        populationCount = []
        try:
          for district in list(ods_districts.keys()):
              districtName = district
              popNumber = ods_districts[district]['population']
              districts.append("{}: {}".format(districtName, popNumber))
              populationCount.append("{}".format(popNumber))
        except:
            ttr_invasions = "No Invasions"
        
        
        populationCount = " ".join(populationCount)
        populationCount = list(populationCount.split(" "))
        populationCount = [ int(x) for x in populationCount ]
        total_pop = sum(populationCount)
        
        ods_districts = "\n".join(sorted(districts))
        ods_districts2 = "Total Population: " + str(total_pop) + "\n\n" + ods_districts

        embed = discord.Embed(
            title=f'Operation: Dessert Storm Population',
            description='\uFEFF',
            colour=0x98FB98,
            timestamp=ctx.message.created_at)
        embed.set_thumbnail(url="https://opdessertstorm.com/static/assets/img/favicon.ico")
        embed.add_field(name="Population:", value=ods_districts2, inline=True)
        embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, {ctx.author}")
        embed.set_author(name=ctx.author, icon_url=self.bot.user.avatar.url)
        await ctx.send(content=None, embed=embed)

def setup(bot):
    bot.add_cog(Toontown(bot))