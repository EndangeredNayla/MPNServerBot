import discord
from discord.ext import commands, tasks
from pterosocket import PteroSocket
import json
import os

# Discord bot setup
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='/', intents=intents)

config_file_path = 'config.json'

def_config_data = {
    "api_key": "",
    "servers": {
    },
    "origin": "",
    "disc_token": ""
}

# Write to config.json
if os.path.exists(config_file_path):
    # Read the existing configuration
    with open(config_file_path, 'r') as config_file:
        config_data = json.load(config_file)
else:
    # Write the default configuration to config.json
    with open(config_file_path, 'w') as config_file:
        json.dump(def_config_data, config_file, indent=4)
    config_data = def_config_data  # Use the default data

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    read_messages.start()  # Start the read_messages loop

@tasks.loop(seconds=5)  # Adjust the interval as needed
async def read_messages():
    for server_info in servers.values():
        channel = bot.get_channel(server_info["channel_id"])
        if channel:
            messages = await channel.history(limit=10).flatten()
            for message in messages:
                if last_message_ids[server_info["id"]] is None or message.id > last_message_ids[server_info["id"]]:
                    await channel.send(f"{message.author}: {message.content}")  # Send new message content
                    last_message_ids[server_info["id"]] = message.id  # Update last message ID

@bot.command()
@discord.option("server", type=discord.SlashCommandOptionType.string, description="Select a server to start")
async def start(ctx, server: str):
    server_info = next((s for s in servers.values() if s["id"] == server), None)  # Get server info
    if server_info:
        channel_id = server_info["channel_id"]
        ptero_socket = PteroSocket(origin, api_key, server, auto_connect=False)
        await ptero_socket.connect()
        await ctx.respond(f"Server {server_info['name']} started!")  # Use server name

@bot.command()
@discord.option("server", type=discord.SlashCommandOptionType.string, description="Select a server to stop")
async def stop(ctx, server: str):
    server_info = next((s for s in servers.values() if s["id"] == server), None)  # Get server info
    if server_info:
        ptero_socket = PteroSocket(origin, api_key, server, auto_connect=False)
        await ptero_socket.close()
        await ctx.respond(f"Server {server_info['name']} stopped!")  # Use server name

# Run the bot
bot.run(disc_token)