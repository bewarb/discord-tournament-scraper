import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from scraper import scrape_tournaments
from filters import filter_tournaments

bot = commands.Bot(command_prefix="!")

@bot.command(name="tournaments")
async def tournaments_command(ctx, *, filters=None):
    """
    Command to fetch and filter tournaments.

    Args:
        ctx: Discord context.
        filters (str): User-provided filters in the format "key=value,key=value".
    """
    # Scrape tournaments or load from cache
    tournaments = scrape_tournaments()

    # Parse filters from user input
    filter_args = {}
    if filters:
        try:
            for f in filters.split(","):
                key, value = f.split("=")
                filter_args[key.strip()] = value.strip()
        except ValueError:
            await ctx.send("Invalid filter format. Use key=value,key=value.")
            return

    # Apply filters
    filtered_tournaments = filter_tournaments(tournaments, **filter_args)

    # Send results
    if not filtered_tournaments:
        await ctx.send("No tournaments found with the specified filters.")
        return

    message = "**Filtered Tournaments:**\n"
    for t in filtered_tournaments:
        message += f"🔹 **Name:** {t['name']} | **Date:** {t['date']} | **Location:** {t['location']} | **Type:** {t['type']}\n"
    await ctx.send(message)
