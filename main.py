from discord.ext import commands
import discord
import os
from scraper import scrape_tournaments

# Load the bot token from the environment variables
TOKEN = os.getenv("DISCORD_TOKEN")

# Define the bot's intents
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent
intents.guilds = True  # Enable guild-related events
intents.members = True  # Enable member-related events

# Initialize the bot
bot = commands.Bot(command_prefix="!", intents=intents)

# Role-to-tournament type mapping
ROLE_TO_TYPE_MAPPING = {
    "M": "M",  # Men's tournaments
    "W": "W",  # Women's tournaments
    "RCO": "RCO"  # Reverse coed tournaments
}

@bot.command(name="femboy")
async def femboy_command(ctx):
    await ctx.send("Kelso a bitch")

@bot.command(name="gay")
async def femboy_command(ctx):
    await ctx.send("Kelso an even bigger bitch than I thought")

@bot.command(name="kelso")
async def femboy_command(ctx):
    await ctx.send("please kill urself")

@bot.command(name="fortnite")
async def femboy_command(ctx):
    await ctx.send("I like kids")

@bot.command(name="jared")
async def femboy_command(ctx):
    await ctx.send("データベースを使用する")

@bot.command(name="katie")
async def femboy_command(ctx):
    await ctx.send("PR OR ER")

@bot.command(name="mikeD")
async def femboy_command(ctx):
    await ctx.send("cs?")

# Command: Fetch tournaments with role-based filtering
@bot.command(name="upcoming")
async def tourney_command(ctx):
    """
    Fetch tournaments based on the roles assigned to the user.
    """
    # Scrape tournaments or load from cache
    tournaments = scrape_tournaments()

    # Get the roles of the user
    user_roles = [role.name for role in ctx.author.roles]

    # Determine the types to filter based on user roles
    allowed_types = [ROLE_TO_TYPE_MAPPING[role] for role in user_roles if role in ROLE_TO_TYPE_MAPPING]

    # If the user has no matching roles, inform them
    if not allowed_types:
        await ctx.send("You do not have any roles that match tournament types (M, W, RCO).")
        return

    # Filter tournaments based on allowed types
    filtered_tournaments = [
        t for t in tournaments if t["type"] in allowed_types
    ]

    # Respond with the filtered results
    if not filtered_tournaments:
        await ctx.send("No tournaments found that match your roles.")
        return

    # Sort by date and limit to the top 10 nearest tournaments
    filtered_tournaments = sorted(filtered_tournaments, key=lambda x: x["date"])[:10]

    # Build and send the response
    message = "**Tournaments Based on Your Roles:**\n"
    for t in filtered_tournaments:
        message += (
            f"🔹 **Name:** {t['name']}\n"
            f"   🔸 **Date:** {t['date']}\n"
            f"   🔸 **Location:** {t['location']}\n"
            f"   🔸 **Max Teams:** {t['max_teams']}\n"
            f"   🔸 **Confirmed Teams:** {t['confirmed']}\n"
            f"   🔸 **Status:** {t['status']}\n\n"
        )
    await ctx.send(message)

# Run the bot
if __name__ == "__main__":
    bot.run(TOKEN)
