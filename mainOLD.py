import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Set up intents
intents = discord.Intents.default()  # Default intents
intents.message_content = True  # Enable message content intent

# Initialize bot with intents
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command(name="test")
async def test_command(ctx):
    await ctx.send("Bot is running!")

# Run the bot
bot.run(TOKEN)
