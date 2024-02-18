import discord
from discord.ext import commands
from googleapiclient.discovery import build
from discord import SlashCommandGroup
from google.oauth2.service_account import Credentials
import os

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Replace 'your_spreadsheet_id' with the actual ID of your Google Sheets spreadsheet
SAMPLE_SPREADSHEET_ID_input = '1QapLYYIlq2vaWRuF1HDEuT6tfZI0T5J40zaTC8c8cOA'

def get_ordinal_suffix(number):
    if 10 <= number % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(number % 10, 'th')
    return f"{number}{suffix}"

class GSheets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.credentials = None

    leaderboard = SlashCommandGroup("leaderboard", "Leaderboard related commands")

    async def get_data_for_pts(self):
        if not self.credentials:
            self.credentials = Credentials.from_service_account_file(
                'service.json',
                scopes=SCOPES
            )

        try:
            service = build('sheets', 'v4', credentials=self.credentials)
            sheet = service.spreadsheets()

            # Get data from range A3:A10
            result_a = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_input,
                                           range='A3:A32').execute()
            values_a = result_a.get('values', [])

            # Get data from range B3:B10
            result_b = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_input,
                                           range='B3:B32').execute()
            values_b = result_b.get('values', [])

            # Get data from range C3:C10
            result_c = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_input,
                                           range='C3:C32').execute()
            values_c = result_c.get('values', [])

            # Combine data from both ranges
            combined_data = [(a, b, c) for a, b, c in zip(values_a, values_b, values_c)]
            return combined_data
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    async def get_data_for_diamond(self):
        if not self.credentials:
            self.credentials = Credentials.from_service_account_file(
                'service.json',
                scopes=SCOPES
            )

        try:
            service = build('sheets', 'v4', credentials=self.credentials)
            sheet = service.spreadsheets()

            result_a = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_input,
                                           range='B3:B32').execute()
            values_a = result_a.get('values', [])

            result_b = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_input,
                                           range='E3:E32').execute()
            values_b = result_b.get('values', [])

            # Combine data from both ranges
            combined_data = [(a, b) for a, b in zip(values_a, values_b)]
            combined_data.sort(key=lambda x: x[1], reverse=True)
            return combined_data
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    async def get_data_for_gold(self):
        if not self.credentials:
            self.credentials = Credentials.from_service_account_file(
                'service.json',
                scopes=SCOPES
            )

        try:
            service = build('sheets', 'v4', credentials=self.credentials)
            sheet = service.spreadsheets()

            result_a = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_input,
                                           range='B3:B32').execute()
            values_a = result_a.get('values', [])

            result_b = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_input,
                                           range='F3:F32').execute()
            values_b = result_b.get('values', [])

            # Combine data from both ranges
            combined_data = [(a, b) for a, b in zip(values_a, values_b)]
            combined_data.sort(key=lambda x: x[1], reverse=True)
            return combined_data
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    async def get_data_for_silver(self):
        if not self.credentials:
            self.credentials = Credentials.from_service_account_file(
                'service.json',
                scopes=SCOPES
            )

        try:
            service = build('sheets', 'v4', credentials=self.credentials)
            sheet = service.spreadsheets()

            result_a = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_input,
                                           range='B3:B32').execute()
            values_a = result_a.get('values', [])

            result_b = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_input,
                                           range='G3:G32').execute()
            values_b = result_b.get('values', [])

            # Combine data from both ranges
            combined_data = [(a, b) for a, b in zip(values_a, values_b)]
            combined_data.sort(key=lambda x: x[1], reverse=True)
            return combined_data
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    async def get_data_for_bronze(self):
        if not self.credentials:
            self.credentials = Credentials.from_service_account_file(
                'service.json',
                scopes=SCOPES
            )

        try:
            service = build('sheets', 'v4', credentials=self.credentials)
            sheet = service.spreadsheets()

            result_a = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_input,
                                           range='B3:B32').execute()
            values_a = result_a.get('values', [])

            result_b = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_input,
                                           range='H3:H32').execute()
            values_b = result_b.get('values', [])

            # Combine data from both ranges
            combined_data = [(a, b) for a, b in zip(values_a, values_b)]
            combined_data.sort(key=lambda x: x[1], reverse=True)
            return combined_data
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    @leaderboard.command(name="points")
    async def points(self, ctx):
        data = await self.get_data_for_pts()
        if data:
            embed = discord.Embed(title="Top 30 Players (pts)", color=0x00ff00)
            for index, item in enumerate(data, start=1):
                ordinal_index = get_ordinal_suffix(int(str(item[0])[2:-2]))
                embed.add_field(name=f"{ordinal_index} - {str(item[1])[2:-2]}", value=str(item[2])[2:-2] + " pts")
                embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Doopliss")
            await ctx.respond(embed=embed)
        else:
            await ctx.respond("Failed to retrieve data from the spreadsheet.")

    @leaderboard.command(name="diamond")
    async def diamond(self, ctx):
        data = await self.get_data_for_diamond()
        if data:
            embed = discord.Embed(title="Top 30 Players winning 1st (Diamond Rank)", color=0xb9f2ff)
            for index, item in enumerate(data, start=1):
                embed.add_field(name=f"{str(item[0])[2:-2]}", value=str(item[1])[2:-2] + " Diamond Ranks")
                embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Doopliss")
            await ctx.respond(embed=embed)
        else:
            await ctx.respond("Failed to retrieve data from the spreadsheet.")
    
    @leaderboard.command(name="gold")
    async def gold(self, ctx):
        data = await self.get_data_for_gold()
        if data:
            embed = discord.Embed(title="Top 30 Players winning 2nd (Gold Rank)", color=0xffd700)
            for index, item in enumerate(data, start=1):
                embed.add_field(name=f"{str(item[0])[2:-2]}", value=str(item[1])[2:-2] + " Gold Ranks")
                embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Doopliss")
            await ctx.respond(embed=embed)
        else:
            await ctx.respond("Failed to retrieve data from the spreadsheet.")

    @leaderboard.command(name="silver")
    async def silver(self, ctx):
        data = await self.get_data_for_silver()
        if data:
            embed = discord.Embed(title="Top 30 Players winning 3rd (Silver Rank)", color=0xc0c0c0)
            for index, item in enumerate(data, start=1):
                embed.add_field(name=f"{str(item[0])[2:-2]}", value=str(item[1])[2:-2] + " Silver Ranks")
                embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Doopliss")
            await ctx.respond(embed=embed)
        else:
            await ctx.respond("Failed to retrieve data from the spreadsheet.")
    
    @leaderboard.command(name="bronze")
    async def bronze(self, ctx):
        data = await self.get_data_for_bronze()
        if data:
            embed = discord.Embed(title="Top 30 Players winning 4th (Bronze Rank)", color=0xcd7f32)
            for index, item in enumerate(data, start=1):
                embed.add_field(name=f"{str(item[0])[2:-2]}", value=str(item[1])[2:-2] + " Bronze Ranks")
                embed.set_footer(text=f"Ran by: {ctx.author} • Yours truly, Doopliss")
            await ctx.respond(embed=embed)
        else:
            await ctx.respond("Failed to retrieve data from the spreadsheet.")

def setup(bot):
    bot.add_cog(GSheets(bot))
