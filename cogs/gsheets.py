import discord
from discord.ext import commands
from googleapiclient.discovery import build
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

    async def get_data_from_sheet(self):
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
                                           range='A3:A17').execute()
            values_a = result_a.get('values', [])

            # Get data from range B3:B10
            result_b = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_input,
                                           range='B3:B17').execute()
            values_b = result_b.get('values', [])

            # Get data from range C3:C10
            result_c = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_input,
                                           range='C3:C17').execute()
            values_c = result_c.get('values', [])

            # Combine data from both ranges
            combined_data = [(a, b, c) for a, b, c in zip(values_a, values_b, values_c)]
            return combined_data
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    @commands.command()
    async def fetch_data(self, ctx):
        data = await self.get_data_from_sheet()
        if data:
            embed = discord.Embed(title="Top 15 Players (pts)", color=0x00ff00)
            for index, item in enumerate(data, start=1):
                ordinal_index = get_ordinal_suffix(int(str(item[0])[2:-2]))
                embed.add_field(name=f"{ordinal_index} - {str(item[1])[2:-2]}", value=str(item[2])[2:-2])
            await ctx.send(embed=embed)
        else:
            await ctx.send("Failed to retrieve data from the spreadsheet.")

def setup(bot):
    bot.add_cog(GSheets(bot))
