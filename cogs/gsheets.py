import discord
from discord.ext import commands
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import os
import pickle

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# here enter the id of your google sheet
SAMPLE_SPREADSHEET_ID_input = '1QapLYYIlq2vaWRuF1HDEuT6tfZI0T5J40zaTC8c8cOA'

class GSheets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def get_data_from_sheet(self):
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_input,
                                     range='E3:E99999').execute()
        values = result.get('values', [])

        return values

    @commands.command()
    async def fetch_data(self, ctx):
        data = await self.get_data_from_sheet()
        if not data:
            await ctx.send("No data found.")
            return

        embed = discord.Embed(title="Points", color=0x00ff00)
        for row in data:
            if len(row) >= 5:
                name = row[0]
                column_e_data = row[4]
                embed.add_field(name=name, value=column_e_data, inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(GSheets(bot))